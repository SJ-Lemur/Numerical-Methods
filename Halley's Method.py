# Root finding algorithm
#Simamkele James

def f(x):
    return x**3 - 10
def f_prime(x):
    """return 1st derivative value of f at x"""
    return 3*(x**2)

def f_prime2x(x):
    """return 2nd derivative value of f at x"""
    return 6*x

def x_n(x_0):
    """returns root approximation of the function f"""
    
    return x_0 - (2* f(x_0) * f_prime(x_0)) / (2*(f_prime(x_0))**2 - f(x_0)*f_prime2x(x_0))



x_0 = 2 # initial guess

total_iteration = 5 #total number of iterations

# denote p as the approximate value

for i in range(total_iteration):
    p = x_n(x_0)
    x_0 = p
    print(str(p))

    