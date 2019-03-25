import numpy as np
import random

#using numpy's random generater
"""for i in range(5):
    rng = np.random.RandomState(2019)
    print(rng.rand(5))
for i in range(5):
    random.seed(2019)
    print([random.randint(1,5) for i in range(5)])"""

def random_decimals(num,cnt,seed = None):
    result_random_decimals = []
    rng = np.random.RandomState(seed)
    for i in range(cnt):
        result_random_decimals.append(rng.rand(num))
    return result_random_decimals

def random_int(a,b,num,cnt,seed = None):
    result_random_int = []
    random.seed(seed)
    for i in range(cnt):
        result_random_int.append([random.randint(a,b) for i in range(num)])
    return result_random_int