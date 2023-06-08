# Crear segunda ventana
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter as ttk

# ventana principal
ventana_principal = tk.Tk()

# titulo de la ventana
ventana_principal.title("Primeros auxilios")

# tamaño de la ventana
ventana_principal.geometry("1000x700")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="white")

top = tk.Toplevel()
ventana_principal.lift()
top.title("Javier Orlando Patiño Camargo ")
ventana_principal.withdraw()
# ---
# ------------------------------------------------------
#Lo que va a ver en el top
#------------------------------------------------------
top.geometry("350x300")
top.resizable(False, False)
top.config(bg="aquamarine2")
usuar = StringVar()
code = StringVar()
frame_top = Frame(top)
frame_top.config(bg="aquamarine2", width=399, height=300)
frame_top.place(x=0, y=0)


def aceptar():
    top.destroy()

bt_aceptar = Button(frame_top,text="Aceptar", command=aceptar)
bt_aceptar.place(x=100, y=220, width=100, height=30)

ventana_principal.wait_window(top)
ventana_principal.deiconify()
ventana_principal.mainloop()