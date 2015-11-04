
from experiments import *


"""
#1
Accuracy and C Privacy
"""
def experiment1():
	plot_parameter_sweep(lambda p: 
						 l1_error(run_T_trials(trials=500,
						 					   cprivacy=p,
						 					   selectivity=0.1,
						 					   errorrate=0.0,
						 					   size=1000,
											   nprivacy=0.01,
											   distinct=50,
				 							   cskew=0.5,
				 							   nskew=0.10),
						 		  query="count"), 
						 parameters=[0.001,0.1,0.2,0.3,0.4,0.5],
						 title="(A) COUNT Accuracy",
						 xaxis="Privacy (p)",
						 yaxis="Error (%)",
						 filename="results/exp1a.png")

	

	plot_parameter_sweep(lambda p: 
						 l1_error(run_T_trials(trials=500,
						 					   cprivacy=p,
						 					   selectivity=0.1,
						 					   errorrate=0.0,
						 					   size=1000,
											   nprivacy=0.01,
											   distinct=50,
				 							   cskew=0.5,
				 							   nskew=0.10),
						 		  query="sum"), 
						 parameters=[0.001,0.1,0.2,0.3,0.4,0.5],
						 title="(B) SUM Accuracy",
						 xaxis="Privacy (p)",
						 yaxis="Error (%)",
						 filename="results/exp1b.png")


	plot_parameter_sweep(lambda p: 
						 l1_error(run_T_trials(trials=500,
						 					   cprivacy=p,
						 					   selectivity=0.1,
						 					   errorrate=0.0,
						 					   size=1000,
											   nprivacy=0.01,
											   distinct=50,
				 							   cskew=0.5,
				 							   nskew=0.10),
						 		  query="avg"), 
						 parameters=[0.001,0.1,0.2,0.3,0.4,0.5],
						 title="(C) AVG Accuracy",
						 xaxis="Privacy (p)",
						 yaxis="Error (%)",
						 filename="results/exp1c.png")

"""
#2
Accuracy and NPrivacy
"""
def experiment2():
	plot_parameter_sweep(lambda p: 
						 l1_error(run_T_trials(trials=1000,
						 					   cprivacy=0.1,
						 					   selectivity=0.1,
						 					   errorrate=0.0,
						 					   size=1000,
											   nprivacy=p,
											   distinct=50,
				 							   cskew=0.5,
				 							   nskew=0.10),
						 		  query="count"), 
						 parameters=[0.001,5,10,15,20,25],
						 title="(A) COUNT Accuracy",
						 xaxis="Privacy (b)",
						 yaxis="Error (%)",
						 filename="results/exp2a.png")

	

	plot_parameter_sweep(lambda p: 
						 l1_error(run_T_trials(trials=1000,
						 					   cprivacy=0.1,
						 					   selectivity=0.1,
						 					   errorrate=0.0,
						 					   size=1000,
											   nprivacy=p,
											   distinct=50,
				 							   cskew=0.5,
				 							   nskew=0.10),
						 		  query="sum"), 
						 parameters=[0.001,5,10,15,20,25],
						 title="(B) SUM Accuracy",
						 xaxis="Privacy (b)",
						 yaxis="Error (%)",
						 filename="results/exp2b.png")


	plot_parameter_sweep(lambda p: 
						 l1_error(run_T_trials(trials=1000,
						 					   cprivacy=0.1,
						 					   selectivity=0.1,
						 					   errorrate=0.0,
						 					   size=1000,
											   nprivacy=p,
											   distinct=50,
				 							   cskew=0.5,
				 							   nskew=0.10),
						 		  query="avg"), 
						 parameters=[0.001,5,10,15,20,25],
						 title="(C) AVG Accuracy",
						 xaxis="Privacy (b)",
						 yaxis="Error (%)",
						 filename="results/exp2c.png")

"""
#3
Accuracy and Selectivity
"""
def experiment3():
	plot_parameter_sweep(lambda p: 
						 l1_error(run_T_trials(trials=500,
						 					   cprivacy=0.1,
						 					   selectivity=p,
						 					   errorrate=0.0,
						 					   size=1000,
											   nprivacy=0.001,
											   distinct=50,
				 							   cskew=0.5,
				 							   nskew=0.10),
						 		  query="count"), 
						 parameters=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
						 title="(A) COUNT Accuracy",
						 xaxis="Selectivity (s)",
						 yaxis="Error (%)",
						 filename="results/exp3a.png")

	

	

	plot_parameter_sweep(lambda p: 
						 l1_error(run_T_trials(trials=100,
						 					   cprivacy=0.1,
						 					   selectivity=p,
						 					   errorrate=0.0,
						 					   size=1000,
											   nprivacy=0.001,
											   distinct=50,
				 							   cskew=0.5,
				 							   nskew=0.10),
						 		  query="sum"), 
						 parameters=[0.1,0.3,0.5,0.7,0.9,1.0],
						 title="(B) SUM Accuracy",
						 xaxis="Selectivity (s)",
						 yaxis="Error (%)",
						 filename="results/exp3b.png")



	plot_parameter_sweep(lambda p: 
						 l1_error(run_T_trials(trials=50,
						 					   cprivacy=0.1,
						 					   selectivity=p,
						 					   errorrate=0.0,
						 					   size=1000,
											   nprivacy=0.001,
											   distinct=50,
				 							   cskew=0.5,
				 							   nskew=0.10),
						 		  query="avg"), 
						 parameters=[0.1,0.3,0.4,0.5,0.6,0.7,0.9,1.0],
						 title="(C) AVG Accuracy",
						 xaxis="Selectivity (s)",
						 yaxis="Error (%)",
						 filename="results/exp3c.png")

