#!/usr/bin/python3

# Matt Lewis, NCC Group 2020
#
# this script processes rfc json files in terms of which ones
# obsolete or update others, then generates repsective
# neo4j cypher files to be imported into neo4j for querying
# and graph display

from os import listdir
import json

def clean(s):
    r = s.encode('ascii','ignore').replace(',','').replace('\"','')
    return r.replace('\r','').replace('\'','').replace('\n',' ').strip()

rfc_folder = '.'

rfcs = (f for f in listdir(rfc_folder) if f.endswith('.json'))

standalone_file = open('standalone.csv','w')
obsoleted_by_file = open('obsoleted_by.csv','w')
obsoletes_file = open('obsoletes.csv','w')
updated_by_file = open('updated_by.csv','w')
updates_file = open('updates.csv','w')

standalone_file.write('rfc,title\n')
obsoleted_by_file.write('rfc,title,obsoletedby\n')
obsoletes_file.write('rfc,title,obsoletes\n')
updated_by_file.write('rfc,title,updatedby\n')
updates_file.write('rfc,title,updates\n')

for rfc in rfcs:
    with open(rfc,'r') as handle:
        parsed = json.load(handle)

        rfcID = parsed["doc_id"].replace(' ','')
        title = clean(parsed["title"])
        pub_status = parsed["pub_status"]
        status = parsed["status"]
        pub_date = parsed["pub_date"]
        obsoleted_by = parsed["obsoleted_by"]
        obsoletes = parsed["obsoletes"]
        updated_by = parsed["updated_by"]
        updates = parsed["updates"]

        # write an entry for each RFC parsed
        standalone_file.writelines('{},{},\n'.format(rfcID, title))

        if(obsoleted_by):
            for o in obsoleted_by:
                obsoleted_by_file.write('{},{},{}\n'.format(rfcID, title, o.strip()))
                
        if(obsoletes):
            for o in obsoletes:
                obsoletes_file.write('{},{},{}\n'.format(rfcID, title, o.strip()))

        if(updated_by):
            for u in updated_by:
                updated_by_file.write('{},{},{}\n'.format(rfcID, title, u.strip()))

        if(updates):
            for u in updates:
                updates_file.write('{},{},{}\n'.format(rfcID, title, u.strip()))

standalone_file.close()
obsoleted_by_file.close()
obsoletes_file.close()
updated_by_file.close()
updates_file.close()


