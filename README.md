## Overview
This repository implements the protocol proposed in "A Blockchain-Based Trusted Management Framework for IoT Collaboration" and contains the Kademlia-based storage scheme and the HLPSL file that is used to verify the security of the designed authentication scheme via AVISPA. 
## Kademlia
### Dependencies
- Fabric v2.4.6
- Caliper v0.5.0
### How to use
See fabric/scripts/fabric-samples/test-network/how-to-use.txt.

I modified the scripts to support flexible orgs-adding feature, the entry is in mynetwork.sh, so remember to use mynetwork.sh instead of network.sh.

Also, I provide a bash script auto-test.sh to easily execute the whole test workflow.

## AVISPA
### Setup
We select OFMC and CL-AtSe backends for simulation since the bitwise XOR operations are not supported in SATMC and TA4SP backends. The result is "SAFE".

## Others
Note that we refer to [this link](https://blog.csdn.net/shuiyixin/article/details/104490091) for the installation and usage of the CP-ABE library.
