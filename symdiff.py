#!/usr/bin/python3 -B

from ktreap import *

def val(MAX):
    L = np.arange(MAX); random.shuffle(L)
    R = np.arange(MAX)
    data = list(np.stack([L, R]).T)

    bunches1 = bunches(3, data)

    data.pop() # removes highest prio element.
    bunches2 = bunches(3, data)

    return (len(bunches1), len(bunches2), len(bunches1 ^ bunches2))

ITERS = 100
for x in [10, 100, 1000, 10000]:
    s = 0
    for _ in range(ITERS):
        s += val(x)[2]
    s /= ITERS
    print("{} -> {}".format(x, int(s)))

