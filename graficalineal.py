import matplotlib.pyplot as plt
import numpy as np
N = 100
m = 10
b = 5

def f(x):
    return m*x+b

x = np.linspace(-10,10, num=N)
y = f(x)

print(y)

fig, ax= plt.subplots()
ax.plot(x,y)
ax.grid()