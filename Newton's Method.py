# Bisection Method Implementation
#Simamkele James

import math
from sys import exit

def f(x):
    return x**3 - 10

#note that the initial interval [a,b] = [2,3]
a = 2
b = 3

if f(a) * f(b) >0:
    print("interval not chosen correctly")
    exit()
    
x_p = (a+b)/2 # root approximation
print(x_p)

N_0 = 5 # total number of iterations

for i in range(N_0):
    if f(x_p) * f(a) < 0:
        b = x_p
    elif f(x_p) * f(b) < 0 :
        a = x_p
    else:
        print("error occured")
        break
    
    x_p = (a+b)/2
    print(x_p)

    