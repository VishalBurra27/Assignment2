import matplotlib.pyplot as plt
import numpy as np


def f(x):
    y=(8*x+556)/7
    return y
xlist=np.linspace(0,10,num=1000)
ylist=f(xlist)
plt.plot(xlist,ylist,label="$8x-7y+556=0$")
plt.title("Regression Equation")
plt.axvline(color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

