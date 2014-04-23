import numpy as np
import sys
import math
import matplotlib as plt
import pylab as py 

from scipy.optimize import curve_fit

data = np.loadtxt("datosTrayectoria.dat")

x = data[:,3]#datos de Numero de pasos
y = data[:,4]# Distancias 

py.plot (x, y, '-r', c='g')
py.title("$Grafica de pasos Vs distancia de la particula al centro$", fontsize=20)
py.xlabel("$Pasos$", fontsize= 20)
py.ylabel("$Distancia\ particula$", fontsize=20)

def py.sinfunc(x, a, b):
    return a*np.sin(x-b)
fitpars, covmat = cuerve_fit(sinfunc, x, y)
plot(x, sinfunc(x, fitpars[0], fitpar[1]), 'b-', label="Ajuste")

py.show()
py.savefig("ajustes-r.png")
