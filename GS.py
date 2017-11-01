from __future__ import print_function
import numpy as np

# lev = 0 is coarse grid
def printindent(lev):
    indent = ""
    for j in range(lev):
        indent = indent + "   "
    print(indent, end="")

def gs(U, A, F, m, maxiters = 3, tol = 10**-8, P = [], indentlev = 0):
    if len(P) == 0:
        printindent(indentlev)
        for j in range(0,maxiters):
            r = F - A.dot(U)
            if np.linalg.norm(r, np.inf) < tol:
                print("Residual diminished below tolerance.")
                return U
            for i in range(0,m):
                U[i] = (1/A[i,i])*(F[i] - A[i, :].dot(U) + A[i, i]*U[i])
            print(".", end="")
        #print("Maximum iterations exceeded.")
        print()
        return U
    else:
        for j in range(0, maxiters):
            for i in range(0, m):
                U[i] = max(P[i], (1 / A[i, i]) * (F[i] - A[i, :].dot(U) + A[i, i] * U[i]))
        return U
