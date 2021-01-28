#!/usr/bin/python3

# Matt Lewis, NCC Group 2020
#
# iterate over RFC text files and check if Security issues are discussed

from os import listdir
import re  

rfc_folder = '.'

rfcs = (f for f in listdir(rfc_folder) if f.endswith('.txt'))
for rfc in rfcs:

    f = open(rfc, 'r')
    
    secon = False
    notdisc = False

    for line in f:
        if "Security Considerations" in line:
            secon = True
        if "Security issues are not discussed in this memo" in line:
            notdisc = True

    if(secon and not notdisc):
        print(rfc)
