#Simamkele James
#Given any IVP y'=f(t,y), y(a) = j,  a <= t <= b
#The IVP should be a well posed problem


def f(t,y):
    return y-t**2 + 1 

def updateFormula(w_0,t_0,t_f,h):
    """
        prints/generates valuses of y at t defined below.
     
        w_0  --> inital values= y(0) 
        t_0  --> initial time
        t_f  --> end of the interval
        h    --> stepsize
    """

    t = t_0
    w = w_0  # w approximately y

    print("t_i          w_i")
    while t <= t_f:
        print(str("{:.1f}".format(round(t,2)))+"          "+str("{:.6f}".format(round(w,6))))

        w = w + h* f(t,w)
        t += h


#Now Apply Eulers Method to generate table 
updateFormula(0.5,0,2,0.2)


              