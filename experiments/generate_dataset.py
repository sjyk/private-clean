
import numpy

"""
Categorical
Simulates a skewed distribution with scale z
"""
def generate_categorical_attributes(S=100,N=50,z=0.01):
	#generate probability distribution
	p = numpy.random.zipf(1.0/z, size=N)
	p = (p + 0.) / numpy.max(p)
	p = p / numpy.sum(p)

	#generate categories
	categories = range(0,N)
	return numpy.random.choice(categories, size=S, replace=True, p=p)

"""
Numerical
Simulates a skewed distribution with scale z
"""
def generate_numerical_attributes(S=100,z=0.01,c=None):
	if c == None:
		c = numpy.ones((S,1))
	return numpy.multiply(numpy.random.zipf(1.0/z, size=S),c)

"""
Randomized Response
"""
def randomized_response(data,p):
	domain = list(set(data))
	private = list(data)

	for i in range(0,len(data)):
		if numpy.random.rand(1) < p:
			private[i] = numpy.random.choice(domain)

	return private

"""
Laplace Noise
"""
def laplace(data, b):
	return list(data) + numpy.random.laplace(scale=b,size=len(data))


"""
Generate full dataset
"""
def generate(S=100,N=50,p=0.1,b=1,z1=0.01,z2=0.01):
	c1 = generate_categorical_attributes(S,N,z1)
	c2 = generate_numerical_attributes(S,z2,c1)
	p1 = randomized_response(c1,p)
	p2 = laplace(c2,b)
	return ((c1,c2),(p1,p2))

