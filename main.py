import matplotlib.pyplot as plt

# [(Key, Priority)]
DATA = [(10, 10), (20, 20), (30, 30), (5, 70), (300, 2), (202, 24), (201, 23)]

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

def render_ktreap_rec(ktreap, x, depth, max_depth, parent_pos, ax):
    if ktreap == None:
        return

    color = "black"
    if "color" in ktreap:
        color = ktreap["color"]

    ax.scatter([x], [-depth], color=color)
    ax.text(x, -depth, str(ktreap["tuple"]), color=color)

    if parent_pos:
        plt.arrow(parent_pos[0], parent_pos[1], x-parent_pos[0], -depth-parent_pos[1])

    delta = 2 ** (max_depth - depth)
    render_ktreap_rec(ktreap["children"][0], x-delta, depth+1, max_depth, [x, -depth], ax)
    render_ktreap_rec(ktreap["children"][1], x+delta, depth+1, max_depth, [x, -depth], ax)

def render_ktreap(ktreap):
    fig, ax = plt.subplots(1, 1, figsize=(6,6))
    ax.set_axis_off()

    max_depth = treap_depth(ktreap)
    render_ktreap_rec(ktreap, 0, 0, max_depth, None, ax)

    plt.show()

def render(k, data):
    treap = create_treap(data)
    annotate_treap(k, treap)
    render_ktreap(treap)

render(3, DATA)
