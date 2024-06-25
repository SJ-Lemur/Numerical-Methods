#Simamkele James
#Given any IVP y'=f(t,y), y(a) = j,  a <= t <= b
#The IVP should be a well posed problem
# Two step method


def f(t,y):
    return y-t**2 +1


def generate_solution(t_0, y_0, t_1, y_1, a, b, h):
     """
        applies Adams-Bashfor Two-Step method to generate solution of the given IVP
        in the interval [a,b].
        
        (t_0,y_0), (t_1, y_1)  ---> inital conditions (can find (t_1,y_1) using any other one step method)
        h          ---> stepsize
    """
     w_i = (y_0, y_1)
     t_i = (t_0, t_1)
    
     print("t_i              w_i")
     while t_i[0] <= b:
            print(str("{:.1f}".format(round(t_i[0],2)))+"          "+str("{:.6f}".format(round(w_i[0],6))))

            
            w_i = (w_i[1], w_i[1] + h*(3/2*f(t_i[1], w_i[1]) - 1/2*f(t_i[0], w_i[0])))
            t_i = (t_i[1], t_i[1]+h)


#defin parameters
t_0 = 0
y_0 = 0.5 
t_1 = 0.2
y_1 = 0.829293

a = 0 
b = 2
h = 0.2
           
generate_solution(t_0, y_0, t_1, y_1, a, b, h)

