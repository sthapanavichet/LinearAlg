import numpy

# transition probability matrix
A = numpy.array([[0, 0, 0.33, 0.33, 0.33], [0, 0, 0, 0, 1], [0, 0.5, 0, 0.5, 0], [0, 1, 0, 0, 0], [0.33, 0.33, 0.33, 0, 0],])

# size of internet
N = 5

#initialize the pagerank vector
v = numpy.array([[1/N], [1/N], [1/N], [1/N], [1/N]])

# damping factor
d = 0.6

# update matrix
U = d * A.T + (1-d) / N
#print(A)
#print(U)
#print(v)

for i in range(15):
#compute the new pagerank vector
    v = numpy.dot(U, v)
    v = numpy.round(v, 3)
    print("Pagerank vector", i+1, "is", v.T)
