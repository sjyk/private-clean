#!/usr/bin/env python

import numpy
import math


"""
(estimate, nominal, actual, ci)
"""

"""
COUNT(distinct)
"""
def distinct_count(dataset):
	est = len(set(dataset[1][0]))
	actual = len(set(dataset[0][0]))
	return (est,est,actual, None)


"""
Count
"""
def countq(dataset,predicate,p,a=0.95):
	actual_pred_set = []
	private_pred_set = []

	for i in range(0,len(dataset[0][0])):
		if dataset[0][0][i] in predicate:
			actual_pred_set.append(i)

		if dataset[1][0][i] in predicate:
			private_pred_set.append(i)

	#Calculate Estimate
	N = distinct_count(dataset)[2]+0.0
	l = len(predicate)+0.0
	Cpred = len(private_pred_set)+0.0
	Ctrue = len(actual_pred_set)+0.0
	S = len(dataset[0][0])

	#print N,l, Cpred/(1-p) - S*p*l/(N*(1-p)), Ctrue, Cpred

	#handle edge cases
	if p <= 1e-3:
		est = Cpred
	elif p >= 0.999:
		est = l/N*S
	else:
		est = max(Cpred/(1-p) - S*p*l/(N*(1-p)), 1)

	#print p,Cpred,Ctrue,est,est-Ctrue, Cpred-Ctrue

	#est = Cpred - (S-Cpred)*(p*l/N) + Cpred*(p*(N-l)/N)
	#P(true in private) = [(1-p)+pl/N]*P(true) + [pl/N]*[1-P(true)]
	#Cpred/(S*(1-p)) - pl/(N*(1-p))= P(true)
	#est = Ctrue - (S-Ctrue)*(p*l/N) + Ctrue*(p*(N-l)/N)

	#print est, Cpred, Ctrue, Cpred - (S-Ctrue)*(p*l/N) + Ctrue*(p*(N-l)/N)

	ci = 0#(1.0/(1.0-p))*math.sqrt(len(dataset[0][0])/2.0 * math.log(1/(1-a)))
	
	return (est, Cpred, Ctrue, ci)

"""
SUM
"""
def sumq(dataset,predicate,p,b,a=0.95):
	actual_pred_set = []
	actual_npred_set = []

	private_pred_set = []
	private_npred_set = []

	for i in range(0,len(dataset[0][0])):
		if dataset[0][0][i] in predicate:
			actual_pred_set.append(dataset[0][1][i])
		else:
			actual_npred_set.append(dataset[0][1][i])

		if dataset[1][0][i] in predicate:
			private_pred_set.append(dataset[1][1][i])
		else:
			private_npred_set.append(dataset[1][1][i])


	#Calculate estimate
	S = len(dataset[0][0])
	N = distinct_count(dataset)[2]
	l = (len(predicate)+0.0)

	Hpred = numpy.sum(private_pred_set)
	Htrue = numpy.sum(actual_pred_set)
	Cpred = len(private_pred_set)+0.0
	Ctrue = len(actual_pred_set)+0.0

	h = numpy.mean(private_pred_set)
	hc = numpy.mean(private_npred_set)

	est = Hpred - (S-Cpred)*(hc*p*l/N) + Cpred*h*(p*(N-l)/N)

	#handle edge case
	if est <= 0:
		est = Hpred

	#print est, Hpred, Htrue

	ci = 0#(b/((1.0-p)*N))*(math.sqrt(2.0*S * math.log(1/(1-a))) + math.log(1/(1-a)))
	
	return (est, Hpred, Htrue, ci)

def avgq(dataset,predicate,p,b,a=0.95):
	res1 = sumq(dataset,predicate,p,b,a)
	res2 = countq(dataset,predicate,p,a)

	#handles poor conditioning
	est = res1[0]/res2[0]
	if res2[0] < 5:
		est = res1[0]/res2[1]

	#print est, res1[2]/res2[2], res1[1]/res2[1]

	return (est,res1[1]/res2[1],res1[2]/res2[2],0)