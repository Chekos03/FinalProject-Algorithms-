import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import time


class Node:
    def __init__(self, key, color="#1a1a40"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.clf()
    nx.draw(tree, pos=pos, labels=labels,
            arrows=False, node_size=2500, node_color=colors)
    plt.pause(0.6)


def build_heap_tree(heap):
    if not heap:
        return None
    nodes = [Node(value) for value in heap]
    for i in range(len(nodes)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(nodes):
            nodes[i].left = nodes[left]
        if right < len(nodes):
            nodes[i].right = nodes[right]
    return nodes[0]


def bfs_traversal(root):
    order = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def dfs_traversal(root):
    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order



def visualize_traversal(root, traversal):
    total = len(traversal)

    for i, node in enumerate(traversal):
        intensity = int(40 + (200 * i / total))
        node.color = f"#{intensity:02x}{intensity:02x}ff"
        draw_tree(root)



def visualize_heap_traversals(data):
    heap = data.copy()
    heapq.heapify(heap)

    root = build_heap_tree(heap)

    plt.figure(figsize=(8, 5))

    print("BFS traversal")
    bfs_order = bfs_traversal(root)
    visualize_traversal(root, bfs_order)

    time.sleep(1)

    for node in bfs_order:
        node.color = "#1a1a40"

    print("DFS traversal")
    dfs_order = dfs_traversal(root)
    visualize_traversal(root, dfs_order)

    plt.show()



data = [7, 3, 5, 1, 9, 2, 8]
visualize_heap_traversals(data)