"""
#4
Accuracy and Skew
"""
def experiment4():
	plot_parameter_sweep(lambda p: 
						 l1_error(run_T_trials(trials=100,
						 					   cprivacy=0.15,
						 					   selectivity=0.1,
						 					   errorrate=0.0,
						 					   size=1000,
											   nprivacy=0.001,
											   distinct=50,
				 							   cskew=p+0.1,
				 							   nskew=0.10),
						 		  query="count"), 
						 parameters=[1.0/5,1.0/4,1.0/3,1.0/2],
						 title="(A) COUNT Accuracy",
						 xaxis="Skew (1/z)",
						 yaxis="Error (%)",
						 filename="results/exp4a.png")


	plot_parameter_sweep(lambda p: 
						 l1_error(run_T_trials(trials=500,
						 					   cprivacy=0.1,
						 					   selectivity=0.1,
						 					   errorrate=0.0,
						 					   size=1000,
											   nprivacy=0.001,
											   distinct=50,
				 							   cskew=p,
				 							   nskew=0.10),
						 		  query="sum"), 
						 parameters=[1.0/5,1.0/4,1.0/3,1.0/2],
						 title="(B) SUM Accuracy",
						 xaxis="Skew (1/z)",
						 yaxis="Error (%)",
						 filename="results/exp4b.png")


	plot_parameter_sweep(lambda p: 
						 l1_error(run_T_trials(trials=500,
						 					   cprivacy=0.1,
						 					   selectivity=0.1,
						 					   errorrate=0.0,
						 					   size=1000,
											   nprivacy=0.001,
											   distinct=50,
				 							   cskew=p,
				 							   nskew=0.10),
						 		  query="avg"), 
						 parameters=[1.0/5,1.0/4,1.0/3,1.0/2],
						 title="(C) AVG Accuracy",
						 xaxis="Skew (1/z)",
						 yaxis="Error (%)",
						 filename="results/exp4c.png")

"""
#5
Accuracy and Skew
"""
def experiment5():
	plot_parameter_sweep(lambda p: 
						 l1_error(run_T_trials(trials=100,
						 					   cprivacy=0.15,
						 					   selectivity=0.1,
						 					   errorrate=0.0,
						 					   size=1000,
											   nprivacy=0.001,
											   distinct=int(p*10),
				 							   cskew=0.5,
				 							   nskew=0.10),
						 		  query="count"), 
						 parameters=[50.0/10,100.0/10,150.0/10,200.0/10,500.0/10,750.0/10,1000],
						 title="(A) COUNT Accuracy",
						 xaxis="Fraction Distinct (%)",
						 yaxis="Error (%)",
						 filename="results/exp5a.png")


	plot_parameter_sweep(lambda p: 
						 l1_error(run_T_trials(trials=100,
						 					   cprivacy=0.15,
						 					   selectivity=0.1,
						 					   errorrate=0.0,
						 					   size=1000,
											   nprivacy=0.001,
											   distinct=int(p*10),
				 							   cskew=0.5,
				 							   nskew=0.10),
						 		  query="sum"), 
						 parameters=[50.0/10,100.0/10,150.0/10,200.0/10,500.0/10,750.0/10,1000],
						 title="(B) SUM Accuracy",
						 xaxis="Fraction Distinct (%)",
						 yaxis="Error (%)",
						 filename="results/exp5b.png")


	plot_parameter_sweep(lambda p: 
						 l1_error(run_T_trials(trials=100,
						 					   cprivacy=0.15,
						 					   selectivity=0.1,
						 					   errorrate=0.0,
						 					   size=1000,
											   nprivacy=0.001,
											   distinct=int(p*10),
				 							   cskew=0.5,
				 							   nskew=0.10),
						 		  query="count"), 
						 parameters=[50.0/10,100.0/10,150.0/10,200.0/10,500.0/10,750.0/10,1000],
						 title="(C) AVG Accuracy",
						 xaxis="Fraction Distinct (%)",
						 yaxis="Error (%)",
						 filename="results/exp5c.png")

def main():
	#experiment1()
	#experiment2()
	#experiment3()
	#experiment4()
	experiment5()


"""
	for t in range(0,1000):
		p = numpy.random.rand(1)[0]
		dataset = generate(S=round(10000*numpy.random.rand(1)+500),N=int(round(100*numpy.random.rand(1)+2)),p=p,b=1)
		res = countq(dataset, predicate=range(0,int(round(49*numpy.random.rand(1)))),p=p)
		#print res[0]-res[2],res[1]-res[2]
		#arr1.append(numpy.abs(res[0]-res[2]))
		#arr2.append(numpy.abs(res[1]-res[2]))
"""

"""
This script runs as the main
"""
if __name__ == "__main__":
    main()