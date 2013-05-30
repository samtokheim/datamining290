#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
import csv
import json
from collections import defaultdict,Counter

(cmte_id, cand_id, cand_nm, contbr_nm, contbr_city, contbr_st, contbr_zip,
contbr_employer, contbr_occupation, contb_receipt_amt, contb_receipt_dt,
receipt_desc, memo_cd, memo_text, form_tp, file_num, tran_id, election_tp) = range(18)


############### Set up variables
# TODO: declare datastructures

cNames = defaultdict(int)
candy = defaultdict(lambda: defaultdict(int))
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
	candy[zipCode][candidateId]+=1

split_gini_list = []
for z in candy:
	#Get the total number of donations for a zip code
	zip_donations = float(sum(candy[z][c] for c in candy[z]))
	
	#Instantiate new list to store individual candidate gini scores per zipcode
	#Calculate the gini score for each candidate/zipcode
	candidates_zip_gini=[]
	for c in candy[z]:
		c_gini = (candy[z][c]/zip_donations)**2
		candidates_zip_gini.append(c_gini)
	#Take the gini score for a zip code and weight by dividing its donations by all the donations
	weighted_score = (1-sum(candidates_zip_gini))*(zip_donations/counter)
	
	#Add this to a list so these weighted zip Gini scores can be summed into an average
	split_gini_list.append(weighted_score)

###
# TODO: calculate the values below:
gini = 1-sum((cNames[c]/counter)**2 for c in cNames)  # current Gini Index using candidate name as the class
split_gini = sum(split_gini_list) # weighted average of the Gini Indexes using candidate names, split up by zip code

##/
print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini
