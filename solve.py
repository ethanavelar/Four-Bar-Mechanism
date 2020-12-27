import numpy as np

def th4th3(h1,h2,h3,h4,h5,a,b,c,d,e):
    th = []
    th42 = 2*np.arctan( ( -b + np.sqrt(b**2 - 4*d*e) ) / (2*d) )
    th41 = 2*np.arctan( ( -b - np.sqrt(b**2 - 4*d*e) ) / (2*d) )
    th32 = 2*np.arctan( (-b + np.sqrt(b**2 -4*a*c)) / (2*a))
    th31 = 2*np.arctan( (-b - np.sqrt(b**2 -4*a*c)) / (2*a))
    th.extend([th31, th32, th41, th42])

    return th

def vector(data):
    nodes = data['nodes']['id']
    th2 = np.radians(data['links']['th2'])
    lengths = data['links']['lengths']
    th = data['links']['th']
    dth = [np.degrees(g) for g in th]
    r1 = lengths[0]
    r2 = lengths[1]
    r3 = lengths[2]
    r4 = lengths[3]
    x = [0]
    y = [0]
    x.append(r2*np.cos(th2))
    y.append(r2*np.sin(th2))
    x.append((r2*np.cos(th2))+(r4*np.cos(data['links']['th'][0])))
    y.append(r4*np.sin(data['links']['th'][0]))
    x.append(lengths[0])
    y.append(0)
    x.append(0)
    y.append(0)
    x.append(r2*np.cos(th2))
    y.append(r2*np.sin(th2))
    x.append((r2*np.cos(th2))+(r4*np.cos(data['links']['th'][1])))
    y.append(r4*np.sin(data['links']['th'][1]))
    x.append(lengths[0])
    y.append(0)
    data['links']['y'] = y
    data['links']['x'] = x
    return data

def velocity(r2,r3,r4,th2,th31,th41, w2):
    #Only solves for open configuration atm
    A1 = np.array([
        [-r3*np.sin(th31), r4*np.sin(th41)],
        [r3*np.cos(th31), -r4*np.cos(th41)]
    ])
    B1 = np.array([
        [r2*np.sin(th2)*w2],
        [-r2*np.cos(th2)*w2]
    ])
    w31, w41 = np.linalg.solve(A1, B1)

    return w31, w41

def acceleration():
    '''
    A = np.array([
        [-r3*np.sin(th31), r4*np.sin(th41)],
        [r3*np.cos(th31), -r4*np.cos(th41)]
    ])
    B = np.array([
        [r2*(np.sin(th2)*a2 + np.cos(th2)*w2**2)) + r3*np.cos(th31)*w31**2 - r4*np.cos(th41)*w41**2],
        [-r2*(np.cos(th2)*a2 - np.sin(th2)*w2**2)) + r3*np.sin(th31)*w31**2 - r4*np.sin(th41)*w41**2]
    ])

    a3, a4 = np.linalg.solve(A, B)
    '''
    return None