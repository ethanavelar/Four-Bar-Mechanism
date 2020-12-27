import matplotlib.pyplot as pl
import numpy as np
from draw import *

def drawNodes(data, ax):
    '''
    First we want to locate the nodes for the open configuration
    then we can move on to doing the closes configuration later.
    '''
    nodes = data['nodes']['id']
    x = data['links']['x']
    y = data['links']['y']
    nodes2 = np.concatenate([nodes, nodes])
    for e in range(len(x)):
        ax.plot(x[e], y[e], color='black', marker='o',markersize=18)
        ax.plot(x[e], y[e], color='white', marker='o',markersize=16)
        ax.text(x[e], y[e], nodes2[e], ha='center', va='center')

    return None

def drawLinks(data, ax):
    '''
    Now we must create the vectors to draw the links
    '''
    nodes = data['nodes']['id']
    x = data['links']['x']
    y = data['links']['y']

    for n in range(1,len(x)):
        x1 = x[n-1]
        x2 = x[n]
        y1 = y[n-1]
        y2 = y[n]

        xvec = np.array([x1,x2])
        yvec = np.array([y1,y2])
        if (n < 4):
            ax.plot(xvec, yvec, 'k-')
        elif (n > 4):
            ax.plot(xvec, yvec, 'k:')
    return None



    

def drawGeometry():
    pass