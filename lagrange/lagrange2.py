import tkinter as tk
from scipy.interpolate import lagrange

root = tk.Tk()

label = tk.Label(root, text="Valores en x")
label.pack()

var1 = tk.DoubleVar()
t1 = tk.Entry(root, textvariable=var1)
t1.pack()

var2 = tk.DoubleVar()
t2 = tk.Entry(root, textvariable=var2)
t2.pack()

var3 = tk.DoubleVar()
t3 = tk.Entry(root, textvariable=var3)
t3.pack()

var4 = tk.DoubleVar()
t4 = tk.Entry(root, textvariable=var4)
t4.pack()


label1 = tk.Label(root, text="Valores en y")
label1.pack()

var5 = tk.DoubleVar()
t5 = tk.Entry(root, textvariable=var5)
t5.pack()

var6 = tk.DoubleVar()
t6 = tk.Entry(root, textvariable=var6)
t6.pack()

var7 = tk.DoubleVar()
t7 = tk.Entry(root, textvariable=var7)
t7.pack()

var8 = tk.DoubleVar()
t8 = tk.Entry(root, textvariable=var8)
t8.pack()


label2 = tk.Label(root, text="Evaluar la funcion")
label2.pack()

var9 = tk.DoubleVar()
t9 = tk.Entry(root, textvariable=var9)
t9.pack()


result = tk.DoubleVar()
l = tk.Label(root, textvariable=result)
l.pack()

# Put trace callbacks on the Entry DoubleVars
def set_label(name, index, mode):
    x = [var1.get(), var2.get(), var3.get(), var4.get()]
    y = [var5.get(), var6.get(), var7.get(), var8.get()]
    p = lagrange(x, y)
    valor = p(var9.get())
    result.set(valor)


var1.trace('w', set_label)
var2.trace('w', set_label)
var3.trace('w', set_label)
var4.trace('w', set_label)
var5.trace('w', set_label)
var6.trace('w', set_label)
var7.trace('w', set_label)
var8.trace('w', set_label)
var9.trace('w', set_label)

# Setting the vars will trigger the trace
var1.set(0.25)
var2.set(0.5)
var3.set(16)
var4.set(16)
var5.set(16)
var6.set(16)
var7.set(16)
var8.set(16)
var9.set(1)
root.mainloop()