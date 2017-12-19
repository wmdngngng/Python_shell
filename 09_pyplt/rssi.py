import math
import numpy as np
#from scipy.optimize import leastsq
import pylab as pl
import matplotlib.pyplot as plt

#ax = plt.axes(xlim=(0, 2), ylim=(-2, 2)) 
Y_Buf_Old = []
Y_Buf_New = []
Y_Buf_Log = []
X_Buf = []
DB_Buf = []

def Rssi_db():
    plt.title("Rssi to DB")
    plt.xlabel("Rssi")
    plt.ylabel("DB")
    y1 = []
    y2 = []
    y3 = []
    y = []
    r_x = []
    x = range(1,1000000,1)
    lasty = 0
    for i in x:
        y1.append(math.log10(i))
        y2.append(10*math.log10(i))
        t = 20*math.log10(i)
        y3.append(t)
        if (t-lasty)>=0.1:
            lasty = t
            y.append(t)
            r_x.append(i)
    plt.plot(x,y1,'r')
    plt.plot(x,y2,'g')
    plt.plot(x,y3,'b')
    plt.show()
    #print(r_x)
    return r_x
    
def Get_X():
    x = list(range(1,200,20))
    a = list(range(200,400,20))
    x = x+a;
    a = list(range(400,800,40))
    x = x+a;
    a = list(range(800,3300,250))
    x = x+a;
    a = list(range(3300,10300,700))
    x = x+a;
    a = list(range(10300,35600,2530))
    x = x+a;
    a = list(range(35600,114000,7840))
    x = x+a;
    a = list(range(114000,360000,24600))
    x = x+a;
    a = list(range(360000,1000000,64000))
    x = x+a;
    return x

def rssi_old(temp_rssi):
    if temp_rssi > 1000000:
        return 1
    elif temp_rssi >= 360000:
        return 2
    elif temp_rssi >= 114000:
        return 3
    elif temp_rssi >= 25600:
        return 4
    elif temp_rssi >= 10300:
        return 5
    elif temp_rssi >= 3300:
        return (10-(temp_rssi-3300)/1400)
    elif temp_rssi >= 800:
        return (20-(temp_rssi-800)/250)
    elif temp_rssi >= 400:
        return (80-(temp_rssi-200)/15)
    elif temp_rssi>= 200:
        return (200-(temp_rssi*2-400)/3)
    else:
        return 255
        
def rssi_new(temp_rssi):
    if temp_rssi > 1000000:
        return 1
    elif temp_rssi >= 360000:   #1~-10db
        return 2
    elif temp_rssi >= 114000:   #11~-20db
        return 3
    elif temp_rssi >= 25600:    #21~-30db
        return 4
    elif temp_rssi >= 10300:    #31~-40db
        return 5
    elif temp_rssi >= 8000:
        return 10
    elif temp_rssi >= 5000:
        return 20
    elif temp_rssi >= 3000:
        return 38
    elif temp_rssi >= 1500:
        return 65
    elif temp_rssi >= 800:
        return 100
    elif temp_rssi >= 300:
        return 170
    else:
        return 255;
        

def Get_Y(x_buf):
    #print(x_buf)
    y_buf_old = []
    y_buf_new = []
    y_buf_log = []
    x_buf_i = []
    i = 0
    for t_x in x_buf:
        i = i+1
        y_buf_old.append(rssi_old(t_x))
        y_buf_new.append(rssi_new(t_x))
        y_buf_log.append(125-20*math.log10(t_x))
        x_buf_i.append(i)
    return y_buf_old,y_buf_new,y_buf_log,x_buf_i

def PolyFit():
    x = np.arange(1, 17, 1)
    y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])
    z1 = np.polyfit(x, y, 3)
    p1 = np.poly1d(z1)
    print(z1)
    print(p1)
    
    z2 = np.polyfit(x, y, 6)
    p2 = np.poly1d(z2)
    print(z2)
    print(p2) 

    pl.plot(x, y, 'b^-', label='Origin Line')
    pl.plot(x, p1(x), 'gv--', label='Poly Fitting Line(deg=3)')
    pl.plot(x, p2(x), 'r*', label='Poly Fitting Line(deg=6)')
    pl.axis([0, 18, 0, 18])
    pl.legend()
    
    
if __name__ == "__main__":
    x_i = []
    PolyFit()
    X_Buf = Rssi_db()
    plt.title("Rssi to LC")
    plt.xlabel("0.1db")
    plt.ylabel("lc")
    
    #X_Buf = Get_X()
    Y_Buf_Old,Y_Buf_New,Y_Buf_Log,x_i = Get_Y(X_Buf)
    plt.plot(x_i, Y_Buf_Old,'.'+'r')
    plt.plot(x_i, Y_Buf_New,'.'+'g')
    #plt.plot(x_i, Y_Buf_Log,'b')
    plt.show()
    
    