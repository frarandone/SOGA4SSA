import numpy as np
import scipy
import argparse
import glob
from pathlib import Path
import subprocess
import re
from numpy import dtype


def getT3SOGAPrograms(programList):
    pfile=open(programList,"r")
    analyzed_programs=pfile.readlines()
    pfile.close()
    
    analyzed_programsName=[ p.strip().split("[")[0].strip() for p in analyzed_programs]
    
    programs=[]
    allprograms=glob.glob("../**/SOGA/**/*.soga",recursive=True)
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
    allprograms=glob.glob("../**/PSI/**/*.psi",recursive=True)
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
    allprograms=glob.glob("../**/STAN/**/*.stan",recursive=True)
    for p in allprograms:
        if(Path(p.strip()).name.split(".")[0].strip().lower() in analyzed_programsName ):
            programs.append(Path(p.strip()))
    
    return programs

def getT3AQUAPrograms():
    pass



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
    value_reg=r"E\[%s\]: (\d+.\d+)"%(re.escape(tvars[0,1].replace('"','').strip()))
     
    rt=getMatches(re.finditer(rt_reg, str(out).strip(), re.IGNORECASE));
    c=getMatches(re.finditer(c_reg, str(out).strip(), re.IGNORECASE));
    d=getMatches(re.finditer(d_reg, str(out).strip(), re.IGNORECASE));
    value=getMatches(re.finditer(value_reg, str(out).strip(), re.IGNORECASE));
    
    return [rt,c,d,value]


def runAQUA(program,tvars):
    subprocess.check_output([""])

def runPSI(program,tvars):
    print(program)

def runSTAN(program,tvars):
    pass 

def Table3():
    tvars=np.loadtxt("target_vars_T3.txt",dtype=str,delimiter=",")
    
    sogaPrograms=getT3SOGAPrograms("Table3_sogaprograms.txt")
    psiPrograms=getT3PSIPrograms("Table3_psiprograms.txt")
    stanPrograms=getT3PSIPrograms("Table3_stanprograms.txt")
    aquaPrograms=getT3PSIPrograms("Table3_aquaprograms.txt")
    
    tableres={}

    print("####################running SOGA#####################")
    for p in sogaPrograms:
        res=np.where(tvars[:,0]==(p.name.split(".")[0]))
        tableres["soga_%s"%(p.name.split(".")[0].replace("Prune","").lower())]=runSOGA(p,tvars[res[0],:])
    print(tableres)
    print("####################running PSI#####################")
    for p in psiPrograms:
        #rint(p.name.split(".")[0])
        pass
    print(len(psiPrograms))
    print("####################running STAN#####################")
    print(len(stanPrograms))
    print("####################running AQUA#####################")
    print(len(aquaPrograms))
    
            
            
            
    


if __name__ == '__main__':
    Table3()