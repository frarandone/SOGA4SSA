# SOGA

## Contents

- The folder "experiments" contains the code implementing the tool SOGA, whose usage is described below;
- The folder "script" contains the scripts of the benchmarks used in the paper "Inference of Probabilistic Programs with Moment-Matching Gaussian Mixtures";
- The folder "tools" contains the scripts of the same benchmarks in format readable by the tools STAN, PSI, AQUA, and BLOG to which SOGA was compared.

In addition, in the folder "python", we include a Jupyter Notebook called "Timing", in which the experiments performed in the paper are already set up for replicability.

## Reproducibilty

- Download the folder.

- From SOGA\python invoke *python3 SOGA.py -f filename* to apply SOGA to the script SOGA\script\filename.txt or *python3 SOGA.py* to print an help message.


## Implementation

The module producecfg.py contains the classes definition for CFG objects and the function produce_cfg, that extracts a CFG from a program script in a .txt file. 

The module libSOGA.py contains the function start_soga, which is used to invoke SOGA on a CFG object and the recursive function SOGA, which, depending on the type of the visited node, calls the functions needed to update the current distribution. 

Such functions are contained in the auxiliary modules:
- libSOGAtruncate.py, containing functions for computing the resulting distribution when a truncation occurs (in conditional or observe instructions);
- libSOGAupdate.py, containing functions for computing the resulting distribution after applying an assignment instruction;
- libSOGAmerge,py, containing functions for computing the resulting distribution when a merge or a prune instruction is encountered;

Additional functions for general purpose are defined in the module libSOGAshared.py, which is imported by all previous libraries.

Parsing of the scripts, expressions and truncations is performed using ANTLR. Definition of the respective grammars can be found in the files SOGA.g4, ASGMT.g4 and TRUNC.g4.