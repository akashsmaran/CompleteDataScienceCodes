# Import the necessary packages; (Install matplotlib by: pip install matplotlib)
import matplotlib.pyplot as plt
import numpy as np

#We fix the seed
np.random.seed(1)
#x axis ranges from the values 0.0-50.0 with a gap of 2.0 between the points

x = np.arange(0.0,50.0,2.0)
y = x ** 1.5 + np.random.rand(x.shape[0]) * 10.0
s = (y) + np.random.rand(*x.shape) *  2
#x - x-axis pts
#y - pts on the graph
#s - size of the points
#c - Color(Here it is red)
plt.scatter(x,y,s,c ='r')
plt.show()
