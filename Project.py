import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import sys
import math
import Tkinter as Tk
import time
import ttk

#setting root window
root = Tk.Tk()
root.title("Maths is an Art")
root.configure(background="#99ff99")

scbar=Tk.Scrollbar(root)

#stylesheet
style = ttk.Style()
style.configure("BW.TLabel",background="#99ff99", foreground="#006600",font=('Harrington',50) ,fontstyle="Bold")
style.configure("BW.TButton",background="#70db70", foreground="black",font=('Century Gothic',18) ,fontstyle="Bold")
style.configure("BW.Label", foreground="red",font=('Century Gothic',10) ,fontstyle="Bold")


#Declaring frames
f1=Tk.Frame(root,bg="#99ff99")
f2=Tk.Frame(root)
f3=Tk.Frame(root)

#Functions to initialise Frames
def _shw1():
    f2.grid_remove()
    f3.grid_remove()
    f1.grid(row=3,column=0,columnspan=4)
   
    
def _shw2():
    f1.grid_remove()
    f3.grid_remove()
    f2.grid(row=3,column=0,columnspan=4)

def _shw3():
    f1.grid_remove()
    f2.grid_remove()
    f3.grid(row=3,column=0,columnspan=4)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate    
#title
ltitle=ttk.Label(root,text="Mathematics is an Art!",style="BW.TLabel")
ltitle.grid(row=0,column=0,columnspan=4)
txt=ttk.Label(root,text="Have you ever seen a mathematician dance?",style="BW.TLabel",font=('Candara',25))
txt.grid(row=1,column=0,columnspan=3, sticky='W')


#Menu Bar
Btn1=ttk.Button(root,text="Home",command=_shw1,style="BW.TButton")
Btn2=ttk.Button(root,text="Plot",command=_shw2,style="BW.TButton")
Btn3=ttk.Button(root,text="Learn",command=_shw3,style="BW.TButton")
Btn1.grid(row=2,column=0)
Btn2.grid(row=2,column=1)
Btn3.grid(row=2,column=2)
button = ttk.Button(master=root, text='Quit', command=_quit,style="BW.TButton")
button.grid(row=2,column=3)

#inside Frame1
f = Figure(figsize=(6,6), dpi=100)
# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=f1)
canvas.show()
canvas.get_tk_widget().grid(row=0, column=0,columnspan=4,rowspan=8)
toolbar = NavigationToolbar2TkAgg(canvas,f1)
toolbar.grid(row=9, column=0, columnspan=3)


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
    a.set_title("Let's do the Maths dance!")
    a.plot([-100,100],[0,0],'y')
    a.plot([0,0],[-100,100],'y')
    F=((A**2))+(((B-7)**2))-49
    a.contour(A,B,F,[0])
    Z=((A**2)/7)+(((B+19)**2)/37)-10
    a.contour(A,B,Z,[0])
    a.plot([5,7,12],[-34,-59,-59],'g',[-5,-9,-7,-12],[-34,-46,-59,-59],'g')
    a.plot([0,17,5],[0,-9,-30],'g',[0,-15,-20],[0,9,30],'g')
    canvas.draw()

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
    a.set_title('y=-x^2')
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
        ch1()
        _ymx()
        _yx()
        _y_x()
        _ymx()
        ch2()
        _yx2()
        _y_x2()
        ch2()
        _yx2()
        _y_x2()
        ch1()
        _yx3()
        _y_x3()
        ch2()
        _yx3()
        _y_x3()
        ch2()
        sinx()
        _sinx()
        ch1()
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

_shw1()


b1 = Tk.Button(master=f1, text='y=x', command=_yx)
b1.grid(row=0,column=4)
b3 = Tk.Button(master=f1, text='y=-x', command=_y_x)
b3.grid(row=0,column=5)
b6 = Tk.Button(master=f1, text='y=|x|', command=_ymx)
b6.grid(row=1,column=4)
b2 = Tk.Button(master=f1, text='y=x^2', command=_yx2)
b2.grid(row=1,column=5)
b12 = Tk.Button(master=f1, text='y=-(x^2)', command=_y_x2)
b12.grid(row=2,column=4)
b10 = Tk.Button(master=f1, text='y=x^3', command=_yx3)
b10.grid(row=2,column=5)
b11 = Tk.Button(master=f1, text='y=-(x^3)', command=_y_x3)
b11.grid(row=3,column=4)
b8 = Tk.Button(master=f1, text='y=sin(x)', command=sinx)
b8.grid(row=3,column=5)
b9 = Tk.Button(master=f1, text='y=-sin(x)', command=_sinx)
b9.grid(row=4,column=4)
b4 = ttk.Button(master=root, text='Check Now!', command=dnc, style="BW.TButton")
b4.grid(row=1,column=3)


#inside of Frame2
f_1 = Figure(figsize=(5, 4), dpi=100)
# a tk.DrawingArea
canvas_1 = FigureCanvasTkAgg(f_1, master=f2)
canvas_1.show()
canvas_1.get_tk_widget().grid(row=0, column=0, columnspan=5)
toolbar = NavigationToolbar2TkAgg(canvas_1,f2)
toolbar.grid(row=1, column=0, columnspan=5)


a_1 = f_1.add_subplot(111)
a_1.grid(True)
c_1=np.linspace(-100,100,100)
b_1=np.linspace(-100,100,100)
A_1,B_1=np.meshgrid(c_1,b_1)

