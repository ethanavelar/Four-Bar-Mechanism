import numpy as np
from draw import *
from solve import *
import matplotlib.pyplot as pl
def getData():
    data = { 
        'nodes': { 'id': np.array(['A','B','C','D']) },
        'links': { 'id': np.array([1,2,3,4]), 'lengths': np.array([6, 2, 7, 9]), 'th2':30, 'w2':10}
    }
    return data


def main():
    data = getData()
    length = data['links']['lengths']
    th2 = np.radians(data['links']['th2'])
    r1 = length[0]
    r2 = length[1]
    r3 = length[2]
    r4 = length[3]
    w2 = data['links']['w2']

    h1 = r1/r2
    h2 = r1/r3
    h3 = r1/r4
    h4 = ( -(r1**2) - (r2**2) - (r3**2) + (r4**2) ) / ( 2*r2*r3 )
    h5 = ( r1**2 + r2**2 - r3**2 + r4**2 ) / ( 2*r2*r4 )
 
    a = -h1 + (1+h2)*np.cos(th2) + h4
    b = -2*np.sin(th2)
    c = h1 - (1-h2)*np.cos(th2) + h4
    d = -h1 + (1-h3)*np.cos(th2) + h5
    e = h1 - (1+h3)*np.cos(th2) + h5

    fg = pl.figure(tight_layout=True)
    ax = fg.add_subplot(1,1,1)
    th = th4th3(h1,h2,h3,h4,h5,a,b,c,d,e)
    dth = [np.degrees(g) for g in th]
    data['links']['th'] = th
    th31 = data['links']['th'][0]
    th41 = data['links']['th'][2]
    data = vector(data)
    drawLinks(data, ax)
    drawNodes(data, ax)
    w3, w4 = velocity(r2,r3,r4,th2,th31,th41,w2)
    print(w3)
    print(w4)
    pl.show()



if __name__ == '__main__': main()