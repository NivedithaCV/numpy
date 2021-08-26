#import module
import numpy as np
import matplotlib.pyplot as plt
from numpy import random

#seed(1)
#generate random points
data1 = random.rand(1000)
data2 = random.rand(1000)
#giving slope
m=4
#relation
y=m*data1+data2
#plot
plt.scatter(data1,y)
plt.show()
