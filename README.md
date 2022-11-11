## Overview
This repository implements the protocol proposed in "A Blockchain-Based Trusted Management Framework for IoT Collaboration" and contains the Kademlia-based storage scheme and the HLPSL file that is used to verify the security of the designed authentication scheme via AVISPA. 
## Kademlia
### Description
Kademlia is utilized to build a distributed storage network among edge servers in this work. 
### How to use
See kademlia/README.md

## CP-ABE
### Description
Attribute-based Encryption (ABE) is a scheme of using attributes to encrypt the content. It makes sure that only users with the corresponding private keys of the attributes can decrypt the content. Generally, CP-ABE is the scheme that ciphertext is encrypted with an access structure (MSP), and each user is given a set of attributes. KP-ABE is the opposite: ciphertexts are "tagged" (encrypted) with a set of attributes, and each user is given an access structure. Both scheme can provide fine-grain user access control in different scenarios.

This project is based on Shashank Agrawal and Melissa Chase's paper [1], and it is the CP-ABE variant mentioned in their paper. The source code in this project also follows their corresponding Charm project [2].

[1] S. Agrawal and M. Chase, “FAME: Fast attribute-based message encryption,” Proc. ACM Conf. Comput. Commun. Secur., pp. 665–682, 2017. https://eprint.iacr.org/2017/807.pdf

[2] "Attribute-based Encryption". https://github.com/sagrawal87/ABE
## AVISPA
### Setup
We select OFMC and CL-AtSe backends for simulation since the bitwise XOR operations are not supported in SATMC and TA4SP backends. The returned result is "SAFE".

## Others
Note that we refer to [this link](https://blog.csdn.net/shuiyixin/article/details/104490091) for the installation and usage of the CP-ABE library.
