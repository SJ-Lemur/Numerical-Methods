#Simamkele James
#Given any IVP y'=f(t,y), y(a) = j,  a <= t <= b
#The IVP should be a well posed problem
# 4th Order Method


def f(t,y):
    return  y-t**2 +1


def generate_solution(t_0, y_0,h,a,b):
    """
        performs Runge Kutta Method and generates solution of the given IVP
        on the interval [a,b].
        
        (t_0,y_0)  ---> inital conditions
        h          ---> stepsize
    """  

    w_i = y_0
    t_i = t_0
    
    print("t_i          w_i")
    while t_i < b:
        print(str("{:.1f}".format(round(t_i,2)))+"          "+str("{:.6f}".format(round(w_i,6))))

        s_1 = f(t_i,w_i)
        s_2 = f(t_i+h/2, w_i + h/2*s_1)
        s_3 = f(t_i+h/2, w_i + h/2*s_2)
        s_4 = f(t_i+h, w_i + h*s_3)

        w_i = w_i + h/6 * (s_1 + 2*s_2 + 2*s_3 + s_4)
        t_i += h

#Apply Runge Kutta's Method
t_0 = 0
y_0 = 0.5 
h = 0.2
a= 0
b = 2

generate_solution(t_0, y_0,h,a,b)

