import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Main Window")
main.config(bg="#E4E2E2")
main.geometry("700x400")


style = ttk.Style(main)
style.theme_use("clam")

radio_button_var = tk.IntVar()
style.configure("radio_button.TRadiobutton", background="#E4E2E2", foreground="#000")
style.map("radio_button.TRadiobutton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

radio_button_0 = ttk.Radiobutton(
    master=main, variable=radio_button_var, text="Rojo", value=0, style="radio_button.TRadiobutton"
)
radio_button_0.place(x=288, y=30)

radio_button_1 = ttk.Radiobutton(
    master=main, variable=radio_button_var, text="Azul", value=1, style="radio_button.TRadiobutton"
)
radio_button_1.place(x=288, y=55)

radio_button_2 = ttk.Radiobutton(
    master=main, variable=radio_button_var, text="Verde", value=2, style="radio_button.TRadiobutton"
)
radio_button_2.place(x=288, y=80)


# --- Funciones ---
def cambiar_color():
    valor = radio_button_var.get()
    if valor == 0:
        main.config(bg="violet")
    elif valor == 1:
        main.config(bg="aqua")
    elif valor == 2:
        main.config(bg="brown")
    else:
        main.config(bg="#E4E2E2")


def salir():
    main.destroy()


# --- Botones ---
style.configure("button.TButton", background="#E4E2E2", foreground="#000", cursor="heart")
style.map("button.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button = ttk.Button(master=main, text="Cambiar", style="button.TButton", command=cambiar_color)
button.place(x=287, y=142, width=80, height=40)

style.configure("button1.TButton", background="#E4E2E2", foreground="#000")
style.map("button1.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button1 = ttk.Button(master=main, text="Salir", style="button1.TButton", command=salir)
button1.place(x=289, y=199, width=80, height=40)


main.mainloop()