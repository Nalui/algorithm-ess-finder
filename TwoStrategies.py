import sympy as sy

def twoStrategies(a):
    a11 = a[0]
    a12 = a[1]
    a21 = a[2]
    a22 = a[3]
    dif =  a11 - a12 - a21 + a22
    if dif == 0:
        if  a11 > a21:
            return [[1,0]]
        elif a11 < a21:
            return [[0,1]]
        elif a11 == a21:
            return []
    q1 = (a22 - a12)/dif
    q2 = (a11 - a21)/dif
    if q1 < 0 or q1 > 1: 
        if a11 > a21 and a22 < a12:
            return [[1,0]]
        elif a11 < a21 and a22 > a12:
            return [[0,1]]
    elif dif < 0: # q1 in [0,1]
        return [[q1,q2]]
    elif dif > 0: # q1 in [0,1]
        if a11 > a21 and a22 > a12:
            return [[1,0],[0,1]]
        if a11 > a21 and a22 == a12:
            return [[1,0]]
        if a11 == a21 and a22 > a12:
            return [[0,1]]
    return False
