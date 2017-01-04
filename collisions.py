import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

N = 2**14
L = 100
m = 100
iters = 100
nuniq = []


# iterative calculation of expected hashes
it_expected_hashes = m
for i in range(1, L):
    it_expected_hashes += m * pow(1.0 - 1.0/N, i*m)
print(it_expected_hashes)

# analytical solution (non-iterative)
expected_hashes = m - (m * (pow(1.0 - 1.0/N , m) - pow(1.0 - 1.0/N, L * m))) / (pow(1.0 - 1.0/N, m) - 1.0)
print(expected_hashes)

# simulate
for i in range(iters):
    chains = []
    for l in range(L):
        col = np.random.choice(N, m, replace=False)
        chains.append(pd.Series(col))
    df = pd.concat(chains, axis=1)
    uq = pd.Series(df.values.ravel()).unique()
    nuniq.append(len(uq))

s = pd.Series(nuniq)
print(s.mean())
plt.figure()
s.plot(kind='hist')
plt.show()
