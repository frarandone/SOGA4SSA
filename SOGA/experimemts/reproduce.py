import numpy as np
import scipy
import argparse
import glob
from pathlib import Path
import subprocess
import re
from numpy import dtype
import os
from difflib import SequenceMatcher
import time
import json

exp_timeout=10


def getT3SOGAPrograms(programList):
    pfile=open(programList,"r")
    analyzed_programs=pfile.readlines()
    pfile.close()
    
    analyzed_programsName=[ p.strip().split("[")[0].strip() for p in analyzed_programs]
    
    programs=[]
    allprograms=glob.glob("../**/programs/SOGA/**/*.soga",recursive=True)
    for p in allprograms:
        if(Path(p.strip()).name.split(".")[0].strip() in analyzed_programsName ):
            programs.append(Path(p.strip()))
    
    return programs
            
            
def getT3PSIPrograms(programList):
    pfile=open(programList,"r")
    analyzed_programs=pfile.readlines()
    pfile.close()
    
    analyzed_programsName=[ p.strip().split("[")[0].strip().lower() for p in analyzed_programs]
    
    programs=[]
    allprograms=glob.glob("../**/programs/PSI/**/*.psi",recursive=True)
    for p in allprograms:
        if(Path(p.strip()).name.split(".")[0].strip().lower() in analyzed_programsName ):
            programs.append(Path(p.strip()))
    
    return programs

def getT3STANPrograms(programList):
    pfile=open(programList,"r")
    analyzed_programs=pfile.readlines()
    pfile.close()
    
    analyzed_programsName=[ p.strip().split("[")[0].strip().lower() for p in analyzed_programs]
    
    programs=[]
    allprograms=glob.glob("../**/programs/STAN/**/*.stan",recursive=True)
    for p in allprograms:
        if(Path(p.strip()).name.split(".")[0].strip().lower() in analyzed_programsName ):
            programs.append(Path(p.strip()))
            
    return programs

def getT3AQUAPrograms(programList):
    pfile=open(programList,"r")
    analyzed_programs=pfile.readlines()
    pfile.close()
    
    analyzed_programsName=[ p.strip().split("[")[0].strip().lower() for p in analyzed_programs]
    
    programs=[]
    allprograms=glob.glob("../**/programs/AQUA/**/*.stan",recursive=True)
    for p in allprograms:
        if(Path(p.strip()).name.split(".")[0].strip().lower() in analyzed_programsName ):
            programs.append(Path(p.strip()))
    
    return programs

def getMatches(matches):
    res=[];
    for matchNum, match in enumerate(matches, start=1):
        #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            #print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum))) 
            res+=match.group(groupNum)
    return "".join(res) 

def runSOGA(program,tvars):
    print(str(program))
    
    out=subprocess.check_output(["python3","../src/SOGA.py","-f",program],text=True)
    
    rt_reg = r"Runtime:(\d+.\d+)"
    c_reg= r"c:(\d+)"
    d_reg= r"d:(\d+)"
    value_reg=r"E\[%s\]: (\d+.\d+)"%(re.escape(tvars[1].replace('"','').strip()))
     
    rt=getMatches(re.finditer(rt_reg, str(out).strip(), re.IGNORECASE));
    c=getMatches(re.finditer(c_reg, str(out).strip(), re.IGNORECASE));
    d=getMatches(re.finditer(d_reg, str(out).strip(), re.IGNORECASE));
    value=getMatches(re.finditer(value_reg, str(out).strip(), re.IGNORECASE));
    
    return [rt,c,d,value]


def runAQUA(program,tvars):
    print(program)
    stormfiles=glob.glob("%s/**/*.template"%(str(program.parent)),recursive=True)
    rt=-1
    mem=False
    to=False
    value=None
    if(len(stormfiles)==0):
        try:
            st=time.time()
            subprocess.check_call(["java","-cp",
                                     "target/aqua-1.0.jar:lib/storm-1.0.jar",
                                     "aqua.analyses.AnalysisRunner",
                                     "../%s"%(program.parent)],cwd="../tools/AQUA",timeout=exp_timeout,stdout=subprocess.DEVNULL,
                                     stderr=subprocess.STDOUT)
            rt=time.time()-st
        except subprocess.CalledProcessError as meme:
            mem=True
        except subprocess.TimeoutExpired as toe:
            to=True
    else:
        try:
            st=time.time()
            subprocess.check_call(["java","-cp",
                                     "target/aqua-1.0.jar:lib/storm-1.0.jar",
                                     "aqua.analyses.AnalysisRunner",
                                     "../%s"%(stormfiles[0])],cwd="../tools/AQUA",timeout=exp_timeout,
                                     stdout=subprocess.DEVNULL,
                                     stderr=subprocess.STDOUT)
            rt=time.time()-st
        except subprocess.CalledProcessError as meme:
            mem=True
        except subprocess.TimeoutExpired as toe:
            to=True
    
    if(mem==False and to==False):
        analisys=json.load(open("%s/analysis_%s.txt"%(str(program.parent),tvars[1].replace('"','').strip()),"r"))
        data=np.array(analisys["data"])
        value=np.dot(data[0,:],data[1,:])
    
    return [rt,value,mem,to]

