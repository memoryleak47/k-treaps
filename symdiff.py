#!/usr/bin/python3 -B

from ktreap import *

MAX = 10000
L = np.arange(MAX); random.shuffle(L)
R = np.arange(MAX)
data = list(np.stack([L, R]).T)

bunches1 = bunches(3, data)

data.pop() # removes highest prio element.
bunches2 = bunches(3, data)

print(len(bunches1), len(bunches2), len(bunches1 ^ bunches2))

