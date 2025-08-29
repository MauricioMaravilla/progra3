import tkinter as tk

class Aplicacion:
    def __init__(self):
        # Crear ventana principal
        self.formulario01 = tk.Tk()
        self.formulario01.title('Operaciones')

        # Etiqueta y entrada para el primer número
        self.label01 = tk.Label(self.formulario01, text="Ingrese el primer número:")
        self.label01.grid(column=1, row=0)
        self.dato01 = tk.StringVar()
        self.entry01 = tk.Entry(self.formulario01, width=10, textvariable=self.dato01)
        self.entry01.grid(column=1, row=1)

        # Etiqueta y entrada para el segundo número
        self.label02 = tk.Label(self.formulario01, text="Ingrese el segundo número:")
        self.label02.grid(column=2, row=0)
        self.dato02 = tk.StringVar()
        self.entry02 = tk.Entry(self.formulario01, width=10, textvariable=self.dato02)
        self.entry02.grid(column=2, row=1)

        # Botones en la columna 0, uno debajo del otro
        self.boton01 = tk.Button(self.formulario01, text="Cuadrado", command=self.calcular_cuadrado)
        self.boton01.grid(column=0, row=1, padx=5, pady=2)

        self.boton02 = tk.Button(self.formulario01, text="Sumar", command=self.sumar)
        self.boton02.grid(column=0, row=2, padx=5, pady=2)

        self.boton03 = tk.Button(self.formulario01, text="Restar", command=self.restar)
        self.boton03.grid(column=0, row=3, padx=5, pady=2)

        # Etiqueta para mostrar el resultado (debajo de todo)
        self.label_resultado = tk.Label(self.formulario01, text="Resultado:")
        self.label_resultado.grid(column=1, row=4, columnspan=2)

        # Iniciar la aplicación
        self.formulario01.mainloop()

    def calcular_cuadrado(self):
        try:
            valor = int(self.dato01.get())
            cuadrado = valor * valor
            self.label_resultado.configure(text=f"Resultado: {cuadrado}")
        except ValueError:
            self.label_resultado.configure(text="Ingrese un número válido en la primera caja.")

    def sumar(self):
        try:
            valor1 = int(self.dato01.get())
            valor2 = int(self.dato02.get())
            suma = valor1 + valor2
            self.label_resultado.configure(text=f"Resultado: {suma}")
        except ValueError:
            self.label_resultado.configure(text="Ingrese números válidos en ambas cajas.")

    def restar(self):
        try:
            valor1 = int(self.dato01.get())
            valor2 = int(self.dato02.get())
            resta = valor1 - valor2
            self.label_resultado.configure(text=f"Resultado: {resta}")
        except ValueError:
            self.label_resultado.configure(text="Ingrese números válidos en ambas cajas.")

# Ejecutar la aplicación
Ejecutar = Aplicacion()
