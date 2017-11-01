import numpy as np

def gs(U, A, F, m, maxiters = 3, tol = 10**-8, P = []):
    if len(P) == 0:
        for j in range(0,maxiters):
            r = F - A.dot(U)
            if np.linalg.norm(r, np.inf) < tol:
                print("Residual diminished below tolerance.")
                return U
            for i in range(0,m):
                U[i] = (1/A[i,i])*(F[i] - A[i, :].dot(U) + A[i, i]*U[i])
        print("Maximum iterations exceeded.")
        return U
    else:
        for j in range(0, maxiters):
            for i in range(0, m):
                U[i] = max(P[i], (1 / A[i, i]) * (F[i] - A[i, :].dot(U) + A[i, i] * U[i]))
        return U
