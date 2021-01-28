# RFC-Security-Research
Original paper and helper scripts to help analyse security aspects of Internet RFCs.

## Overview 
This repository hosts a review of RFC security (written in the syle of an RFC), in addition to various python helper scripts that were 
used to obtain the data necessary for the underlying analysis, and for generating the necessary Cypher (neo4j graph database) code to support
graph database analysis of the RFC corpus.

## Creating the Graph Database

The scripts in this repo are merely quick scripts that extract the info needed for the whitepaper, and which put them in a CSV format that can be used for import into a neo4j (in this instance) graph database. The scripts are in no way exhaustive in terms of the data extracted and so they serve as examples/templates only.

## Example

To extract the email and obsolescence relationships across RFCs, run the following scripts across the RFC corpus, which will generate CSV files of the relationships:

https://github.com/m4ttl/RFC-Security-Research/blob/main/RFC%20Email%20Processing/email-Cypher.py
https://github.com/m4ttl/RFC-Security-Research/blob/main/RFC%20Precedent%20Processing/parsejsoncypher.py

Then import the CSV files into neo4j such as:

```LOAD CSV WITH HEADERS FROM 'file:///blah.csv' AS csvLine
MERGE (rfc:RFC {name: csvLine.rfc})
MERGE (email:Email {name: csvLine.email})
CREATE (email)-[:CONTRIBUTED_TO]->(rfc)
```

For the obsolescence relationships, import those into neo4j such as:

```CREATE INDEX ON :RFC(name)

LOAD CSV WITH HEADERS FROM 'file:///standalone.csv' AS csvLine
MERGE (rfc:RFC {name: csvLine.rfc, title: csvLine.title})

LOAD CSV WITH HEADERS FROM 'file:///updated_by.csv' AS csvLine
MERGE (rfc:RFC {name: csvLine.rfc, title: csvLine.title})
MERGE (updaterfc:Updaterfc {name: csvLine.updatedby})
CREATE (rfc)-[:UPDATED_BY]->(updaterfc)

LOAD CSV WITH HEADERS FROM 'file:///updates.csv' AS csvLine
MERGE (rfc:RFC {name: csvLine.rfc, title: csvLine.title})
MERGE (updatesrfc:Updatesrfc {name: csvLine.updates})
CREATE (rfc)-[:UPDATES]->(updatesrfc)

LOAD CSV WITH HEADERS FROM 'file:///obsoleted_by.csv' AS csvLine
MERGE (rfc:RFC {name: csvLine.rfc, title: csvLine.title})
MERGE (obsoletedbyrfc:Obsoletedbyrfc {name: csvLine.obsoletedby})
CREATE (rfc)-[:OBSOLETED_BY]->(obsoletedbyrfc)

LOAD CSV WITH HEADERS FROM 'file:///obsoletes.csv' AS csvLine
MERGE (rfc:RFC {name: csvLine.rfc, title: csvLine.title})
MERGE (obsoletesrfc:Obsoletesrfc {name: csvLine.obsoletes})
CREATE (rfc)-[:OBSOLETES]->(obsoletesrfc)
```

One can then use the various queries as documented in the whitepaper to query the necessary information and to create the desired connected graphs of relationships.

Related summary blog post: https://research.nccgroup.com/?p=6870
