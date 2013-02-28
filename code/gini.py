#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
import csv
import json
from collections import defaultdict

(cmte_id, cand_id, cand_nm, contbr_nm, contbr_city, contbr_st, contbr_zip,
contbr_employer, contbr_occupation, contb_receipt_amt, contb_receipt_dt,
receipt_desc, memo_cd, memo_text, form_tp, file_num, tran_id, election_tp) = range(18)


############### Set up variables
# TODO: declare datastructures

cNames = defaultdict(int)
zCodes = defaultdict(int)
counter = 0.0


############### Read through files
for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        ###
        # TODO: replace line below with steps to save information to calculate
        # Gini Index
        row[cand_nm], row[contbr_zip]
        ##/

	candidateId=str(row[2])
	zipCode=str(row[6])
	counter+=1
	cNames[candidateId]+=1
	zCodes[zipCode]+=1	

###
# TODO: calculate the values below:
gini = 1-sum((cNames[c]/counter)**2 for c in cNames)  # current Gini Index using candidate name as the class
zip_gini= 1-sum((zCodes[z]/counter)**2 for z in zCodes)
split_gini = sum((cNames[c]/counter)*(1-(cNames[c]/counter)**2)*zip_gini for c in cNames) # weighted average of the Gini Indexes using candidate names, split up by zip code
##/
print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini
