from sympy.core.symbol import var
import FindEss as fe
import EssByNash as en
import sympy as sy
import numpy as np

# m = sy.Matrix([[-0.5,2],[0,1]])
# print(find_ess.findEss(m))

# m2 = sy.Matrix([[3,4,-1],[-1,3,-2],[1,-1,3]])
# print(find_ess.ess(m2))

# x, y, z, w = sy.symbols('x y z w')
# print(sy.linsolve((x-3*y+4*z-2,2*x-6*y+8*z-7),(x,y,z)))

# xvect = sy.Matrix([(1, 0, 0)])

''' TESTES DA FUNÇÂO FINDESS'''
# a = sy.Matrix([[3,-2,4,-1],[4,-2,1,4],[-1,3,3,-2],[1,2,-1,3]])
# a = sy.Matrix([[-2,1,4],[3,3,-2],[2,-1,3]]) #ta diferente do evolutionarygames(R)
# a = sy.Matrix([[0,-1,1],[1,0,-1],[-1,1,0]])
# a = sy.Matrix([[2,0,4],[0,0,0],[3,0,1]])
# a = sy.Matrix([[4,2],[1,3]])
# a = sy.Matrix([[2,4],[3,1]])
# a = sy.Matrix([[0.625,0.369,0.276,0.255],[0.848,0.602,0.356,0.266],
#     [0.685,0.620,0.440,0.260],[0,0,0,0]])
# print(fe.findEss(a))


''' TESTES DA FUNÇÂO ESSBYNASH'''
# a = np.array([[-2,1,4],[3,3,-2],[1,-1,3]])
# a = np.array([[0,-1,1],[1,0,-1],[-1,1,0]])
# a = np.array([[2,4],[3,1]])
# a = np.array([[3,-2,4,-1],[4,-2,1,4],[-1,3,3,-2],[1,2,-1,3]])
# np.array([[0.625,0.369,0.276,0.255],[0.848,0.602,0.356,0.266],
    # [0.685,0.620,0.440,0.260],[0,0,0,0]])
# print(en.essByNash(a))


# x = [4/5,1/5]
# print(x, a)
# print(fe
#.isEss(x,a)) #acho que deveria ser true