import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import sys
import math
import Tkinter as Tk
import time
import matplotlib.animation as ani
from matplotlib import style
style.use('ggplot')

root = Tk.Tk()
root.wm_title("Embedding in TK")

f = Figure(figsize=(5, 4), dpi=100)
# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().grid(row=0, column=0, columnspan=5)
toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.grid(row=1, column=0, columnspan=5)


a = f.add_subplot(111)
a.grid(True)
c=np.linspace(-100,100,100)
b=np.linspace(-100,100,100)
A,B=np.meshgrid(c,b)
def ch():
    a.plot([-100,100],[0,0],'y')
    a.plot([0,0],[-100,100],'y')
    F=((A**2))+(((B-7)**2))-49
    a.contour(A,B,F,[0])
    Z=((A**2)/7)+(((B+19)**2)/37)-10
    a.contour(A,B,Z,[0])
    a.plot([5,7,12],[-34,-59,-59],'g',[-5,-7,-12],[-34,-59,-59],'g')

def ch1():
    a.cla()
    a.plot([-100,100],[0,0],'y')
    a.plot([0,0],[-100,100],'y')
    F=((A**2))+(((B-7)**2))-49
    a.contour(A,B,F,[0])
    Z=((A**2)/7)+(((B+19)**2)/37)-10
    a.contour(A,B,Z,[0])
    a.plot([5,9,7,12],[-34,-46,-59,-59],'g',[-5,-7,-12],[-34,-59,-59],'g')
    a.plot([0,-17,-5],[0,-9,-30],'g',[0,15,10],[0,9,30],'g')
    canvas.draw()
    
def ch2():
    a.cla()
    a.plot([-100,100],[0,0],'y')
    a.plot([0,0],[-100,100],'y')
    F=((A**2))+(((B-7)**2))-49
    a.contour(A,B,F,[0])
    Z=((A**2)/7)+(((B+19)**2)/37)-10
    a.contour(A,B,Z,[0])
    a.plot([5,7,12],[-34,-59,-59],'g',[-5,-9,-7,-12],[-34,-46,-59,-59],'g')
    a.plot([0,17,5],[0,-9,-30],'g',[0,-15,-10],[0,9,30],'g')
    canvas.draw()
    
def ch3():
    a.cla()
    a.set_title("When a mathematician dances")
    a.plot([-100,100],[0,0],'y')
    a.plot([0,0],[-100,100],'y')
    F=((A**2))+(((B-7)**2))-49
    a.contour(A,B,F,[0])
    Z=((A**2)/7)+(((B+19)**2)/37)-10
    a.contour(A,B,Z,[0])
    a.plot([5,7,12],[-34,-59,-59],'g',[-5,-9,-7,-12],[-34,-46,-59,-59],'g')
    a.plot([0,17,5],[0,-9,-30],'g',[0,-15,-20],[0,9,30],'g')
    canvas.draw()

def setup():
    a.cla()
    a.grid(True)
    a.set_xlim(-100,100)
    a.set_ylim(-100,100)
    a.plot([0,0],[-100,100],'g',[-100,100],[0,0],'g')

def _yx():
    a.cla()
    a.set_title('y=x')
    ch()
    x=[i for i in range(-20,20)]
    y=[i for i in x]
    a.plot(x,y,'g')
    canvas.draw()

def _yx2():
    a.cla()
    a.set_title('y=x^2')
    ch()
    x=[i for i in range(-14,15)]
    y=[(i**2)/5 for i in x]
    a.plot(x,y,'g')
    canvas.draw()

def _y_x2():
    a.cla()
    a.set_title('y=x^2')
    ch()
    x=[i for i in range(-14,15)]
    y=[-(i**2)/5 for i in x]
    a.plot(x,y,'g')
    canvas.draw()
    
def _y_x3():
    a.cla()
    a.set_title('y=x^3')
    ch()
    x=[i for i in range(-13,14)]
    y=[-(i**3)/65 for i in x]
    a.plot(x,y,'g')
    canvas.draw()

def _yx3():
    a.cla()
    a.set_title('y=x^3')
    ch()
    x=[i for i in range(-13,14)]
    y=[(i**3)/65 for i in x]
    a.plot(x,y,'g')
    canvas.draw()

def _y_x():
    a.cla()
    a.set_title('y=-x')
    ch()
    x=[i for i in range(-20,20)]
    y=[-i for i in x]
    a.plot(x,y,'g')
    canvas.draw()

