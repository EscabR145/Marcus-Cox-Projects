#Warm-up exercise: Complete the following code that computes and plots 
# the 7th order Taylor series approximation and Taylor error bound for 
# f(x) = cos(x) with expansion point x=0 on the interval [-3, 3] 
# with increment 0.01.  
#
### Import section
# 3 necessary statements for numerical plotting in Jupyter
import numpy as np
import matplotlib.pyplot as plt
# Factorial comes from 'math' package
from math import factorial
#
### Initialize section
#array of derivatives at 0 compute by hand
deriv = np.array([1,0,-1,0,1,0,-1,0])
# degree of Taylor polynomial
N = len(deriv) - 1
# Max abs. value of N+1 deriv on interval (Compute using calculus)
# (used in error formula:  error <= abs(h^(N+1)/(N+1)) * max(abs(N+1th deriv.))
maxAbsNplus1deriv = 1
#array with h values
h = np.arange(-3,3.05,0.01)
# Give the expansion point for the Taylor series
expansion = 0
# Create an array to contain Taylor series
taylor = np.zeros(len(h))
#
### Calculation section
#calculate Taylor series for all h at once using a loop
for n in range(N+1):
    taylor = taylor + (h**n)/factorial(n)*deriv[n]
#actual function values 
actualFn = np.cos(expansion + h)
#error actual and taylor series
actualAbsError = abs(taylor - actualFn)
#theoretical error=|h^(deg+1)/(deg+1)!*max|n+1 deriv||
theoAbsError = abs(h**(N+1)/factorial(N+1)*maxAbsNplus1deriv)
#Compute actual x values (displaced by expansion point)
xActual = expansion + h
#
### Output section
#plot figures for cos and errors using
# Object-oriented style plotting
# Two subplots in a row
fig, axes = plt.subplots(nrows=1,ncols=2,figsize=(8,4))
# objects for the left subplot (attached to axes #0)
axes[0].plot(xActual,taylor,'r', label = 'Taylor Series')
axes[0].plot(xActual,actualFn, 'b--', label = 'Cos(x)')
axes[0].legend(loc = 2) #Put the legend in the upper left hand corner
axes[0].set_title('Taylor Series for Cos(x)')
# objects for the right subplot (attached to axes #1)
axes[1].plot(xActual,actualAbsError, label = 'Actual Absolute Error')
axes[1].plot(xActual,theoAbsError, label = 'Theoretical Absolute Error')
axes[1].legend(loc = 2) #Put the legend in the upper left hand corner
axes[1].set_title('Actual and Theoretical Error')




