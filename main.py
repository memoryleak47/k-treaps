#!/usr/bin/python3 -B

from ktreap import *

MAX = 20
L = np.arange(MAX); random.shuffle(L)
R = np.arange(MAX)
data = list(np.stack([L, R]).T)

render(3, data)

data.pop() # removes highest prio element.
render(3, data)

plt.show()
