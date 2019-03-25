import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_file = './data/IQ_60.txt'
data = np.loadtxt(data_file)
used_bins = [0, 75, 85, 95, 105, 115, 125, 135, 145, 155]
#display histgram
n, bins, patches = plt.hist(data,bins = used_bins,density=False,rwidth =1, align="mid", alpha=0.5, histtype="bar",ec="black")
print(n)
# %% Set graph attributes
plt.xlim((65, 155))
plt.xlabel('range of x')
plt.ylabel('Frequency')
plt.show()