import tkinter as tk
from datetime import date
from tkinter import messagebox

def calcular_edad():
    try:
        anio = int(entry_anio.get())
        mes = int(entry_mes.get())
        dia = int(entry_dia.get())

        hoy = date.today()
        nacimiento = date(anio, mes, dia)
        edad = hoy.year - nacimiento.year

        # Verificar si ya cumplió años este año
        if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
            edad -= 1

        messagebox.showinfo("Resultado", f"Tienes {edad} años.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Edad")
ventana.geometry("300x200")

# Etiquetas y entradas
tk.Label(ventana, text="Año de nacimiento:").pack(pady=5)
entry_anio = tk.Entry(ventana)
entry_anio.pack()

tk.Label(ventana, text="Mes de nacimiento:").pack(pady=5)
entry_mes = tk.Entry(ventana)
entry_mes.pack()

tk.Label(ventana, text="Día de nacimiento:").pack(pady=5)
entry_dia = tk.Entry(ventana)
entry_dia.pack()

# Botón para calcular
btn_calcular = tk.Button(ventana, text="Calcular Edad", command=calcular_edad)
btn_calcular.pack(pady=10)

ventana.mainloop()