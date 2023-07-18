# [(Key, Priority)]
DATA = [(10, 10), (20, 20), (30, 30)]

# node = {"tuple": (_, _), "children": [_, _], "color"}

def create_treap(data):
    pass

# annotates a treap with colors to express k-bunches
def treap_to_ktreap(k, treap):
    pass

def render_ktreap(ktreap):
    pass

def render(k, data):
    treap = create_treap(data)
    ktreap = treap_to_ktreap(k, treap)
    render_ktreap(ktreap)
