
from generate_dataset import generate
from query import distinct_count, countq, sumq, avgq
import numpy
import math

def run_T_trials(trials=100,
				 size=1000,
				 cprivacy=0.1,
				 nprivacy=1,
				 distinct=10,
				 selectivity=0.5,
				 errorrate=0.21,
				 cskew=0.33,
				 nskew=0.33):

	sumr = []
	countr = []
	avgr = []

	for t in range(0,trials):
		#print "Running Trial ", t
		dataset = generate(S=size,p=cprivacy,b=nprivacy,N=distinct,z1=cskew,z2=nskew)
		truepred = range(int(round((1-selectivity)*distinct)),distinct)#numpy.random.choice(range(0,distinct),size=int(round(selectivity*distinct)),replace=False)
		corruptpred = []

		if int(round(errorrate*distinct)) >= 1: 
			corruptpred = numpy.random.choice(range(0,distinct),size=int(round(errorrate*distinct)),replace=False)

		corruptpred = list(set(truepred).union(set(corruptpred)))

		sum_cresult = sumq(dataset, predicate=truepred,p=cprivacy,b=nprivacy)
		count_cresult = countq(dataset, predicate=truepred,p=cprivacy)
		avg_cresult = avgq(dataset, predicate=truepred,p=cprivacy,b=nprivacy)

		sum_dresult = sumq(dataset, predicate=corruptpred,p=cprivacy,b=nprivacy)
		count_dresult = countq(dataset, predicate=corruptpred,p=cprivacy)
		avg_dresult = avgq(dataset, predicate=corruptpred,p=cprivacy,b=nprivacy)

		if count_cresult[2] > 0:
			sumr.append((sum_cresult[0],sum_dresult[1],sum_cresult[2],sum_dresult[2],sum_cresult[1]))
			countr.append((count_cresult[0],count_dresult[1],count_cresult[2],count_dresult[2],count_cresult[1]))
			avgr.append((avg_cresult[0],avg_dresult[1],avg_cresult[2],avg_dresult[2],count_cresult[1]))

	return (sumr,countr,avgr)

def run_T_detection_trials(trials=100,
				 		   size=1000,
				 		   cprivacy=0.1,
				 		   nprivacy=1,
				 		   distinct=10,
				 		   cskew=0.33,
				   		   nskew=0.33):

	failure = 0
	for t in range(0,trials):
		dataset = generate(S=size,p=cprivacy,b=nprivacy,N=distinct,z1=cskew,z2=nskew)
		res = distinct_count(dataset)
		failure = failure + (res[0] == res[2])

	return (failure+0.)/trials

	

def l1_error(result_tuple, query='sum'):
	index = 0
	if query == 'sum':
		index = 0
	elif query == 'count':
		index = 1
	else:
		index = 2
	
	errors = [ [100*numpy.abs(r[0]-r[2])/max(r[2],1),100*numpy.abs(r[1]-r[2])/max(r[2],1),100*numpy.abs(r[3]-r[2])/max(r[2],1),100*numpy.abs(r[4]-r[2])/max(r[2],1)] for r in result_tuple[index]]
	
	return (numpy.mean(errors,axis=0), numpy.std(errors,axis=0))

