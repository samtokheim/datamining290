#!/usr/bin/python
"""This script can be used to analyze data in the 2012 Presidential Campaign,
available from http://www.fec.gov/disclosurep/PDownload.do"""

import fileinput
import csv
import math

total = 0
values = []
candidates = {}

for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
	value = float(row[9])
	total += value
	candidateId = str(row[1])
	candidate = str(row[2])	
	
	if candidateId not in candidates:
		candidates[candidateId] = candidate
	
        ###
        # TODO: calculate other statistics here
        # You may need to store numbers in an array to access them together
        ##/
	values.append(value)

###
# TODO: aggregate any stored numbers here
#
##/
mean = total/len(values)
median = sorted(values)[len(values)/2]
minVal = min(values)
maxVal = max(values)

def sd(values,mean):
	size = len(values)

	#Find deviation from mean for each value and square it
	squaresOfDev = [(v-mean)**2 for v in values]
	
	#Sum the squared deviation of each value
	sumOfDev = 0.0
	for v in squaresOfDev:
		sumOfDev += v

	#Divide the sum of squared deviations by one less than the total count of values. Then find the square root.
	stdDev = (sumOfDev/size)**0.5
	
	return stdDev

def printCandidates(candidates):
	
	cList =[]
		
	#Split into first and last names. Reverse the order of first and last names. Remove commas. Add to list.	
	for key in candidates:
		
		c = candidates[key].split()
		cString = c[1]+" "+c[0]
		cString = cString.replace(',','')
		cList.append(cString)
	
	#Sort the list and then create a comma separated string from the list
	cList = sorted(cList)
	candidatesList = ", ".join(cList)

	return candidatesList
	
##### Print out the stats
print "Total: %s" % total
print "Minimum: %s " %  minVal
print "Maximum: %s" % maxVal
print "Mean: %s" % str(mean)
print "Median: %s" % str(median) 
# square root can be calculated with N**0.5
print "Standard Deviation: %s" % str(sd(values,mean))

##### Comma separated list of unique candidate names
print "Candidates: %s" % printCandidates(candidates)

def minmax_normalize(value):
    """Takes a donation amount and returns a normalized value between 0-1. The
    normilzation should use the min and max amounts from the full dataset"""
    ###
    # TODO: replace line below with the actual calculations
    norm = ((value-minVal)/(maxVal-minVal))*(1-0)+0

    ###/
    
    return norm

##### Normalize some sample values
print "Min-max normalized values: %r" % map(minmax_normalize, [2500, 50, 250, 35, 8, 100, 19])

