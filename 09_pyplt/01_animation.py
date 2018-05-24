import os
import numpy as np
import subprocess
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation 

pi = 3.141592654
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2)) 
line, = ax.plot([], [],lw=2)
#G = nx.Graph()
def Init():
    print("hello")
    plt.title("Animation")
    return line,
    
def update(i):
    x = np.linspace(0, 2, 20)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    print("x",x)
    
    #print("i=%d, y=%2.2f"% (i,y))
    return line,

def main():
# call the animator.  blit=True means only re-draw the parts that have changed. 
    ani = animation.FuncAnimation(fig, update, init_func=Init, blit=True, frames=300, interval=1000)
    plt.show()
    
if __name__ == '__main__':
    main()