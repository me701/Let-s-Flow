# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:44:41 2019

@author: jasonxjy
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.integrate import simps

# initial condition
V0 = 0
P=-20
miu=10
L=10
rho = 1
g=-9.8
rt = 20
# time points
r = np.linspace(0,rt)
x = np.linspace(0,rt)

# function that returns dy/dt
def HagenHorizontal(Vh,r):

    k = -P/(miu*L)
    dVhdr = k * r

    return dVhdr


#Plot for def1
# solve ODE
Vh = odeint(HagenHorizontal,V0,r)
plt.plot(r,Vh)
plt.ylabel('V')
plt.xlabel('r')
plt.show()

a = -P/(miu*L*4)*(rt**2-x**2) * 2*3.141592653*x

Vhvol = simps(a,x)


Vhaveg = Vhvol/3.141592653/rt**2

print("volumeric flowrate is ",Vhvol, "and average velocity is ",Vhaveg)


def Hagenvertical(Vv,r):

    k = -rho*g/2/miu
    dVvdr = -k * r
    return dVvdr

#plot for def2
Vv = odeint(Hagenvertical,V0,r)

plt.plot(r,Vv)
plt.ylabel('V')
plt.xlabel('r')
plt.show()


b = rho*g/(miu*4)*(rt**2-x**2) * 2*3.141592653*x
Vvvol = simps(b, x)
Vvaveg = Vvvol/3.141592653/rt**2

print("volumeric flowrate is ",Vvvol, "and average velocity is ",Vvaveg)



r1=10

Vs=0


C1=(Vs-P/4/miu/L*(r1**2-rt**2))/np.log(r1/rt) 
C2 = -P/4/miu/L*rt**2-C1*np.log(rt)

def AnnulusHorizontal(ran):

    Van=P/4/miu/L*ran**2+C1*np.log(ran)+C2
    return Van

ran = np.linspace(10, 20)
x=np.linspace(10,20)
Van = AnnulusHorizontal(ran)
      

plt.plot(ran, Van)
plt.ylabel('V')
plt.xlabel('r')
plt.show()


c = (P/4/miu/L*x**2+C1*np.log(x)+C2) * 2*3.141592653*x

Vanvol = simps(c,x)
Vanaveg = Vanvol/(3.141592653*(rt**2-r1**2))

print("volumeric flowrate is ",Vanvol, "and average velocity is ",Vanaveg)


C3=(Vs+rho*g/miu/4*(r1**2-rt**2))/np.log(r1/rt)
C4=rho*g/miu/4*rt**2-C3*np.log(rt)

def AnnulusVertical(ran):

    Vanv=-rho*g/4/miu*ran**2+C3*np.log(ran)+C4
    return Vanv

Vanv = AnnulusVertical(ran)
      

plt.plot(ran, Vanv)
plt.ylabel('V')
plt.xlabel('r')
plt.show()

x=np.linspace(20,10)
d = -rho*g/4/miu*x**2+C3*np.log(x)+C4 * 2*3.141592653*x

Vanvvol = simps(d,x)
Vanvaveg = Vanvvol/(3.141592653*rt**2-3.141592653*r1**2)

print("volumeric flowrate is ",Vanvvol, "and average velocity is ",Vanvaveg)

'''
print(y)


'''
