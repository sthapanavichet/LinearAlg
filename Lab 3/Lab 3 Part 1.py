import numpy

# transition probability matrix
A = numpy.array([[0, 0.25, 0.25, 0.25, 0.25], [0.5, 0, 0, 0.5, 0], [0.33, 0, 0, 0.33, 0.33], [1, 0, 0, 0, 0], [0, 0, 0, 1, 0]])

#initialize the pagerank vector
v = numpy.array([[0.2], [0.2], [0.2], [0.2], [0.2]])

# damping factor
d = 0.85

# size of internet
N = 5

# update matrix
U = d * A.T + (1-d) / N

for i in range(15):
#compute the new pagerank vector
    v = numpy.dot(U, v)
    v = numpy.round(v, 3)
    print("Pagerank vector", i+1, "is", v.T)
