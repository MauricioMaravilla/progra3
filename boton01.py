import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.valor=1
        self.ventana01= tk.Tk()
        self.ventana01.title('Botones')
        self.ventana01.geometry('600x400')

        self.label01= tk.Label(self.ventana01, text=self.valor)
        self.label01.grid(column=0, row=0)
        self.label01.configure(foreground='red')

        self.boton01=tk.Button(self.ventana01, text='sumar',command=self.sumar)
        self.boton01.grid(column=0, row=1)

        self.boton02 = tk.Button(self.ventana01, text='resta', command=self.resta)
        self.boton02.grid(column=0, row=2)

        self.ventana01.mainloop()

    def sumar(self):
        self.valor=self.valor+1
        self.label01.config(text=self.valor)
    def resta(self):
        self.valor=self.valor-1
        self.label01.config(text=self.valor)

Ejecutar =  Aplicacion ()