def setup():
    a_1.cla()
    a_1.grid(True)
    a_1.set_xlim(-100,100)
    a_1.set_ylim(-100,100)
    a_1.plot([0,0],[-100,100],'g',[-100,100],[0,0],'g')

def xy():
    setup()
    m=mg.get()
    m=int(m)
    c=cg.get()
    c=int(c)
    x=[i for i in range(-70,71)]
    y=[(m*i)+c for i in x]
    setup()
    a_1.plot(x,y)
    canvas_1.draw()

def x2y2():
    setup()
    r=rg.get()
    r=int(r)
    x=xg.get()
    x=int(x)
    y=yg.get()
    y=int(y)
    F_1=((A_1-x)**2)+((B_1-y)**2)-(r**2)
    a_1.contour(A_1,B_1,F_1,[0])
    canvas_1.draw()

def x2x():
    setup()
    a1=ag.get()
    a1=int(a1)
    b=bg.get()
    b=int(b)
    x=[i for i in range(-70,71)]
    y=[(a1*(i**2)+(b*i)) for i in x]
    a_1.plot(x,y)
    canvas_1.draw()


#y=mx+c

lm=Tk.Label(f2,text="y=",width=5)
lm.grid(row=2,column=0)
mg=Tk.Entry(f2,width=5)
mg.grid(row=2,column=1)
lc=Tk.Label(f2,text="x+",width=5)
lc.grid(row=2,column=2)
cg=Tk.Entry(f2,width=5)
cg.grid(row=2,column=3)
button=Tk.Button(f2,text="Go",width=5,command=xy)
button.grid(row=2, column=4)
#x2+y2=r2
lx=Tk.Label(f2,text="Enter x")
lx.grid(row=7,column=0)
xg=Tk.Entry(f2)
xg.grid(row=7,column=1)
ly=Tk.Label(f2,text="Enter y")
ly.grid(row=8,column=0)
yg=Tk.Entry(f2)
yg.grid(row=8,column=1)
lr=Tk.Label(f2,text="Enter r")
lr.grid(row=7,column=2)
rg=Tk.Entry(f2)
rg.grid(row=7,column=2)
button1=Tk.Button(f2,text="Go",command=x2y2)
button1.grid(row=8, column=2)
#ax2+bx+c
la=Tk.Label(f2,text="Enter a")
la.grid(row=9,column=0)
ag=Tk.Entry(f2)
ag.grid(row=9,column=1)
lb=Tk.Label(f2,text="Enter b")
lb.grid(row=10,column=0)
bg=Tk.Entry(f2)
bg.grid(row=10,column=1)
button2=Tk.Button(f2,text="Go",command=x2x)
button2.grid(row=10, column=2)

#inside of Frame3
fr1=Tk.Frame(f3)
f_2 = Figure(figsize=(5, 4), dpi=100)
# a tk.DrawingArea
canvas_2 = FigureCanvasTkAgg(f_2, master=f3)
canvas_2.show()
canvas_2.get_tk_widget().grid(row=0, column=0, columnspan=5)
toolbar = NavigationToolbar2TkAgg(canvas_2,f3)
toolbar.grid(row=1, column=0, columnspan=5)

a_2 = f_2.add_subplot(111)
a_2.grid(True)
c_2=np.linspace(-100,100,100)
b_2=np.linspace(-100,100,100)
A_2,B_2=np.meshgrid(c_2,b_2)

def fr1_shw():
    fr1.grid(row=4,column=0,columnspan=5,rowspan=3)

def _line():
    #Point A
    for x in range(0,11):
        a_2.cla()
        a_2.set_title("Moving 10 units along positive X-axis")
        a_2.plot([-20,20],[0,0],'g',[0,0],[20,-20],'g')
        a_2.plot(x,0,'ro')
        canvas_2.show()
    time.sleep(2)  
    for x in range(0,11):
        a_2.cla()
        a_2.set_title("Moving 10 units along positive Y-axis")
        a_2.plot([-20,20],[0,0],'g',[0,0],[20,-20],'g')
        a_2.plot(10,x,'ro')
        canvas_2.show()
    time.sleep(1)
    a_2.set_title("This is Point A")
    canvas_2.show()
    time.sleep(1)

    #Point B
    for x in range(0,-11,-1):
        a_2.cla()
        a_2.plot(10,10,'ro')
        a_2.set_title("Moving 10 units along negative X-axis")
        a_2.plot([-20,20],[0,0],'g',[0,0],[20,-20],'g')
        a_2.plot(x,0,'ro')
        canvas_2.show()
    time.sleep(2)  
    for x in range(0,-11,-1):
        a_2.cla()
        a_2.plot(10,10,'ro')
        a_2.set_title("Moving 10 units along negative Y-axis")
        a_2.plot([-20,20],[0,0],'g',[0,0],[20,-20],'g')
        a_2.plot(-10,x,'ro')
        canvas_2.show()
    time.sleep(1)
    a_2.set_title("This is Point B")
    canvas_2.show()
    time.sleep(1)
    a_2.set_title("Bridge the gap!")
    a_2.plot([10,-10],[10,-10],'b')
    canvas_2.show()

bline=Tk.Button(f3,text="Line",command=fr1_shw)
bline.grid(row=3,column=0)
l_line=Tk.Label(fr1,text="Ill show you how to plot a line. First Plot two points. Say A(10,10) and B(-10,-10).")
l_line.grid(row=0,column=0,columnspan=5)
l_bline=Tk.Button(fr1,text="Click me!" ,command=_line)
l_bline.grid(row=1,column=0)

Tk.mainloop()

