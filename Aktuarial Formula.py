# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:49:12 2019

@author: ananda putri
"""

#Actuarial Present Value
import os
os.chdir("C:\\Users\\ananda putri\\Documents\\matematika asuransi")
import pandas as pd
data=pd.read_csv("TMT 2012.csv")
import numpy as np
data=np.matrix(data)
data[x,1]
i=float(input("masukkan tingkat bunga= "))
x=int(input("masukkan usia pemegang polis= "))
X=int(input("masukkan usia meninggal pemegang polis= "))
v=(1+i)**(-1)
t=X-x
def Vt(i,t):
    return (1+i)**(-t)
def tPx(x,t):
    return 1-(t*data[x,1])
def miuxplust(x,t):
    return (data[x,1]/tPx(x,t))
miuxplust(x,t)
def zf(t):
    return (Vt(i,t))*(tPx(x,t))*(miuxplust(x,t))
from scipy.integrate import quad
A,k=quad(zf,x,x+t)
print ('Actuarial Present Value = ',A)

#Actuarial untuk anuitas berjangka n makeham
def Vt(i,t):
    Vt= (1+i)**(-t)
    return Vt
def tPx(A,B,C,x,t):
    m= B/np.log10(C)
    pe= -(A*t)-(m*C**x)*((C**t)-1)
    import math
    tPx= math.exp(pe)
    return tPx
def miu(A,B,C,x,t):
    return A+(B*((C)**(x+t)))
def zf(t):
    return (Vt(i,t))*(tPx(A,B,C,x,t))*miu(A,B,C,x,t)
def A():
    i=float(input("masukkan tingkat bunga= "))
    x=int(input("masukkan usia pemegang polis= "))
    A=float(input("masukkan A= "))
    B=float(input("masukkan B= "))
    C=float(input("masukkan C= "))
    n=int(input("masukkan jangka= "))
    def zf(t):
        return (Vt(i,t))*(tPx(A,B,C,x,t))*miu(A,B,C,x,t)
    from scipy.integrate import quad
    a,r=quad(zf,0,n)
    return a
A()


#Actuarial untuk anuitas berjangka n gompertz
import numpy as np
def Vt(i,t):
    Vt= (1+i)**(-t)
    return Vt
def tPx(A,B,C,x,t):
    pe= (B*C**x)*((C**t)-1)/np.log10(C)
    import math
    tPx= math.exp(pe)
    return tPx
def a():
    i=float(input("masukkan tingkat bunga= "))
    x=int(input("masukkan usia pemegang polis= "))
    A=float(input("masukkan A= "))
    B=float(input("masukkan B= "))
    C=float(input("masukkan C= "))
    n=int(input("masukkan jangka= "))
    def vp(t):
        return Vt(i,t)*tPx(A,B,C,x,t)
    from scipy.integrate import quad
    a,r=quad(vp,0,n)
    return a
a()








