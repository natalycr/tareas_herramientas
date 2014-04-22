import numpy as np
import sys
import math

print "Marcha Aleatoria 1er punto","\n"

R=float(sys.argv[1])  #Radio del Sol
print type(R)
x=[]
y=[]
z=[]
N=[]
ra=[]


i=0 #contador
r=0 #radio en el que se encuentra la particula
xo=0
yo=0
zo=0
while r<=R:

    #para la particula pasos de 1
    theta=np.random.randrange(0,359)
    phi=np.random.randrange(90,270)

    p=1 # distancia de cada  paso
    xi=p* np.sin(theta)* np.cos(phi) #posicion en x
    yi=p* np.sin(theta)* np.sin(phi) #posicion en y
    zi=p* np.cos(phi)#posicion en z
    
    xo=xo+xi
    yo=xo+xi
    zo=xo+xi
    r=(xo**2+yo**2+zo**2)**0.5
    i=i+1
    x.append(xo)
    y.append(xo)
    z.append(xo)
    N.append(i)
    ra.append(r)
    
print N[-1],ra[-1]




    
