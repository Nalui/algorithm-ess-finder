import sympy as sy

def findEss (a):
    a = sy.Matrix(a)
    n = a.shape[0]
    if n == 2:
        ess = twoStrategies(a)
    elif n > 2:
        ess = nStrategies(a,n)
    return ess

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
    q1 = sy.Rational(a22 - a12,dif)
    q2 = sy.Rational(a11 - a21,dif)
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

def nStrategies(a, I):
    ess = []
    n = a.shape[0]
    if I == n:
        x = createVector(I, 'x')
        y = createVector(I, 'y')
        w = y*a*x.T

        parciais = []
        for i in range(I-1):
            parciais.append(sy.diff(w[0], y[i]))

        solucaoSistema = sy.solve(parciais, x[:I-1])

        classificaSolucao = len(solucaoSistema)
        if classificaSolucao == I-1: 
            solucaoSistema = inDelta(solucaoSistema)
            if solucaoSistema:
                if isEss(solucaoSistema, a):
                    ess.append(solucaoSistema)
                    return ess
        elif classificaSolucao < I-1 and classificaSolucao > 0:
            return 'not implemented'

        I = I - 1
        essStep3 = nStrategies(a, I)
        for i in essStep3:
            ess.append(i)
        return ess

    if I < n:
        for J in range(n):
            aJ = a[:,:]
            aJ.col_del(J)
            aJ.row_del(J)
            essDeltaI = findEss(aJ)
            for i in essDeltaI:
                extendForm = extendSolution(i, J, n)
                if isEss(extendForm,a):
                    if extendForm not in ess:
                        ess.append(extendForm)
    return ess

def createVector(n, var):
    vector = []
    last = 1
    for i in range(1, n):
        globals()['%s%s'%(var,i)] = sy.symbols('%s%s '%(var,i))
        vector.append(globals()['%s%s'%(var,i)])
        last = last - globals()['%s%s'%(var,i)]
    vector.append(last)
    vector = sy.Matrix([vector])
    return vector

def inDelta(solucaoSistema):
    sum = 0
    vetor = []
    for i in solucaoSistema:
        valor = solucaoSistema[i]
        if valor < 0:
            return False
        vetor.append(valor)
        sum += valor
    if sum > 1:
        return False
    vetor.append(1 - sum)      
    return vetor

def isEss(x, a):
    n = len(x)
    y = sy.zeros(1,n)
    x = sy.Matrix([x])
    for i in range(n):
        y[0,i] = 1 
        dif = ((x - y)*a*x.T)[0] 
        if dif < 0:
            return False
        if dif == 0:
            if x != y:
                dif2 = ((x - y)*a*y.T)[0]
                if dif2 <= 0:
                    return False
        y[0,i] = 0
    return True

def extendSolution(solucaoSistema, J, n): 
    solucaoExpandida = []
    k = 0
    for i in range(n):
        if i == J:
            solucaoExpandida.append(0)
        else:
            solucaoExpandida.append(solucaoSistema[k])
            k += 1
    return solucaoExpandida