#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   drawutil.py
@Desc    :   Draw functions.
'''

# here put the import lib
import matplotlib.pyplot as plt
import numpy as np

from spartan.tensor import Graph

# TODO do not import matplotlib function in model file


def plot_graph(graph: Graph, layout=None, *args, **kwargs):
    import networkx as nx
    nx_layout = {
        None: nx.draw_networkx,
        'circular': nx.draw_circular,
        'kamada_kawai': nx.draw_kamada_kawai,
        'random': nx.draw_random,
        'shell': nx.draw_shell,
        'spectral': nx.draw_spectral,
        'spring': nx.draw_spring
    }
    draw_func = nx_layout[layout]
    g = nx.from_scipy_sparse_matrix(graph.sm)
    draw_func(g, *args, **kwargs)


def drawEigenPulse(densities: list = [], figpath: str = None):
    xs = range(len(densities))
    plt.plot(xs, densities, label='density')
    plt.xlabel('window idx')
    plt.ylabel('density')
    
    thres = np.mean(densities) + 3 * np.std(densities)
    plt.hlines(thres, min(xs), max(xs), linestyles='dashed', colors='yellow', label='threshold')
    plt.legend()
    if figpath is None:
        plt.show()
    else:
        plt.savefig(figpath)    

