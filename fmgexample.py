from multigrid import fmg
from Poisson2D import Poisson2D
import numpy as np

f = lambda x,y: -8.0*(np.pi**2)*np.sin(2.0*np.pi*x)*np.sin(2.0*np.pi*y)

minm = 1
numcycles = 6
#numcycles = 7  # CAUSES MemoryError in Poisson2D() when attempts to allocate dense NxN matrix with m+2=257 and N=66049

# generate fine grid and discretize Poisson on it
m = minm
for i in range(0, numcycles):
    m = 2 * m + 1
N = (m + 2)**2
print('%d x %d grid with N=%d total unknowns' % (m+2,m+2,N))

A, U, F, _, X = Poisson2D(m, f, bvals = True)

# get fmg solution
U = fmg(m, F, numcycles = numcycles, eta1 = 1, eta2 = 3)

Uexact = np.zeros((N, 1))
uexact = lambda x,y: np.sin(2.0*np.pi*x)*np.sin(2.0*np.pi*y)
kk = lambda i,j: j * (m + 2) + i
for j in range(0, m + 2):
    for i in range(0, m + 2):
        k = kk(i,j)
        Uexact[k] = uexact(X[i],X[j])

print(np.linalg.norm(U - Uexact, np.inf))

