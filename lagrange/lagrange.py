from tkinter import *

##instancia de tkinter
window = Tk()

window.title("Lagrange bola")
v = IntVar()


Radiobutton(window,
              text="1",
              padx = 20,
              variable=v,
              value=1).pack(anchor=W)
Radiobutton(window,
              text="2",
              padx = 20,
              variable=v,
              value=2).pack(anchor=W)
Radiobutton(window,
              text="3",
              padx = 20,
              variable=v,
              value=3).pack(anchor=W)
Radiobutton(window,
              text="4",
              padx = 20,
              variable=v,
              value=4).pack(anchor=W)


# def cuadrados(x):
#     a = Entry(window, width=50, borderwidth = 5)
#     b = Entry(window, width=50, borderwidth = 5)
#     c = Entry(window, width=50, borderwidth = 5)
#     d = Entry(window, width=50, borderwidth = 5)
#     a.pack()
#     b.pack()
#     c.pack()
#     d.pack()
#
#
# def click():
#
#     myLabel = Label(window, text="Poner valores de X")
#     myLabel.pack()
#     varA = DoubleVar()
#     varB = DoubleVar()
#     varC = DoubleVar()
#     varD = DoubleVar()
#     a = Entry(window, width=50, borderwidth=5 ,textvariable = varA)
#     b = Entry(window, width=50, borderwidth=5 ,textvariable = varB)
#     c = Entry(window, width=50, borderwidth=5 ,textvariable = varC)
#     d = Entry(window, width=50, borderwidth=5 ,textvariable = varD)
#
#     a.pack()
#     b.pack()
#     c.pack()
#     d.pack()
#
#     myLabel = Label(window, text ="Poner valores de Y")
#     myLabel.pack()
#     e = Entry(window, width=50, borderwidth=5)
#     f = Entry(window, width=50, borderwidth=5)
#     g = Entry(window, width=50, borderwidth=5)
#     h = Entry(window, width=50, borderwidth=5)
#     e.pack()
#     f.pack()
#     g.pack()
#     h.pack()
#
#     varA.trace('w')
#     varB.trace('w')
#     m = lambda x,y : x + y
#     m(varA.get(),varB.get())
#
def cambio():
    print("cambio su valor")

def click():
    label = Label(window, text=v.get())
    label.pack()


v.trace('w',cambio())


myButton = Button(window, text="Calcular", command=click())
myButton.pack()


##siempre va al final
window.mainloop()
