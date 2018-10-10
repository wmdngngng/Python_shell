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
        
def rssi_line(temp_rssi):
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
    elif temp_rssi >= 5300:
        return 8
    elif temp_rssi >= 3300:
        return 10
    elif temp_rssi >= 2300:   #16
        return 16-(temp_rssi-2300)*6/1000
    elif temp_rssi >= 1800:   #28
        return 28-(temp_rssi-1800)*6/250
    elif temp_rssi >= 1000:   #76
        return 76-(temp_rssi-1000)*6/100
    elif temp_rssi >= 500:    #136
        return 136-(temp_rssi-500)*6/50
    elif temp_rssi >=200:
        return 208-(temp_rssi-200)*6/25
    else:
        return 255
        
def Return_Y(xs):
    y = []
    for x in xs:
        y.append(438*x*x/100000000 - x*0.053 + 156.7)
    return y
        
def Get_Y(x_buf):
    #print(x_buf)
    y_buf_old = []
    y_buf_new = []
    y_buf_line = []
    x_buf_i = []
    i = 0
    for t_x in x_buf:
        i = i+1
        y_buf_old.append(rssi_old(t_x))
        y_buf_new.append(rssi_new(t_x))
        y_buf_line.append(rssi_line(t_x))
        x_buf_i.append(i)
    return y_buf_old,y_buf_new,y_buf_line,x_buf_i

def PolyFit():
    x = np.arange(1, 17, 1)
    y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])
    
    z1 = np.polyfit(x, y, 3)    #第一个拟合，自由度为3
    p1 = np.poly1d(z1)          #生成多项式
    print(z1)
    print(p1)
    
    z2 = np.polyfit(x, y, 6)    #第二个拟合，自由度为6
    p2 = np.poly1d(z2)          #生成多项式
    print(z2)
    print(p2) 

    pl.plot(x, y, 'b^-', label='Origin Line')   #绘制原曲线
    pl.plot(x, p1(x), 'gv--', label='Poly Fitting Line(deg=3)')
    pl.plot(x, p2(x), 'r*', label='Poly Fitting Line(deg=6)')
    pl.axis([0, 18, 0, 18])
    pl.legend()
    
def PolyFitRssi():
    x = [8000, 5000, 3000, 1500, 800, 300]
    y = [10, 20, 38, 65, 100, 170]
    x1 = [8000,5000]
    y1 = [10,20]
    
    x2 = [5000,3000]
    y2 = [20,38]
    
    x3 = [3000, 1500]
    y3 = [38, 65]
    
    x4 = [1500, 800]
    y4 = [65, 100]
    
    x5 = [800, 300]
    y5 = [100, 170]
    
    x6 = [300, 100]
    y6 = [170, 250]
    
    z1 = np.polyfit(x1,y1,1)
    p1 = np.poly1d(z1)
    print(p1)
    
    z2 = np.polyfit(x2,y2,1)
    p2 = np.poly1d(z2)
    print(p2)
    
    z3 = np.polyfit(x3,y3,1)
    p3 = np.poly1d(z3)
    print(p3)
    
    z4 = np.polyfit(x4,y4,1)
    p4 = np.poly1d(z4)
    print(p4)
    
    z5 = np.polyfit(x5,y5,1)
    p5 = np.poly1d(z5)
    print(p5)
    
    z6 = np.polyfit(x6,y6,1)
    p6 = np.poly1d(z6)
    print(p6)
    
    plt.plot(x,y, 'r*')
    plt.plot(x1,y1, 'g-')
    plt.plot(x2,y2, 'b-')
    plt.plot(x3,y3, 'g-')
    plt.plot(x4,y4, 'b-')
    plt.plot(x5,y5, 'g-')
    plt.plot(x6,y6, 'b-')
    #pl.plot(x,p1(x), 'g-')
    #pl.plot(x,Return_Y(x), 'b-')
    plt.show()
    
if __name__ == "__main__":
    x_i = []
    #PolyFitRssi()
    X_Buf = Rssi_db()
    plt.title("Rssi to LC")
    plt.xlabel("0.1db")
    plt.ylabel("lc")
    
    Y_Buf_Old,Y_Buf_New,Y_Buf_Line,x_i = Get_Y(X_Buf)
    plt.plot(x_i, Y_Buf_Old,'.'+'r')
    plt.plot(x_i, Y_Buf_New,'.'+'g')
    plt.plot(x_i, Y_Buf_Line,'.'+'b')
    
    plt.show()
    
    