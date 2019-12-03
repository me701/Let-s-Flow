# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication, QComboBox, QPushButton)
import sys
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.integrate import simps

class MainWindow(QWidget):
   
    def __init__(self):
        super().__init__()
        self.UI()
       
    def UI(self):
     

        labelP = QLabel('P in Pa')
        labelmiu = QLabel('viscosity in Poise')
        labelL = QLabel('L in m')
        labelrho = QLabel('density in kg/m^3')
        labelg = QLabel('g in N/m^2')
        labelrt = QLabel('outer radius in m^2')
        labelrin = QLabel('inner radius in m^2')
        labeltype = QLabel('type')

     

        self.P = QLineEdit()
        self.miu = QLineEdit()
        self.L = QLineEdit()
        self.rho = QLineEdit()
        self.g = QLineEdit()
        self.rt = QLineEdit()
        self.rin = QLineEdit()
       
        self.cb = QComboBox()
        self.cb.setObjectName("comboBox")
        self.cb.addItem("HagenHorizontal")
        self.cb.addItem("Hagenvertical")
        self.cb.addItem("AnnulusHorizontal")
        self.cb.addItem("AnnulusVertical")
       
        self.run = QPushButton('Run')
        self.run.clicked.connect(self.aaa)    
        self.clear = QPushButton('Clear')
       
        grid = QGridLayout()
        grid.setSpacing(10)
       

        grid.addWidget(labelP,1,0)
        grid.addWidget(self.P, 1, 1)
        grid.addWidget(labelmiu,2,0)
        grid.addWidget(self.miu, 2, 1)        
        grid.addWidget(labelL,3,0)
        grid.addWidget(self.L, 3, 1)
        grid.addWidget(labelrho,4,0)
        grid.addWidget(self.rho, 4, 1)
        grid.addWidget(labelg,5,0)
        grid.addWidget(self.g, 5, 1)
        grid.addWidget(labelrt,6,0)
        grid.addWidget(self.rt, 6, 1)
        grid.addWidget(labelrin,7, 0)
        grid.addWidget(self.rin, 7, 1)
        grid.addWidget(labeltype,8,0)
        grid.addWidget(self.cb, 8,1)
        grid.addWidget(self.run,9,0,1,2)
       
        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.show()


    def aaa(self):
        rt = float(self.rt.text())
        r = np.linspace(0,rt,1000)
        x = np.linspace(0,rt,1000)
        P = float(self.P.text())        
        miu = 10*float(self.miu.text())
        L = float(self.L.text())
        rho = float(self.rho.text())        
        g = float(self.g.text())
        rin = float(self.rin.text())
        Vs = 0
        t0 = 0
        ran = np.linspace(rin, rt)
        if 'HagenHorizontal' in self.cb.currentText():
            def HagenHorizontal(Vh,r):
               
                k = -P/(2*miu*L)
                dVhdr = k * r
           
                return dVhdr
           
           
            Vh0 = -P/(2*miu*L)/2*(t0**2-rt**2)

            Vh = odeint(HagenHorizontal,Vh0,r)
            plt.plot(r,Vh)
            plt.ylabel('V, m/s')
            plt.xlabel('r, m')
            plt.show()

            a = P/(miu*L*4)*(rt**2-x**2) * 2*3.141592653*x
            Vhvol = simps(a,x)
            Vhaveg = Vhvol/3.141592653/rt**2
            print("volumeric flowrate = ",Vhvol, "m^3/s")
            print("average velocity = ",Vhaveg, "m/s")
           
        if 'Hagenvertical' in self.cb.currentText():
            def Hagenvertical(Vv,r):
                k = rho*g/2/miu
                dVvdr = k * r
                return dVvdr
            Vv0 = rho*g/4/miu*(t0**2-rt**2)
            Vv = odeint(Hagenvertical,Vv0,r)
            plt.plot(r,Vv)
            plt.ylabel('V, m/s')
            plt.xlabel('r, m')
            plt.show()
            b = -rho*g/(miu*4)*(rt**2-x**2) * 2*3.141592653*x
            Vvvol = simps(b, x)
            Vvaveg = Vvvol/3.141592653/rt**2
            print("volumeric flowrate is ",Vvvol, "m^3/s")
            print("average velocity is ",Vvaveg, "m/s")

        if 'AnnulusHorizontal' in self.cb.currentText():
           
            C1=(Vs-P/4/miu/L*(rin**2-rt**2))/np.log(rin/rt)
            C2 = -P/4/miu/L*rt**2-C1*np.log(rt)
           
            def AnnulusHorizontal(ran):

                Van=-P/4/miu/L*ran**2-C1*np.log(ran)-C2
                return Van
           
            Van = AnnulusHorizontal(ran)
                 
            plt.plot(ran, Van)
            plt.ylabel('V, m/s')
            plt.xlabel('r, m')
            plt.show()
            x=np.linspace(rt,rin, 100)
            c = (P/4/miu/L*x**2+C1*np.log(x)+C2) * 2*3.141592653*x
           
            Vanvol = simps(c,x)
            Vanaveg = Vanvol/(3.141592653*(rt**2-rin**2))
            print("volumeric flowrate = ",Vanvol,"m^3/s")
            print("average velocity = ",Vanaveg, "m/s")
           
        if 'AnnulusVertical' in self.cb.currentText():
            C3=(Vs+rho*g/miu/4*(rin**2-rt**2))/np.log(rin/rt)
            C4=rho*g/miu/4*rt**2-C3*np.log(rt)
           
            def AnnulusVertical(ran):
           
                Vanv=rho*g/4/miu*ran**2-C3*np.log(ran)-C4
                return Vanv
           
            Vanv = AnnulusVertical(ran)
                 
            plt.plot(ran, Vanv)
            plt.ylabel('V, m/s')
            plt.xlabel('r, m')
            plt.show()
           
            x=np.linspace(rt,rin, 100)
            d = (-rho*g/4/miu*x**2+C3*np.log(x)+C4) * 2*3.141592653*x
           
            Vanvvol = simps(d,x)
            Vanvaveg = Vanvvol/(3.141592653*(rt**2-rin**2))
           
            print("volumeric flowrate = ",Vanvvol, "m^3/s")
            print("average velocity = ",Vanvaveg, "m/s")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    app.exec_()