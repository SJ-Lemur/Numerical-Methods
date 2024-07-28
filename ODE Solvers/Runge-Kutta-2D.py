# Simamkele James
# Method for numerically solving 2D ODE systems


import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    """x_dot = f(x,y)"""
    return y
    
    
def g(x,y):
    """y_dot = g(x,y)"""
    
    return x - x**3
    
def update_formula(t_0, t_f, del_t, x_0, y_0):
    """performes runge-kutta method
    
    vector_k1 = k11,k12
    vector_k2 = k21,k22 ....
    
    t_0 = initial time
    t_f = final time
    del_t = step size
    
    x_0, y_0 = initial conditions """
    
    t = 0
    x = x_0
    y = y_0
    
    xy_arr = []   # solution of the system given IC
    
    
    while t <= t_f:
        # vector k1
        k11 = f(x, y) * del_t
        k12 = g(x, y) * del_t
        
        # vector k2
        k21 = f(x + (1/2)*k11, y+(1/2)*k12) * del_t
        k22 = g(x + (1/2)*k11, y+(1/2)*k12) * del_t
        
        # vector k3
        k31 = f(x+(1/2)*k21, y+ (1/2)*k22) * del_t
        k32 = g(x+(1/2)*k21, y+ (1/2)*k22) * del_t
        
        # vector k4
        k41 = f(x+k31, y+ k32) * del_t
        k42 = g(x+k31, y+ k32) * del_t
        
        t += del_t
        x = x+ (1/6)*(k11 + 2*k21 + 2*k31 + k41)
        y = y+ (1/6)*(k12 + 2*k22 + 2*k32 + k42)
                    
        xy_arr.append((x,y))
        
    
    return xy_arr


#perform RUNGE-KUTTA

xy_arr = update_formula(-10,10, 0.1, 0.5,0.3)

# Assume x and y are your solution arrays
x = []
y = []

for point in xy_arr:
    x.append(point[0])
    y.append(point[1])

        
# PLOT THE PHASE PORTRAIT

x = np.array(x)
y = np.array(y)

plt.figure(figsize=(10, 8))
plt.plot(x, y, 'b-', label='Trajectory')
plt.scatter(x, y, c='r', s=10)  # Optional: to show points more clearly

# Customize the plot
plt.xlabel('X-axis label')  # Replace with your appropriate label
plt.ylabel('Y-axis label')  # Replace with your appropriate label
plt.title('Phase Portrait')
plt.legend()
plt.grid()
plt.show()