def runPSI(program,tvars):
    print(program)
    rt=None
    mem=False
    to=False
    value=None
    
    ppath="../%s"%(program)
    
    try:
        st=time.time()
        cwd="../tools/psi"
        value=subprocess.check_output(["./psi",ppath,"--expectation","--raw","--mathematica"],timeout=exp_timeout,cwd=cwd,text=True)
        rt=time.time()-st
        f=open("results/psi_formula/%s.txt"%(program.name.split(".")[0]),"w+")
        f.write(value)
        f.close()
    except subprocess.CalledProcessError as meme:
        mem=True
    except subprocess.TimeoutExpired as toe:
        to=True
    
    return [rt,value,mem,to]

def runSTAN(program,tvars):
    ppath="../%s/%s"%(program.parent,program.name.split(".")[0])
    print(program)
    rt=None
    mem=False
    to=False
    value=None
    
    cwd="../tools/cmdstan-2.32.0"
    subprocess.check_call(["make",ppath],cwd=cwd)
    if(Path("%s/%s.data.R"%(str(program.parent),program.name.split(".")[0]))).is_file():
        try:
            st=time.time()
            subprocess.check_call(["%s/%s"%(str(program.parent),program.name.split(".")[0]),"sample","num_samples=1000",
                               "data","file=%s/%s.data.R"%(str(program.parent),program.name.split(".")[0]),"output",
                               "file=%s.csv"%(program.name.split(".")[0])],timeout=600,stdout=subprocess.DEVNULL,
                                         stderr=subprocess.STDOUT)
            rt=time.time()-st
        except subprocess.CalledProcessError as meme:
            mem=True
        except subprocess.TimeoutExpired as toe:
            to=True
    else:
        try:
            st=time.time()
            subprocess.check_call(["%s/%s"%(str(program.parent),program.name.split(".")[0]),"sample","num_samples=1000",
                               "data","output", "file=%s.csv"%(program.name.split(".")[0])],timeout=exp_timeout,stdout=subprocess.DEVNULL,
                                         stderr=subprocess.STDOUT)
            rt=time.time()-st
        except subprocess.CalledProcessError as meme:
            mem=True
        except subprocess.TimeoutExpired as toe:
            to=True
    
    subprocess.check_call(["../tools/cmdstan-2.32.0/bin/stansummary","%s.csv"%(program.name.split(".")[0]),"-c",
                           "%s_out.csv"%(program.name.split(".")[0])])
    
    data=np.loadtxt("%s_out.csv"%(program.name.split(".")[0]),delimiter=",",skiprows=1,dtype=str)
    os.remove("%s.csv"%(program.name.split(".")[0]))
    os.remove("%s_out.csv"%(program.name.split(".")[0]))
    
    res=None
    vtgt=tvars[1].strip().lower()
    for r in data:
        v=r[0].strip().lower()
        if(v==vtgt):
            value=float(r[1])
            break
    return [rt,value,mem,to]

def Table3():
    tvars_soga=np.loadtxt("target_vars_T3.txt",dtype=str,delimiter=",")
    tvars_stan=np.loadtxt("STAN variables.txt",dtype=str,delimiter=",")
    tvars_aqua=np.loadtxt("AQUA variables.txt",dtype=str,delimiter=",")
    tvars_psi=np.loadtxt("PSI variables.txt",dtype=str,delimiter=",")
    
    sogaPrograms=getT3SOGAPrograms("Table3_sogaprograms.txt")
    stanPrograms=getT3STANPrograms("Table3_stanprograms.txt")
    psiPrograms=getT3PSIPrograms("Table3_psiprograms.txt")
    aquaPrograms=getT3AQUAPrograms("Table3_aquaprograms.txt")
    
    tableres={}

    print("####################running SOGA#####################")
    for p in sogaPrograms:
        for idx,var in enumerate(tvars_soga[:,0]):
            if(var.lower()==p.name.split(".")[0]):
                break
        tableres["soga_%s"%(p.name.split(".")[0].replace("Prune","").lower())]=runSOGA(p,tvars_soga[idx,:])
    print("####################running STAN#####################")
    for p in stanPrograms:
        for idx,var in enumerate(tvars_stan[:,0]):
            if(var.lower()==p.name.split(".")[0]):
                break
        tableres["stan_%s"%(p.name.split(".")[0].lower())]=runSTAN(p,tvars_stan[idx,:])
    print("####################running AQUA#####################")
    for p in aquaPrograms:
        for idx,var in enumerate(tvars_aqua[:,0]):
            if(var.lower()==p.name.split(".")[0]):
                break
        tableres["aqua_%s"%(p.name.split(".")[0].lower())]=runAQUA(p,tvars_aqua[idx,:])
    print("####################running PSI#####################")
    for p in psiPrograms:
        for idx,var in enumerate(tvars_aqua[:,0]):
            if(var.lower()==p.name.split(".")[0]):
                break
        tableres["psi_%s"%(p.name.split(".")[0].lower())]=runPSI(p,tvars_psi[idx,:])
         
    
    print(tableres)
    
            

if __name__ == '__main__':
    Table3()