#!/usr/bin/python3 -B

from ktreap import *

def val(MAX):
    L = np.arange(MAX); random.shuffle(L)
    R = np.arange(MAX)
    data = list(np.stack([L, R]).T)

    bunches1 = bunches(3, data)

    data.pop() # removes highest prio element.
    bunches2 = bunches(3, data)

    return len(bunches2 - bunches1)

ITERS = 100
for x in [10, 50, 100, 500, 1000, 5000, 10000]:
    s = 0
    for _ in range(ITERS):
        s = max(s, val(x))
    c = s / np.log(x)
    print("Removing the top-prio (key, prio)-pair from a random 3-ktreap with {} nodes requires {} new 3-tuples. This is equivalent to np.log({}) * {}".format(x, s, x, c))

