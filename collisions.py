import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def mwc64x(state):
    c = state >> 32
    x = state & 0xffffffff
    state = x * 4294883355 + c
    c = state >> 32
    x = state & 0xffffffff
    return x ^ c

N = 2**14
L = 100
m = 100
iters = 10
nuniq = []


# iterative calculation of expected hashes
it_expected_hashes = m
for i in range(1, L):
    it_expected_hashes += m * pow(1.0 - 1.0/N, i*m)
print(it_expected_hashes)

# analytical solution (non-iterative)
expected_hashes = m - (m * (pow(1.0 - 1.0/N , m) - pow(1.0 - 1.0/N, L * m))) / (pow(1.0 - 1.0/N, m) - 1.0)
print(expected_hashes)

# simplified simulation
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

state = 10
print(mwc64x(state))
print(state)


