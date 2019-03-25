import numpy as np
import scipy.stats as ss
#type(data) : array
def Arithmetic_average(data):
    return np.mean(data)

def Geometric_average(data):
    tmp = np.prod(np.array(data))
    return np.power(tmp,data)

def Harmonic_average(data):
    return ss.hmean(data)

def mode(data):
    return ss.mode(data)