def plot_parameter_sweep(exp_lambda,
						 parameters,
						 error=False,
						 xaxis="",
						 yaxis="",
						 title="",
						 filename="output.png"):
	
	import matplotlib.pyplot as plt
	from matplotlib import font_manager, rcParams

	plt.figure()

	X = parameters
	Y1 = []
	E1 = []

	Y2 = []
	E2 = []

	Y3 = []
	E3 = []

	for x in X:
		result = exp_lambda(x)
		Y1.append(result[0][0])
		E1.append(result[1][0])

		Y2.append(result[0][1])
		E2.append(result[1][1])

		Y3.append(result[0][3])
		E3.append(result[1][3])

	rcParams.update({'font.size': 22})

	fprop = font_manager.FontProperties(fname= 
        '/Library/Fonts/Microsoft/Gill Sans MT.ttf') 

	plt.plot(X, Y1, 's-', linewidth=2.5,markersize=16,color='#3399FF')

	if not error:
		plt.plot(X, Y2, 'o-', linewidth=2.5,markersize=16,color='#FF6666')
	else:
		plt.plot(X, Y3, 'o-', linewidth=2.5,markersize=16,color='#FF6666')
	#plt.plot(X, Y3, '--')
	plt.title(title,fontproperties=fprop)
	plt.xlabel(xaxis,fontproperties=fprop)
	plt.ylabel(yaxis,fontproperties=fprop)
	xticklabels = plt.getp(plt.gca(), 'xticklabels') 
	xticklabels = plt.getp(plt.gca(), 'yticklabels') 
	plt.setp(xticklabels, fontproperties=fprop) 
	#plt.legend(['PrivateClean','Naive', 'Dirty'], loc='upper left')
	plt.grid(True)
	plt.savefig(filename)

def plot_level_set_sweep1(xaxis="",
						 yaxis="",
						 title="",
						 filename="output.png"):
	
	import matplotlib.pyplot as plt
	from matplotlib import font_manager, rcParams

	rcParams.update({'font.size': 22})

	fprop = font_manager.FontProperties(fname= 
        '/Library/Fonts/Microsoft/Gill Sans MT.ttf') 

	plt.figure()

	X1 = [2,5,10,20,50,75,100,150,200,250,500,750,1000]
	X2 = [1.0/5,1.0/4,1.0/3,1.0/2]
	colors = ['#fdcc8a','#fc8d59','#de2d26','#b30000']

	index = 0
	for ox in X2:
		Y = []
		X = []
		
		for x in X1:
			p = run_T_detection_trials(trials=100,distinct=x,cskew=ox)
			Y.append(p)
			X.append((x+0.)/1000)
		
		plt.plot(X, Y, linewidth=2.5,color=colors[index])
		index = index + 1

	#plt.plot(X, Y3, '--')
	plt.title(title,fontproperties=fprop)
	plt.xlabel(xaxis,fontproperties=fprop)
	plt.ylabel(yaxis,fontproperties=fprop)
	xticklabels = plt.getp(plt.gca(), 'xticklabels') 
	xticklabels = plt.getp(plt.gca(), 'yticklabels') 
	plt.setp(xticklabels, fontproperties=fprop) 
	#plt.legend(['PrivateClean','Naive', 'Dirty'], loc='upper left')
	plt.grid(True)
	plt.savefig(filename)

def plot_level_set_sweep2(xaxis="",
						 yaxis="",
						 title="",
						 filename="output.png"):
	
	import matplotlib.pyplot as plt
	from matplotlib import font_manager, rcParams

	rcParams.update({'font.size': 22})

	fprop = font_manager.FontProperties(fname= 
        '/Library/Fonts/Microsoft/Gill Sans MT.ttf') 

	plt.figure()

	X1 = [2,5,10,20,50,75,100,150,200,250,500,750,1000]
	X2 = [0.05,0.1,0.25,0.5]
	colors = ['#fdcc8a','#fc8d59','#de2d26','#b30000']

	index = 0
	for ox in X2:
		Y = []
		X = []
		
		for x in X1:
			p = run_T_detection_trials(trials=100,distinct=x,cprivacy=ox)
			Y.append(p)
			X.append((x+0.)/1000)
		
		plt.plot(X, Y, linewidth=2.5,color=colors[index])
		index = index + 1

	#plt.plot(X, Y3, '--')
	plt.title(title,fontproperties=fprop)
	plt.xlabel(xaxis,fontproperties=fprop)
	plt.ylabel(yaxis,fontproperties=fprop)
	xticklabels = plt.getp(plt.gca(), 'xticklabels') 
	xticklabels = plt.getp(plt.gca(), 'yticklabels') 
	plt.setp(xticklabels, fontproperties=fprop) 
	#plt.legend(['PrivateClean','Naive', 'Dirty'], loc='upper left')
	plt.grid(True)
	plt.savefig(filename)
