#!/usr/bin/python3

# Matt Lewis, NCC Group 2020
#
# process RFCs in terms of requirements level keywords - i.e.
# get some stats on their usage

from os import listdir

# dirty hack using replacement words to avoid miscounting; e.g.
# where 'MUST' and 'MUST NOT' are different yet MUST would be counted twice
# REPL1 = MUST NOT, REPL2 = SHALL NOT, REPL3 = SHOULD NOT, REPL4 = NOT RECOMMENDED

KEYWORDS = ['MUST','REQUIRED','SHALL','REPL1','REPL2','SHOULD','RECOMMENDED','REPL3','REPL4','MAY','OPTIONAL']

def getWordCounts(rfc_text):
    counts = {}

    for w in KEYWORDS:

        counts[w] = rfc_text.count(w)

    return counts

# RFCs are in this folder, download the latest archive from: https://www.rfc-editor.org/retrieve/bulk/
rfc_folder = '.'

rfcs = (f for f in listdir(rfc_folder) if f.endswith('.txt'))
for rfc in rfcs:
    f = open(rfc, 'r')
    rfc_text = f.read()

    c = getWordCounts(rfc_text)
    
    vals = ''
    for (key, val) in c.items():
        #print(key, val)
        vals += ',' + str(val)

    print('{}{}'.format(rfc.replace('.txt.encoded',''), vals))

