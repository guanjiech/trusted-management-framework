## Overview
This repository implements the protocol proposed in "A Blockchain-Based Trusted Management Framework for IoT Collaboration" and contains the Kademlia-based storage scheme and the HLPSL file that is used to verify the security of the designed authentication scheme via AVISPA. 
## Kademlia
### Description
Kademlia is utilized to build a distributed storage network among edge servers in this work. 
### How to use
See kademlia/README.md

## AVISPA
### Setup
We select OFMC and CL-AtSe backends for simulation since the bitwise XOR operations are not supported in SATMC and TA4SP backends. The returned result is "SAFE".

## Others
Note that we refer to [this link](https://blog.csdn.net/shuiyixin/article/details/104490091) for the installation and usage of the CP-ABE library.
