#Calculates initial output layer error
def outputError(n):
	err = n*(1.0-n)*(0.0-n)
	return(err)

#Calculates hidden layer errors
def hiddenError(n,err,w):
	err = n*(1-n)*(err*w)
	return(err)

#Calculates the new weight
def nw(w,learn_rate,err,n):
	nw = w+(learn_rate*err*n)
	return(nw)

#This is the constant for learning rate
learn_rate = 10

#Initial input values
n1 = 1	
n2 = 2

#Hidden layer values represents the sigmoid of sum(inputs*weight)
n3 = 0.7311
n4 = 0.0179
n5 = 0.9933

#Output layer
n6 = 0.8387

#Initial weights
w_13 = -3.0
w_14 = 2.0
w_15 = 4.0
w_23 = 2.0
w_24 = -3.0
w_25 = 0.5
w_36 = 0.2
w_46 = 0.7
w_56 = 1.5

#Error for output layer
err_6 = outputError(n6)

#Errors for hidden layer
err_5 = hiddenError(n5,err_6,w_56)
err_4 = hiddenError(n4,err_6,w_46)
err_3 = hiddenError(n3,err_6,w_36)

#Errors for input layer
err_2 = 0.0 #hiddenError(n2,err_5,w_25)
err_1 = 0.0 #hiddenError(n1,err_3,w_13)

#New weights
nw_13 = nw(w_13,learn_rate,err_3,n1)
nw_14 = nw(w_14,learn_rate,err_4,n1)
nw_15 = nw(w_15,learn_rate,err_5,n1)
nw_23 = nw(w_23,learn_rate,err_3,n2)
nw_24 = nw(w_24,learn_rate,err_4,n2)
nw_25 = nw(w_25,learn_rate,err_5,n2)
nw_36 = nw(w_36,learn_rate,err_6,n3)
nw_46 = nw(w_46,learn_rate,err_6,n4)
nw_56 = nw(w_56,learn_rate,err_6,n5)

#Output errors
print "err_1: %s" % err_1
print "err_2: %s" % err_2
print "err_3: %s" % err_3
print "err_4: %s" % err_4
print "err_5: %s" % err_5
print "err_6: %s" % err_6

#Output new weights
print "w_13: %s" % nw_13
print "w_14: %s" % nw_14
print "w_15: %s" % nw_15
print "w_23: %s" % nw_23
print "w_24: %s" % nw_24
print "w_25: %s" % nw_25
print "w_36: %s" % nw_36
print "w_46: %s" % nw_46
print "w_56: %s" % nw_56
