# import numpy as np
# import matplotlib.pyplot as plt
#
# #Fibonacci
# def fibn(n):
#     if n == 0:
#         return [0]
#     elif n == 1:
#         return [0, 1]
#     else:
#         lst = fibn(n-1)
#         lst.append(lst[-1] + lst[-2])
#         return lst
#
# #print(list(fibn(100)))
#
#
# #Fractals
#
# def fractal(file):
#     dico ={}
#     i=-1.2
#     letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
#     for letter in letters:
#         dico[letter]= i
#         i +=0.1
#
#     n = [dico[letter] for letter in file]
#
#     x=[0]
#     y=[0]
#
#     for i in list(range(1,150)):
#         xi = n[0] + n[1]*x[i-1] + n[2]*x[i-1]**2 + n[3]*x[i-1]*y[i-1]+ n[4]*y[i-1] + n[5]*y[i-1]**2
#         yi = n[6] + n[7]*x[i-1] + n[8]*x[i-1]**2 + n[9]*x[i-1]*y[i-1] + n[10]*y[i-1]+n[11]*y[i-1]**2
#         x.append(xi)
#         y.append(yi)
#
#     return [x,y]
#
# # file= "GIIETPIQRRUL"
# # res = fractal(file)
# # plt.plot(res[0],res[1])
# # plt.ylabel("y")
# # plt.xlabel("X")
# # plt.show()
#
#
#
# #Prime numbers
# import math
# def primenum(number):
#     primes = []
#     for i in range(2,number+1):
#         primes.append(i)
#
#     i = 2
#     while(i <= int(math.sqrt(number))):
#         if i in primes:
#             for j in range(i*2, number+1, i):
#                     if j in primes:
#                         primes.remove(j)
#         i = i+1
#     return (primes)
#
# print(primenum(10))

#REACTION DIFFUSION

from math import sqrt
from scipy.stats import norm
import numpy as np

def brownian(x0, n, dt, delta, out=None):
    x0 = np.asarray(x0)
    r = norm.rvs(size=x0.shape + (n,), scale=delta * sqrt(dt))
    if out is None:
        out = np.empty(r.shape)
    np.cumsum(r, axis=-1, out=out)
    out += np.expand_dims(x0, axis=-1)
    return out

import numpy
from pylab import plot, show, grid, xlabel, ylabel

delta = 2
T = 10.0
N = 500
dt = T/N
m = 20
x = numpy.empty((m,N+1))
x[:, 0] = 50

brownian(x[:,0], N, dt, delta, out=x[:,1:])
t = numpy.linspace(0.0, N*dt, N+1)
for k in range(m):
    plot(t, x[k])
xlabel('t', fontsize=16)
ylabel('x', fontsize=16)
grid(True)
show()