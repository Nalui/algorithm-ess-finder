import sympy as sy
import TwoStrategies as twos

def findEss (a):
    n = a.shape[0]
    if n == 2:
        ess = twos.twoStrategies(a)
    elif n > 2:
        ess = nStrategies(a,n)
    else: 
        return "ERROR"
    return ess

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

        solucaoSistema = sy.solve(parciais, x[:I-1]) # I - 1 variaveis

        classificaSolucao = len(solucaoSistema)
        if classificaSolucao == I-1: # se a solução for unica
            solucaoSistema = inDelta(solucaoSistema)
            if solucaoSistema:
                if isEss(solucaoSistema, a):
                    ess.append(solucaoSistema)
                    return ess
        elif classificaSolucao == 1 and inDeltaMultiple(solucaoSistema): #ta tudo errado aqui
            #se a solução for possivel indeterminada e possuir uma parte pertencente a delta
            if isEss(solucaoSistema):
                ess.append(solucaoSistema)
                return ess

        I = I - 1
        essStep3 = nStrategies(a, I)
        for i in essStep3:
            ess.append(i)
        return ess

    if I < n: #TODO verificar se não falta nada
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

def inDelta(solucaoSistema):
    #verifica se a solução pertence a delta (0<=xi<=1) e traz o xn
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

def inDeltaMultiple(solucaoSistema): #TODO tentar contemplar esse caso também
    return False

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
                if dif2 < 0:
                    return False
        y[0,i] = 0
    return True