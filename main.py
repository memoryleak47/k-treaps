import matplotlib.pyplot as plt
import numpy as np
import random

# data = [(Key, Priority)]
# node = {"tuple": (_, _), "children": [_, _], "color"}
# bunch = [node, node, node, ...]

def get_color(bunch):
    s = 0
    for n in bunch:
        s += hash(n["tuple"])

    s = abs(hash(s)) // 1

    r = s % 200 / 256; s = s // 256
    g = s % 200 / 256; s = s // 256
    b = s % 200 / 256; s = s // 256

    return (r, g, b)

def create_treap(data):
    if len(data) == 0:
        return None
    data = sorted(data, key=lambda x: x[1])
    (key, prio) = data.pop()
    data_l = [x for x in data if x[0] < key]
    data_r = [x for x in data if x[0] > key]
    l_treap = create_treap(data_l)
    r_treap = create_treap(data_r)
    return {"tuple": (key, prio), "children": [l_treap, r_treap]}

# returns the list of nodes that lie forward of a bunch
def fwd(bunch):
    candidates = []
    for x in bunch:
        candidates.append(x["children"][0])
        candidates.append(x["children"][1])
    return list(filter(lambda x: (x is not None) and (x not in bunch), candidates))

# annotates a treap with colors to express k-bunches
def annotate_treap(k, treap):
    bunch = [treap]
    while len(bunch) < k:
        candidates = fwd(bunch)
        if len(candidates) == 0:
            break
        best = sorted(candidates, key=lambda x: x["tuple"][1])[-1]
        bunch.append(best)

    col = get_color(bunch)
    for b in bunch:
        b["color"] = col

    for f in fwd(bunch):
        annotate_treap(k, f)

def treap_depth(treap):
    if treap == None:
        return 0

    l = treap_depth(treap["children"][0])
    r = treap_depth(treap["children"][1])
    return max(l, r) + 1

def render_ktreap_rec(ktreap, x, depth, max_depth, parent_pos, parent, ax):
    if ktreap == None:
        return

    color = "black"
    if "color" in ktreap:
        color = ktreap["color"]

    # this does nothing except correcting the viewport
    ax.scatter([x], [-depth], color=color, alpha=0)
    ax.text(x, -depth, str(ktreap["tuple"]), color="white", horizontalalignment='center', backgroundcolor=color)

    if parent_pos:
        shared_color = "black"
        lw=1
        if color == parent["color"]:
            shared_color = color
            lw=4
        plt.arrow(parent_pos[0], parent_pos[1], x-parent_pos[0], -depth-parent_pos[1], color=shared_color, head_width=0, head_length=0, length_includes_head=True, lw=lw)

    delta = 2 ** (max_depth - depth - 1)
    render_ktreap_rec(ktreap["children"][0], x-delta, depth+1, max_depth, [x, -depth], ktreap, ax)
    render_ktreap_rec(ktreap["children"][1], x+delta, depth+1, max_depth, [x, -depth], ktreap, ax)

def render_ktreap(ktreap):
    fig, ax = plt.subplots(1, 1, figsize=(6,6))
    ax.set_axis_off()

    max_depth = treap_depth(ktreap)
    render_ktreap_rec(ktreap, 0, 0, max_depth, None, ktreap, ax)

def render(k, data):
    treap = create_treap(data)
    annotate_treap(k, treap)
    render_ktreap(treap)

MAX = 20
L = np.arange(MAX)
R = np.arange(MAX); random.shuffle(R)
data = list(np.stack([L, R]).T)
random.shuffle(data)

render(3, data)

data.pop()
render(3, data)

plt.show()
