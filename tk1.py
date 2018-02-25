# actual program

import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import sys
import math
import Tkinter as Tk

root = Tk.Tk()
root.wm_title("Embedding in TK")

f = Figure(figsize=(5, 4), dpi=100)

# DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

a = f.add_subplot(111)
a.grid(True)
c=np.linspace(-100,100,100)
b=np.linspace(-100,100,100)
A,B=np.meshgrid(c,b)

#character position without hands
def ch():
    a.plot([-100,100],[0,0],'y')
    a.plot([0,0],[-100,100],'y')
    F=((A**2))+(((B-7)**2))-49
    a.contour(A,B,F,[0])
    Z=((A**2)/7)+(((B+19)**2)/37)-10
    a.contour(A,B,Z,[0])
    a.plot([5,7,12],[-34,-59,-59],'g',[-5,-7,-12],[-34,-59,-59],'g')

 # Initial character position
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

# Character position 2
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
   
#character position 3
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
    
#y=x
def _yx():
    a.cla()
    a.set_title('y=x')
    ch()
    x=[i for i in range(-20,20)]
    y=[i for i in x]
    a.plot(x,y,'g')
    canvas.draw()
#y=x2
def _yx2():
    a.cla()
    a.set_title('y=x^2')
    ch()
    x=[i for i in range(-14,15)]
    y=[(i**2)/5 for i in x]
    a.plot(x,y,'g')
    canvas.draw()
#y=-x2
def _y_x2():
    a.cla()
    a.set_title('y=x^2')
    ch()
    x=[i for i in range(-14,15)]
    y=[-(i**2)/5 for i in x]
    a.plot(x,y,'g')
    canvas.draw()

#y=-x3
def _y_x3():
    a.cla()
    a.set_title('y=x^3')
    ch()
    x=[i for i in range(-13,14)]
    y=[-(i**3)/65 for i in x]
    a.plot(x,y,'g')
    canvas.draw()
#=x3
def _yx3():
    a.cla()
    a.set_title('y=x^3')
    ch()
    x=[i for i in range(-13,14)]
    y=[(i**3)/65 for i in x]
    a.plot(x,y,'g')
    canvas.draw()
#y=-x
def _y_x():
    a.cla()
    a.set_title('y=-x')
    ch()
    x=[i for i in range(-20,20)]
    y=[-i for i in x]
    a.plot(x,y,'g')
    canvas.draw()
#dance function
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
#y=|x|
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
#y=sin(x)
def sinx():
    a.cla()
    a.set_title('y=sin(x)')
    ch()
    x=[i for i in range(-20,21,10)]
    y=[12*(math.sin(i)) for i in x]
    a.plot(x,y,'g')
    canvas.draw()
#y=-sin(x)
def _sinx():
    a.cla()
    a.set_title('y=-sin(x)')
    ch()
    x=[i for i in range(-20,21,10)]
    y=[-12*(math.sin(i)) for i in x]
    a.plot(x,y,'g')
    canvas.draw()

 # display bar
def replaceText(text):
    display.delete(0, Tk.END)
    display.insert(0, text)
def clearText():
    replaceText("0")
def appendToDisplay(text):
    entryText = display.get()
    textLength = len(entryText)
    if entryText == "0":
        replaceText(text)
    else:
        display.insert(textLength, text)
# i dont know what it does
def _plot():
    expression = display.get()
    a.set_title(expression)
    canvas.draw()


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
def _ent():
    createWidgets()
    
ch1()
a.set_title('Mathematics is an art!')

button = Tk.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tk.TOP)
b1 = Tk.Button(master=root, text='y=x', command=_yx)
b1.pack(side=Tk.LEFT)
b3 = Tk.Button(master=root, text='y=-x', command=_y_x)
b3.pack(side=Tk.LEFT)
b6 = Tk.Button(master=root, text='y=|x|', command=_ymx)
b6.pack(side=Tk.LEFT)
b2 = Tk.Button(master=root, text='y=x^2', command=_yx2)
b2.pack(side=Tk.LEFT)
b12 = Tk.Button(master=root, text='y=-(x^2)', command=_y_x2)
b12.pack(side=Tk.LEFT)
b10 = Tk.Button(master=root, text='y=x^3', command=_yx3)
b10.pack(side=Tk.LEFT)
b11 = Tk.Button(master=root, text='y=-(x^3)', command=_y_x3)
b11.pack(side=Tk.LEFT)
b8 = Tk.Button(master=root, text='y=sin(x)', command=sinx)
b8.pack(side=Tk.LEFT)
b9 = Tk.Button(master=root, text='y=-sin(x)', command=_sinx)
b9.pack(side=Tk.LEFT)
b4 = Tk.Button(master=root, text='Dance', command=dnc)
b4.pack(side=Tk.LEFT)
b4 = Tk.Button(master=root, text='Enter your equation', command=_ent)
b4.pack(side=Tk.LEFT)

display=Tk.Entry(root, font=("Helvetica", 16), borderwidth=0, justify=Tk.RIGHT)
display.insert(0, "0")
display.pack(side=Tk.LEFT)
sevenButton = Tk.Button(master=root, font=("Helvetica", 11), text="7", borderwidth=0, command=lambda: appendToDisplay("7"))
sevenButton.pack(side=Tk.LEFT)
eightButton = Tk.Button(master=root, font=("Helvetica", 11), text="8", borderwidth=0, command=lambda: appendToDisplay("8"))
eightButton.pack(side=Tk.LEFT)
nineButton = Tk.Button(master=root, font=("Helvetica", 11), text="9", borderwidth=0, command=lambda: appendToDisplay("9"))
nineButton.pack(side=Tk.LEFT)
timesButton = Tk.Button(master=root, font=("Helvetica", 11), text="*", borderwidth=0, command=lambda: appendToDisplay("*"))
timesButton.pack(side=Tk.LEFT)


Tk.mainloop()

