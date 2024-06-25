#Simamkele James
#Given any IVP y'=f(t,y), y(a) = j,  a <= t <= b
#The IVP should be a well posed problem
# 2nd Order Method


def f(t,y):
    """define your function here"""
    return t*y+t**3

def generate_points(t_0, y_0,h,a,b):
    """
    performs Midpoint Method and generates solution of the given IVP
    on the interval [a,b].
    
    (t_0,y_0)  ---> inital conditions
    h          ---> stepsize
    """

    w_i = y_0
    t_i = t_0

    print("t_i          w_i")
    while t_i <= b:
        print(str("{:.1f}".format(round(t_i,2)))+"          "+str("{:.6f}".format(round(w_i,6))))

        w_i = w_i + h*f(t_i+h/2, w_i+h/2*f(t_i,w_i))
        t_i += h


#Apply Midpoint Method
t_0= 0
y_0= 1
h = 0.2
a= 0
b = 2

generate_points(t_0, y_0,h,a,b)


