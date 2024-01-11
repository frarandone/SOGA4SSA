# A parser that produce a .soga file from a high-level to low-level syntax
import re
import numpy as np
from sklearn.mixture import GaussianMixture
import tempfile
from functools import partial

nsamples=int(10**7)

computedDist={}

def extractMatch(input_prog,regex):
    matches = re.finditer(regex, input_prog, re.MULTILINE)
    inMatches=[]
    oText=[]
    for matchNum, match in enumerate(matches, start=1):
        #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        oText+=[input_prog[match.start():match.end()]]
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            inMatches+=[match.group(groupNum)]
    return inMatches,oText

def genSample(dist):
    X=dist()
    print(np.mean(X))
    return X

def compileUniform(input_prog):
    global computedDist
    #uniform([low,high], ncmp)
    matches,oText=extractMatch(input_prog,regex = r"uniform\((.*?)\)")
    for idx,m in enumerate(matches):
        if(f"uniform({m})" not in computedDist):
            res=re.split(r"(?<=\])\s*,",m)
            
            low=float(res[0].split(",")[0].replace("[","").strip())
            high=float(res[0].split(",")[1].replace("]","").strip())
            ncmp=int(res[1].strip())

            X=genSample(partial(np.random.uniform,low, high,nsamples)).reshape(-1, 1)
            weights,means,covariances=fitGmm(X,ncmp)

            input_prog=input_prog.replace(oText[idx],
                     "gm([%s],[%s],[%s])"%(",".join(map(str,weights.tolist())),",".join(map(str,means.T.tolist()[0])),
                     ",".join(map(str,(np.sqrt(covariances).reshape(-1,1).T.tolist()[0])))))

            computedDist[f"uniform({m})"]=[weights,means,covariances]
        else:
            print("all done")
            # weights=computedDist[f"uniform({m})"][0]
            # means=computedDist[f"uniform({m})"][1]
            # covariances=computedDist[f"uniform({m})"][2]

            # input_prog=input_prog.replace(oText[idx],
            #          "gm([%s],[%s],[%s])"%(",".join(map(str,weights.tolist())),",".join(map(str,means.T.tolist()[0])),
            #          ",".join(map(str,(np.sqrt(covariances).reshape(-1,1).T.tolist()[0])))))



    return input_prog

def compileBeta(input_prog):
    #beta([a,b], ncmp)
    matches,oText=extractMatch(input_prog,regex = r"beta\((.*?)\)")
    for idx,m in enumerate(matches):
        res=re.split(r"(?<=\])\s*,",m)
        a=float(res[0].split(",")[0].replace("[","").strip())
        b=float(res[0].split(",")[1].replace("]","").strip())
        ncmp=int(res[1].strip())

        X=np.random.beta(a, b,size=nsamples).reshape(-1, 1)
        weights,means,covariances=fitGmm(X,ncmp)

        input_prog=input_prog.replace(oText[idx],
             "gm([%s],[%s],[%s])"%(",".join(map(str,weights.tolist())),",".join(map(str,means.T.tolist()[0])),
             ",".join(map(str,(np.sqrt(covariances).reshape(-1,1).T.tolist()[0])))))

    return input_prog

def compileExpRnd(input_prog):
    #exprnd(scale,ncmp)
    matches,oText=extractMatch(input_prog,regex = r"exprnd\((.*?)\)")
    for idx,m in enumerate(matches):
        X=np.random.exponential(float(m.split(",")[0].strip()),nsamples).reshape(-1, 1)
        weights,means,covariances=fitGmm(X,int(m.split(",")[1].strip()))

        input_prog=input_prog.replace(oText[idx],
            "gm([%s],[%s],[%s])"%(",".join(map(str,weights.tolist())),",".join(map(str,means.T.tolist()[0])),
            ",".join(map(str,(np.sqrt(covariances).reshape(-1,1).T.tolist()[0])))))
    
    return input_prog

def compileBernoulli(input_prog):
    #bern(p)
    matches,oText=extractMatch(input_prog,regex = r"bern\((.*?)\)")
    for idx,m in enumerate(matches):
        p=float(m.split(",")[0].strip())
        input_prog=input_prog.replace(oText[idx],
            "gm([%f,%f],[0.0,1.0],[0.0,0.0])"%(1-p,p,))
    
    return input_prog

def compileGauss(input_prog):
    #gauss(mean,std)
    matches,oText=extractMatch(input_prog,regex = r"gauss\((.*?)\)")
    for idx,m in enumerate(matches):
        mean=float(m.split(",")[0].strip())
        std=float(m.split(",")[1].strip())

        input_prog=input_prog.replace(oText[idx],
            "gm([1.0],[%f],[%f])"%(mean,std))
    
    return input_prog


def fitGmm(X=None,ncomp=2):
    gmm = GaussianMixture(n_components=ncomp,max_iter=100,n_init=10,init_params="k-means++",
        reg_covar=0,tol=1e-5)
    gmm.fit(X)

    # Access parameters
    means = gmm.means_
    weights = gmm.weights_
    covariances = gmm.covariances_

    return weights,means,covariances


def compile2SOGA(input_prog):
    progr=compileExpRnd(input_prog=input_prog)
    progr=compileUniform(input_prog=progr)
    progr=compileBeta(input_prog=progr)

    progr=compileGauss(input_prog=progr)
    progr=compileBernoulli(input_prog=progr)

    print(progr)

    temp_file=tempfile.NamedTemporaryFile(mode='w',delete=False)
    temp_file.write(progr)
    temp_file.close()

    return temp_file.name