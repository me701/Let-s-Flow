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
     
        labelV0 = QLabel('V0')
        labelP = QLabel('P')
        labelmiu = QLabel('miu')
        labelL = QLabel('L')
        labelrho = QLabel('rho')
        labelg = QLabel('g')
        labelrt = QLabel('rt')
        labeltype = QLabel('type')
      
        self.V0 = QLineEdit()
        self.P = QLineEdit()
        self.miu = QLineEdit()
        self.L = QLineEdit()
        self.rho = QLineEdit()
        self.g = QLineEdit()
        self.rt = QLineEdit()
        
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
        
        grid.addWidget(labelV0,1,0)
        grid.addWidget(self.V0, 1, 1)
        grid.addWidget(labelP,2,0)
        grid.addWidget(self.P, 2, 1)
        grid.addWidget(labelmiu,3,0)
        grid.addWidget(self.miu, 3, 1)        
        grid.addWidget(labelL,4,0)
        grid.addWidget(self.L, 4, 1) 
        grid.addWidget(labelrho,5,0)
        grid.addWidget(self.rho, 5, 1) 
        grid.addWidget(labelg,6,0)
        grid.addWidget(self.g, 6, 1) 
        grid.addWidget(labelrt,7,0)
        grid.addWidget(self.rt, 7, 1)
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
        V0 = float(self.V0.text())
        P = float(self.P.text())        
        miu = float(self.miu.text())
        L = float(self.L.text())
        rho = float(self.rho.text())        
        g = float(self.g.text())
        r1=10
        Vs=0
        ran = np.linspace(10, 20)
        
        if 'HagenHorizontal' in self.cb.currentText():
            def HagenHorizontal(Vh,r):
                
                k = -P/(miu*L)
                dVhdr = k * r
            
                return dVhdr
        
            Vh = odeint(HagenHorizontal, V0, r)
            plt.plot(r,Vh)
            plt.ylabel('V')
            plt.xlabel('r')
            plt.show()
            
            a = -P/(miu*L*4)*(rt**2-x**2) * 2*3.141592653*x

            Vhvol = simps(a,x)
            Vhaveg = Vhvol/3.141592653/rt**2
            print("volumeric flowrate = ",Vhvol)
            print("average velocity = ",Vhaveg)
    
        if 'Hagenvertical' in self.cb.currentText():
            def Hagenvertical(Vv,r):

                k = -rho*g/2/miu
                dVvdr = -k * r
                
                return dVvdr
            
            Vv = odeint(Hagenvertical,V0,r)
            plt.plot(r,Vv)
            plt.ylabel('V')
            plt.xlabel('r')
            plt.show()
            
            b = rho*g/(miu*4)*(rt**2-x**2) * 2*3.141592653*x
            Vvvol = simps(b, x)
            Vvaveg = Vvvol/3.141592653/rt**2
            
            print("volumeric flowrate = ",Vvvol)
            print("average velocity = ",Vvaveg)
        
        if 'AnnulusHorizontal' in self.cb.currentText():
            
            C1=(Vs-P/4/miu/L*(r1**2-rt**2))/np.log(r1/rt) 
            C2 = -P/4/miu/L*rt**2-C1*np.log(rt)
            
            def AnnulusHorizontal(ran):

                Van=P/4/miu/L*ran**2+C1*np.log(ran)+C2
                return Van
            
            Van = AnnulusHorizontal(ran)
                  
            plt.plot(ran, Van)
            plt.ylabel('V')
            plt.xlabel('r')
            plt.show()
            
            c = (P/4/miu/L*x**2+C1*np.log(x)+C2) * 2*3.141592653*x
            
            Vanvol = simps(c,x)
            Vanaveg = Vanvol/(3.141592653*(rt**2-r1**2))
            print("volumeric flowrate = ",Vanvol)
            print("average velocity = ",Vanaveg)
            
        if 'AnnulusVertical' in self.cb.currentText():
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
            
            x=np.linspace(20,10, 100)
            d = -rho*g/4/miu*x**2+C3*np.log(x)+C4 * 2*3.141592653*x
            
            Vanvvol = simps(d,x)
            Vanvaveg = Vanvvol/(3.141592653*rt**2-3.141592653*r1**2)
            
            print("volumeric flowrate = ",Vanvvol)
            print("average velocity = ",Vanvaveg)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    app.exec_()







