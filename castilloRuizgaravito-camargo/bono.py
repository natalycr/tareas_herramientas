import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import sys


R = float(sys.argv[1])

fig = plt.figure()
ax = fig.gca(projection='3d')

u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:30j]

a=R*np.cos(u)*np.sin(v)
b=R*np.sin(u)*np.sin(v)
c=R*np.cos(v)

ax.plot_wireframe(a, b, c, color="y")

data = np.loadtxt("datosTrayectoria.dat")

x = data[:,0]
y = data[:,1]
z = data[:,2]
ax.scatter(x,y,z, '-r', color='g', s=8)


plt.show()
