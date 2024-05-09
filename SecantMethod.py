# Secant Method Implementation
#Simamkele James


def f(x):
    return x**3 - 10

def update_formula(p0,p1):
    if f(p1)-f(p0) == 0:
        return p1
    
    return p1 - (f(p1)*(p1-p0)) / (f(p1)-f(p0))


#note that the initial interval [a,b] = [2,4]
a = 2
b = 4

N_0 = 5 # total number of iterations

for i in range(N_0):
    p = update_formula(a,b)
    a = b
    b = p
    print(p)

    