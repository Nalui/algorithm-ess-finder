import numpy as np
import nashpy as nash

def essByNash(a):
    ess = []
    A = a[:]
    B = a[:]
    game = nash.Game(A, B)
    for x in game.support_enumeration():
        if isEss(x[0],np.array(a)):
            ess.append(x[0])
    return ess

def isEss(x, a): #caso 2x2
    n = len(x)
    y =np.zeros(n)
    for i in range(n):
        y[i] = 1
        dif = np.dot(np.dot(x-y,a),x.T)
        if dif < 0:
            return False
        if dif == 0:
            if not np.array_equal(x,y):
                if np.dot(np.dot(x-y,a),y.T) <= 0:
                    return False  
        y[i] = 0
    return True
