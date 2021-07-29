# IoT---Provisioning-Dynamic-Security

For our simulator we shortlisted 5 network security protocols:

* Ascon 
* Trivium 
* PRESENT
* NtruEncrypt

## NtruEncrypt
The implementation for NtruEncrypt can be found here: https://github.com/tbuktu/ntru 

Follow the instructions in the ReadMe to run and test the protocols. 

## Ascon 

We have two implementations of Ascon, one in Python (pyascon-master) and the other in Java (javaascon-master). The python implementation folder contains a ReadMe with all the neccessary information about the protocol and different files within the folder. The file **ascontest.py** is where we created our testing code for encryption/decryption speeds. 

We did not create tests for the java implementation. The java version of the protocol is not as advanced, nor is it optimized, thus it only has two modes of operation: Ascon-128 and Ascon-128a. 

This protocol was designed by a team of cryptographers from Graz University of Technology, Infineon Technologies, and Radboud University: Christoph Dobraunig, Maria Eichlseder, Florian Mendel, and Martin Schläffer.

## Trivium & PRESENT

The implementation for Trivium can be found here: https://github.com/johnny-pan/trivium

The implementation for PRESENT can be found here: https://github.com/xSAVIKx/PRESENT-cipher 

We had to edit both protocols to make them python3 compatible. The implementations can be found in the **prestrivtest** folder. File **test.py** contains the testing code we created for encryption/decryption speeds for both protocols. 
