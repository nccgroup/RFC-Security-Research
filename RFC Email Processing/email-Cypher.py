#!/usr/bin/python3

# Matt Lewis, NCC Group 2020
#
# iterates over corpus of RFC text and extracts
# email addresses of contributors etc.
# RFC corpus can be obtained here: https://www.rfc-editor.org/retrieve/bulk/

from os import listdir
import re  

rfc_folder = '.'
email_addresses = {}

rfcs = (f for f in listdir(rfc_folder) if f.endswith('.txt'))
for rfc in rfcs:

    f = open(rfc, 'r')
   
    rfcid = rfc.replace('.txt','')
    for line in f:
        e = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", line)
        for i in e:
            if ('example' not in i):
                if (i not in email_addresses):
                    email_addresses[i] = []
                    email_addresses[i].append(rfcid)
                else:
                    if rfcid not in email_addresses[i]:
                        email_addresses[i].append(rfcid)

    f.close()

for (key, val) in email_addresses.items():  

    for edge in val:
        print('{},{}'.format(key, edge))

