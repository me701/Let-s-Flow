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
r1=10

Vs=0


C1=(Vs-P/4/miu/L*(r1**2-rt**2))/np.log(r1/rt) 
C2 = -P/4/miu/L*rt**2-C1*np.log(rt)
C3=(Vs+rho*g/miu/4*(r1**2-rt**2))/np.log(r1/rt)
C4=rho*g/miu/4*rt**2-C3*np.log(rt)

# function that returns dy/dt



def velocities(system):
    if system =="HagenHorizontal":
        x = np.linspace(0,20)
        V = odeint(HagenHorizontal,V0,r)  
        
        a = -P/(miu*L*4)*(rt**2-x**2) * 2*3.141592653*x
        Vvol = simps(a,x)
        Vaveg = Vvol/3.141592653/rt**2
        #Plot for def1
        # solve ODE
        plt.plot(r,V)
        plt.ylabel('V')
        plt.xlabel('r')
        plt.show()

    elif system == "Hagenvertical":
        x = np.linspace(0,20)
        V = odeint(Hagenvertical,V0,r)

        b = rho*g/(miu*4)*(rt**2-x**2) * 2*3.141592653*x
        Vvol = simps(b, x)
        Vaveg = Vvol/3.141592653/rt**2
        
        #plot for def2
        plt.plot(r,V)
        plt.ylabel('V')
        plt.xlabel('r')
        plt.show()

    elif system=="AnnulusHorizontal":
        ran = np.linspace(10, 20)
        x=np.linspace(10,20)
        V = AnnulusHorizontal(ran)
         
        c = (P/4/miu/L*x**2+C1*np.log(x)+C2) * 2*3.141592653*x
        
        Vvol = simps(c,x)
        Vaveg = Vvol/(3.141592653*(rt**2-r1**2))
        
        plt.plot(ran, V)
        plt.ylabel('V')
        plt.xlabel('r')
        plt.show()
        
    elif system == "AnnulusVertical":
        ran = np.linspace(10, 20)
        V = AnnulusVertical(ran)
        x=np.linspace(20,10)
        d = -rho*g/4/miu*x**2+C3*np.log(x)+C4 * 2*3.141592653*x
        
        Vvol = simps(d,x)
        Vaveg = Vvol/(3.141592653*rt**2-3.141592653*r1**2)
        plt.plot(ran, V)
        plt.ylabel('V')
        plt.xlabel('r')
        plt.show()
        
    else:
        print("your system was not found")
        
    #print(Vvol, Vaveg)    
    return Vvol,Vaveg   

def HagenHorizontal(Vh,r):

    k = -P/(miu*L)
    dVhdr = k * r

    return dVhdr

def Hagenvertical(Vv,r):

    k = -rho*g/2/miu
    dVvdr = -k * r
    return dVvdr

def AnnulusHorizontal(ran):

    Van=P/4/miu/L*ran**2+C1*np.log(ran)+C2
    return Van


def AnnulusVertical(ran):

    Vanv=-rho*g/4/miu*ran**2+C3*np.log(ran)+C4
    return Vanv


system=str(input("please choose the type of your system 1)HagenHorizontal 2)Hagenvertical 3)AnnulusVertical 4)AnnulusHorizontal :" ))
print('\n')
print("For {} system volumeric flowrate is {} and average velocity is {}".format(system,velocities(system)[0],velocities(system)[1]))
