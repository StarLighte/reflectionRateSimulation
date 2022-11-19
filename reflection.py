import numpy as np
import cmath as cm
import matplotlib.pyplot as mpl


def r(na,ta,nb,tb):
    return (na*cm.cos(ta)-nb*cm.cos(tb))/(na*cm.cos(ta)+nb*cm.cos(tb))

def t(na,ta,nb,tb):
    return (2*na*cm.cos(ta))/(na*cm.cos(ta)+nb*cm.cos(tb))

def refractionRate(theta,lamda,n,d):
    length_n=len(n)
    length_d=len(d)
    if(length_n!=length_d):
        print("error")
        return "error"
    tth=lambda nnn:cm.asin(n[0]*cm.sin(theta)/nnn)
    angle=list(map(tth,n))
    k=2*cm.pi/lamda
    rr=0
    for i in range(length_n-1):
        rr=r(n[-i-2],angle[-i-2],n[-i-1],angle[-i-1]) + (t(n[-i-2],angle[-i-2],n[-i-1],angle[-i-1])*t(n[-i-1],angle[-i-1],n[-i-2],angle[-i-2])*rr*cm.exp(2j*n[-i-1]*k*d[-i-1]*cm.cos(angle[-i-1])))/(1-(r(n[-i-1],angle[-i-1],n[-i-2],angle[-i-2])*rr*cm.exp(2j*n[-i-1]*k*d[-i-1]*cm.cos(angle[-i-1]))))


    return rr

'''
for theta in np.linspace(0,0.9,9):
    g=lambda a:(cm.polar(refractionRate(cm.asin(1.35*theta/(1.7+0.02j)),193,(1.7+0.02j,1.82+0.34j,0.88314+2.778j),(0,a,0)))[0])**2
    X=list(np.linspace(0,200,100))
    Y=list(map(g,X))
    mpl.plot(X,Y)
'''

'''
for theta in np.linspace(0,0.9,9):
    g=lambda a:(cm.polar(refractionRate(cm.asin(1.35*theta/(1.7+0.02j)),193,(1.7+0.02j,1.82+0.25j,1.65+0.25j,0.88314+2.778j),(0,a,150,0)))[0])**2
    X=list(np.linspace(0,200,100))
    Y=list(map(g,X))
    mpl.plot(X,Y)
mpl.show()
'''
degree=cm.pi/180
g=lambda a:(cm.polar(refractionRate(80*degree,193,(1.7
+0.02j,1.82+.34j,0.88314+2.778j),(0,a,0)))[0])**2
print(g(1))
X=list(np.linspace(0,200,100))
Y=list(map(g,X))
mpl.plot(X,Y)
mpl.show()