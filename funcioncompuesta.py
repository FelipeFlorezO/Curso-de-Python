import numpy as np
import matplotlib.pyplot as plt

N = 1000

x = np.linspace(-10, 10,num= N)

def g(x):
    return x**2
def f(x):
    return np.sin(x)

y = g(x)

f_o_g = f(y)

plt.plot(x,f(y))

