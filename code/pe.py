from math import log, exp
from scipy.stats import linregress
import numpy as np
import csv

data = open("price-elasticity.csv", "rb" )
reader = csv.reader(data)
output = open("output.txt","w")

reader.next()
x_list = []
y_list = []
for line in reader:
	x = int(line[1])
	y = float(line[2].strip('$'))	
	x_list.append(x)
	y_list.append(y)

#x = np.random.random(10)
#y = np.random.random(10)

slope, intercept, r_value, p_value, std_err = linregress(y_list, x_list)
print "r-squared: ",r_value**2

data.close()
output.close()
