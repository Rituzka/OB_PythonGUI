import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.geometry("175x175")


select = tkinter.StringVar()
labelsel = ttk.Label(window, text=" ")
labelsel.grid(column=0, row=10, sticky=tkinter.W)


def mostrarseleccion(value):
    labelsel.configure(text=value)


def reiniciar(value, label):
    value.set(None)
    label.configure(text=' ')


r1 = ttk.Radiobutton(window, text='Casado/a', value='Casado/a', variable=select, command=lambda: mostrarseleccion(select.get()))
r2 = ttk.Radiobutton(window, text='Soltero/a', value='Soltero/a', variable=select, command=lambda: mostrarseleccion(select.get()))
r3 = ttk.Radiobutton(window, text='Viudo/a', value='Viudo/a', variable=select, command=lambda: mostrarseleccion(select.get()))
r4 = ttk.Radiobutton(window, text='Pareja de hecho', value='En Pareja', variable=select, command=lambda: mostrarseleccion(select.get()))

r1.grid(column=0, row=2, sticky=tkinter.W)
r2.grid(column=0, row=3, sticky=tkinter.W)
r3.grid(column=0, row=4, sticky=tkinter.W)
r4.grid(column=0, row=5, sticky=tkinter.W)

b2 = ttk.Button(window, text='Reiniciar', command=lambda: reiniciar(select, labelsel))
b2.grid(column=0, row=9, sticky=tkinter.W)

window.mainloop()
