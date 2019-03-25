import numpy as np
import scipy.stats as ss
from random_value import random_int
#Quartiles
data = random_int(1,100,10,1)
data = data[0]
print(np.percentile(data,q = 45))
print(ss.zscore(data))