def dnc():
    for i in range(6):
        ch2()
        ch3()
    for i in range(3):
        ch1()
        _yx()
        _y_x()
        _ymx()
        _yx()
        _y_x()
        _ymx()
        ch2()
        _yx2()
        _y_x2()
        _yx2()
        _y_x2()
        ch1()
        _yx3()
        _y_x3()
        _yx3()
        _y_x3()
        ch2()
        sinx()
        _sinx()
        sinx()
        _sinx()
    ch1()

def _ymx():
    a.cla()
    a.set_title('y=|x|')
    ch()
    x=[i for i in range(0,21)]
    y=[i for i in x]
    x1=[i for i in range(-20,1)]
    y1=[-i for i in x1]
    a.plot(x,y,'g',x1,y1,'g')
    canvas.draw()

def sinx():
    a.cla()
    a.set_title('y=sin(x)')
    ch()
    x=[i for i in range(-20,21,10)]
    y=[12*(math.sin(i)) for i in x]
    a.plot(x,y,'g')
    canvas.draw()

def _sinx():
    a.cla()
    a.set_title('y=-sin(x)')
    ch()
    x=[i for i in range(-20,21,10)]
    y=[-12*(math.sin(i)) for i in x]
    a.plot(x,y,'g')
    canvas.draw()


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate    
ch1()
a.set_title('Mathematics is an art!')

button = Tk.Button(master=root, text='Quit', command=_quit)
button.grid()
b1 = Tk.Button(master=root, text='y=x', command=_yx)
b1.grid(row=2,column=0)
b3 = Tk.Button(master=root, text='y=-x', command=_y_x)
b3.grid(row=2,column=1)
b6 = Tk.Button(master=root, text='y=|x|', command=_ymx)
b6.grid(row=2,column=2)
b2 = Tk.Button(master=root, text='y=x^2', command=_yx2)
b2.grid(row=2,column=3)
b12 = Tk.Button(master=root, text='y=-(x^2)', command=_y_x2)
b12.grid(row=2,column=4)
b10 = Tk.Button(master=root, text='y=x^3', command=_yx3)
b10.grid(row=2,column=5)
b11 = Tk.Button(master=root, text='y=-(x^3)', command=_y_x3)
b11.grid(row=3,column=0)
b8 = Tk.Button(master=root, text='y=sin(x)', command=sinx)
b8.grid(row=3,column=1)
b9 = Tk.Button(master=root, text='y=-sin(x)', command=_sinx)
b9.grid(row=3,column=2)
b4 = Tk.Button(master=root, text='Dance', command=dnc)
b4.grid(row=3,column=3)

def xy():
    m=mg.get()
    m=int(m)
    c=cg.get()
    c=int(c)
    x=[i for i in range(-10,11)]
    y=[(m*i)+c for i in x]
    setup()
    a.plot(x,y)
    canvas.draw()

def x2y2():
    setup()
    x=xg.get()
    x=int(x)
    y=yg.get()
    y=int(y)
    F=((A-x)**2)+((B-y)**2)-49
    a.contour(A,B,F,[0])
    canvas.draw()

def x2x():
    setup()
    a1=ag.get()
    a1=int(a1)
    b=bg.get()
    b=int(b)
    x=[i for i in range(-10,10)]
    y=[(a1*(i**2)+(b*i)) for i in x]
    a.plot(x,y)
    canvas.draw()

#y=mx+c
lm=Tk.Label(text="Enter m")
lm.grid(row=5,column=0)
mg=Tk.Entry(root)
mg.grid(row=5,column=1)
lc=Tk.Label(text="Enter c")
lc.grid(row=6,column=0)
cg=Tk.Entry(root)
cg.grid(row=6,column=1)
button=Tk.Button(text="Go",command=xy)
button.grid(row=6, column=2)
#x2+y2=r2
lx=Tk.Label(text="Enter x")
lx.grid(row=7,column=0)
xg=Tk.Entry(root)
xg.grid(row=7,column=1)
ly=Tk.Label(text="Enter y")
ly.grid(row=8,column=0)
yg=Tk.Entry(root)
yg.grid(row=8,column=1)
button1=Tk.Button(text="Go",command=x2y2)
button1.grid(row=8, column=2)
#ax2+bx+c
la=Tk.Label(text="Enter a")
la.grid(row=9,column=0)
ag=Tk.Entry(root)
ag.grid(row=9,column=1)
lb=Tk.Label(text="Enter b")
lb.grid(row=10,column=0)
bg=Tk.Entry(root)
bg.grid(row=10,column=1)
button2=Tk.Button(text="Go",command=x2x)
button2.grid(row=10, column=2)

Tk.mainloop()

