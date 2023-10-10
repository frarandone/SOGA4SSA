# SOGA

## Contents

- The folder "experiments" contains the scripts and data to reproduce the main results of of the paper (i.e., Table 3).
- The folder "grammars" contains the file with the grammar of SOGA (SOGA.g4) and the two sub-grammars ASGMT (ASGMT.g4) and TRUNC (TRUNC.g4).
- The folder "programs" contains the scripts of the models analyzed in the paper, divided by tools.
- The folder "src" contains the code implementing the tool SOGA, whose usage is described below;
- The folder "tools" contains the implementation of the tools AQUA, BLOG, cmdstan and PSI, to which SOGA is compared.

## Reproducibilty

- Create and start a new docker container based on the following steps:

docker container create -i -t --name SOGA bistrulli/soga:0.1
docker start SOGA

- then enter the container 

docker attach SOGA

- for reproduing Table 3 issue the following command

cd /root/SOGA/experimemts
python3 reproduce.py

- after executing this command the Table will be saved in /root/SOGA/experimemts/results/Table3.csv with the same structure of the Table 3 of the paper   

## Comparison with PSI

- Considering that for calculating the symbolic formulas derived with PSI, we used the proprietary tool https://www.wolfram.com/mathematica/, 
  we can't distribute it within this replication package. To allow the replication of the results, we save each PSI  formula in the folder 
  "/root/SOGA/experiments/results/psi_formula" so that these can then be executed once a license for the tool has been obtained.

## Implementation

The module producecfg.py contains the classes definition for CFG objects and the function produce_cfg, that extracts a CFG from a program script in a .txt file. 

The module libSOGA.py contains the function start_soga, which is used to invoke SOGA on a CFG object and the recursive function SOGA, which, depending on the type of the visited node, calls the functions needed to update the current distribution. 

Such functions are contained in the auxiliary modules:
- libSOGAtruncate.py, containing functions for computing the resulting distribution when a truncation occurs (in conditional or observe instructions);
- libSOGAupdate.py, containing functions for computing the resulting distribution after applying an assignment instruction;
- libSOGAmerge,py, containing functions for computing the resulting distribution when a merge or a prune instruction is encountered;

Additional functions for general purpose are defined in the module libSOGAshared.py, which is imported by all previous libraries.

Parsing of the scripts, expressions and truncations is performed using ANTLR. Definition of the respective grammars can be found in the files SOGA.g4, ASGMT.g4 and TRUNC.g4.
