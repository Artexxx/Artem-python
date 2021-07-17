import random
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np


def visualize(imgs, titles=None, colormaps=None, scale=1):
    fig = plt.figure(figsize=(10 * scale, 20 * scale))

    if type(imgs) != list:
        plt.imshow(imgs.astype(np.uint8), cmap=colormaps)
        plt.show()
        return None

    for plt_idx, img in enumerate(imgs, start=1):
        if img.shape[0] == 3:
            img = img.transpose(1, 2, 0)
        ax = fig.add_subplot(3, len(imgs), plt_idx)
        ax.set_xticks([]); ax.set_yticks([])
        ax.imshow(img.astype(np.uint8), cmap=colormaps[plt_idx - 1] if colormaps else None)
        if titles:
            ax.set_title(titles[plt_idx - 1], size=15 * (scale * 0.8))
    plt.show()
    return None


####----------------- Visualize Block Splitting  -----------------####

def visualize_block_splitting(image):
    fig = plt.figure(figsize=(4, 5))
    ax = fig.add_subplot()
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set_xticks([]); ax.set_yticks([])
    loc = plticker.MultipleLocator(base=8)
    ax.xaxis.set_major_locator(loc); ax.yaxis.set_major_locator(loc)

    ax.grid(which='major', axis='both', linestyle='-', color='b')
    ax.imshow(image.astype(np.uint8))


####----------------- Visualize Discrete Cosine Transform  -----------------####

def visualize_DCT_kernel_matrix(dct_kernel_matrix):
    fig, axes = plt.subplots(nrows=8, ncols=8, figsize=(8, 8))
    fig.patch.set_facecolor('#ececec')
    vmin, vmax = dct_kernel_matrix.min(), dct_kernel_matrix.max()
    for i in range(8):
        for j in range(8):
            axes[i, j].imshow(dct_kernel_matrix[i, j], cmap='gray', vmin=vmin, vmax=vmax)
            axes[i, j].axis('off')


####----------------- Visualize HuffmanTree -----------------####

def draw_nx(G, root, figsize=(20, 10)):
    def nodes_label_filter(nodes):
        for node, item in nodes.items():
            nodes[node] = item if (item != None) else ''
        return nodes

    def nodes_filter(nodes):
        filtered_nodes = []
        for node, item in nodes.items():
            if (item != None) and node!=root:
                filtered_nodes.append(node)
        return filtered_nodes

    edge_labels = nx.get_edge_attributes(G, 'label')
    node_labels = nodes_label_filter(nx.get_node_attributes(G, 'label'))

    pos = hierarchy_pos(G, root)
    plt.figure(figsize=figsize)

    # Draw raw graph
    # nx.draw_networkx_nodes(G, pos, node_color=None, node_color='#55aa55', alpha=0.3)
    nx.draw_networkx_edges(G, pos, alpha=0.9)

    # Root node
    nx.draw_networkx_nodes(G, pos, nodelist=[root], node_color='r')

    # Green nodes (filter nodes)
    nx.draw_networkx_nodes(G, pos,
                           nodelist=nodes_filter(nx.get_node_attributes(G, 'label')),
                           node_color='#55aa55',
                           alpha=0.15,
                           node_size=900)
    # Edge Labels
    nx.draw_networkx_edge_labels(G, pos,
                                 edge_labels=edge_labels,
                                 font_size=16,
                                 font_family='sans-serif', )
    # Node Labels
    nx.draw_networkx_labels(G, pos,
                            labels=node_labels,
                            font_size=15,
                            font_family='sans-serif')


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    """
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.
    """
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos: G is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        '''
        see hierarchy_pos docstring for most arguments
        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed
        '''

        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap, vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


def build_graph(tree, G=None):
    """Add nodes recursively and create a list of edges"""

    # Create Digraph object
    if G is None:
        G = nx.Graph()
        G.add_node(str(tree), label=tree.char)

    # Add nodes
    if tree.left:
        G.add_node(str(tree.left), label=tree.left.char)
        G.add_edge(str(tree), str(tree.left), label="0")
        G = build_graph(tree.left, G=G)

    if tree.right:
        G.add_node(str(tree.right), label=tree.right.char)
        G.add_edge(str(tree), str(tree.right), label="1")
        G = build_graph(tree.right, G=G)
    return G


def visualize_huffman_tree(h, figsize=(15, 5)):
    G = build_graph(h.root)
    draw_nx(G, str(h.root), figsize=figsize)
    return None
