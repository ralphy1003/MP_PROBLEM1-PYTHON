#PROBLEM 1-PYTHON
import numpy as np
import matplotlib.pyplot as plt

def plotprob(x):
	if x <= 9:
		return (x*x)-7
	else:
		return ((x*x)-7)-10

yaxis = np.vectorize(plotprob)

x = np.arange(0,100)
y = yaxis(x)

plt.axis([0,100,-400,10000])
plt.stem(x,y)
plt.show()
