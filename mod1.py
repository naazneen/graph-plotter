import matplotlib
import Tkinter as Tk
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

root=Tk.Tk()
f = Figure(figsize=(5, 4), dpi=100)
# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().grid(row=0, column=0, columnspan=5)
a = f.add_subplot(111)
a.grid(True)
a.set_xlim([-10,10])
a.set_ylim([-10,10])
c=np.linspace(-100,100,100)
b=np.linspace(-100,100,100)
A,B=np.meshgrid(c,b)


def _res():
    root.geometry("500x500")
    
def _xy():
    m=mg.get()
    m=int(m)
    c=cg.get()
    c=int(c)
    x=[i for i in range(-10,11)]
    y=[(m*i)+c for i in x]
    a.plot(x,y)
    canvas.draw()

def _x2y2():
    x=xg.get()
    x=int(x)
    y=yg.get()
    y=int(y)
    F=((A-x)**2)+((B-y)**2)-49
    a.contour(A,B,F,[0])
    canvas.draw()

def _x2x():
    a1=ag.get()
    a1=int(a1)
    b=bg.get()
    b=int(b)
    x=[i for i in range(-10,10)]
    y=[(a1*(i**2)+(b*i)) for i in x]
    a.plot(x,y)
    canvas.draw()

button=Tk.Button(text="Click here",command=_res)
button.grid(row=1, column=0)
#y=mx+c
lm=Tk.Label(text="Enter m")
lm.grid(row=2,column=0)
mg=Tk.Entry(root)
mg.grid(row=2,column=1)
lc=Tk.Label(text="Enter c")
lc.grid(row=3,column=0)
cg=Tk.Entry(root)
cg.grid(row=3,column=1)
button=Tk.Button(text="Go",command=_xy)
button.grid(row=3, column=2)
#x2+y2=r2
lx=Tk.Label(text="Enter x")
lx.grid(row=4,column=0)
xg=Tk.Entry(root)
xg.grid(row=4,column=1)
ly=Tk.Label(text="Enter y")
ly.grid(row=5,column=0)
yg=Tk.Entry(root)
yg.grid(row=5,column=1)
button1=Tk.Button(text="Go",command=_x2y2)
button1.grid(row=5, column=2)
#ax2+bx+c
la=Tk.Label(text="Enter a")
la.grid(row=6,column=0)
ag=Tk.Entry(root)
ag.grid(row=6,column=1)
lb=Tk.Label(text="Enter b")
lb.grid(row=7,column=0)
bg=Tk.Entry(root)
bg.grid(row=7,column=1)
button2=Tk.Button(text="Go",command=_x2x)
button2.grid(row=7, column=2)

root.mainloop()
