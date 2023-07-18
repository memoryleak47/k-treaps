# [(Key, Priority)]
DATA = [(10, 10), (20, 20), (30, 30)]

# node = {"tuple": (_, _), "children": [_, _], "color"}

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

# annotates a treap with colors to express k-bunches
def treap_to_ktreap(k, treap):
    pass

def render_ktreap(ktreap):
    pass

def render(k, data):
    treap = create_treap(data)
    ktreap = treap_to_ktreap(k, treap)
    render_ktreap(ktreap)

render(3, DATA)
