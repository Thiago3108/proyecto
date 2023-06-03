from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

class ListboxFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)

        self.hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(
            self,
            xscrollcommand=self.hscrollbar.set,
            yscrollcommand=self.vscrollbar.set
        )
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.hscrollbar.config(command=self.listbox.xview)
        self.vscrollbar.config(command=self.listbox.yview)

        self.listbox.insert(tk.END, "HERIDAS")
        self.listbox.insert(tk.END, "HEMORRAGIAS")
        self.listbox.insert(tk.END, "HEMORRAGIAS222")

        self.listbox.bind("<<ListboxSelect>>", self.on_select)  # Agregar evento de selección

    def on_select(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            if index == 0:
                self.abrir_1_1()
            elif index == 1:
                self.abrir_2()

    def abrir_1_1(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "HERIDAS\n", "title")
        t_resultados.insert("end","\nUna herida es la pérdida de continuidad de la piel o de las mucosas a consecuencia de un traumatismo, provocanto la comunicación del interior con el exterior del cuerpo.\nActuación:\n1 Lavarse las manos.\n2 Colocarse unos guantes.\n3 Limpiar la herida con agua y jabón.\n4 Secar la herida con gasa desde el centro hacia la periferia de la misma.\n5 Desinfectar la herida con un antiséptico.\n6 Cubrirla con gasa y esparadrapo.\n7Retirar guantes y lavarse las manos.\n8 Advertir sobre la vacunación antitetánica.\n9 Solicitar valoración sanitaria ante heridas profundas y vacunación antitetánica.\nQué no debo hacer:\n·Emplear algodón, pomadas, polvos, etc., sobre la herida.\n·Manipulaciones innecesarias de la herida.\n·Limpiar la herida con manos, trapos, pañuelos, sucios.")
        t_resultados.config(state=DISABLED)

        posicion_insercion = "10.15"  # Posición donde se insertará la imagen
        posicion_insercion_2 = "5.0"
        # Insertar la imagen en la posición especificada
        imagen = Label(t_resultados, image=fond)
        imagen.image = fond  # Mantener una referencia a la imagen para evitar que se elimine
        t_resultados.window_create(posicion_insercion, window=imagen)
        t_resultados.insert(posicion_insercion, "\n")
        #imagen no.2
        imagen_2 = Label(t_resultados, image=fond_2)
        imagen_2.image = fond_2  # Mantener una referencia a la imagen para evitar que se elimine
        t_resultados.window_create(posicion_insercion_2, window=imagen_2)
        t_resultados.insert(posicion_insercion_2, "\n")

    def abrir_2(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"),     foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "HEMORRAGIAS\n", "title")
        t_resultados.insert("end","Podemos definir hemorragia como la salida de sangre de los vasos \nsanguíneos como consecuencia de la rotura de los mismos.\n\nActuación:\n\n·Lavarse las manos.\n·Colocarse los guantes.\n·Detener la hemorragia: Si es abundante pedir ayuda al 112:\n\n1ª Opción: COMPRESIÓN DIRECTA DEL PUNTO SANGRANTE.\n\n·Comprimir directamente la zona que sangra, con gasas o pañuelos\n limpios.\n·Mantener la compresión entre 5 y 10 minutos, sin retirar nunca el apósito.\n·Si sigue sangrando, añadir más gasas.\n·Mantener siempre el miembro elevado.\n·Sujetar las gasas con vendaje compresivo.\n\n2ª Opción: COMPRESIÓN DE LA ARTERIA SOBRE EL HUESO\n   SUBYACENTE.\n\n·Si a pesar de lo anterior, persiste la hemorragia, realizar compresión\n directa sobre la arteria correspondiente a la zona del sangrado y siempre por encima de la misma, con:\n   a) Si la hemorragia es en el brazo: Compresión con la yema de los\n dedos sobre la arteria humeral.\n   b) Si la hemorragia es en la pierna: Compresión con el talón de la mano sobre la arteria femoral.\nQué no hacer:\n·Quitar gasas empapadas.\n·Se deben evitar los torniquetes, pues al evitar completamente el paso de sangre se dañan también zonas sanas.\nHemorragia interna. Síntomas del shock:\n·Consciente ó no.\n·Palidez.\n·Sudoración fría.\n·Extremidades frías.\n·Labios azulados.\n·Pulso débil y acelerado.\n·Respiración superficial y acelerada.\nAvisar al 112 y tumbar con la cabeza más baja que las piernas (posición de trendelenburg: con las piernas más altas que el resto del cuerpo).\nHemorragia nasal o epistaxis:\n·Comprimir ligeramente la aleta nasal del lado sangrante hacia el tabique nasal durante 10 minutos, si no cesa continuar otros 10 minutos.\n·Si continúa, coloque una gasa o algodón empapado en agua oxigenada en la fosa nasal que sangra introduciéndola poco a poco.\n·Aplique frío local en el lado sangrante.\n·Si la hemorragia dura mas de 30 minutos acudir al centro médico más cercano.")
        t_resultados.config(state=DISABLED)
# ventana principal
ventana_principal = tk.Tk()

# titulo de la ventana
ventana_principal.title("Jhon Alexander Calderón Muñoz")

# tamaño de la ventana
ventana_principal.geometry("1000x700")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="khaki")

################################################################
# Imagenes a usar
################################################################

fond = PhotoImage(file="fondo_v.png")
fond_2=PhotoImage(file="fondo_v2.png")

################################################################
# contenido
################################################################

fondo_ventana_prin = Label(ventana_principal, image=fond)
fondo_ventana_prin.place(x=0,y=0)

titulo_n = Label(ventana_principal, text="Primeros Auxilios", anchor="w")
titulo_n.config(bg="blanched almond", fg="black", font=("italic", 30))
titulo_n.place(x=10, y=10, width=980, height=100)

frame_indice = Label(fondo_ventana_prin)
frame_indice.config(bg="red")
frame_indice.place(x=20, y=130, width=250, height=545)

frame_marco_indice = Label(frame_indice)
frame_marco_indice.config(bg="white")
frame_marco_indice.place(x=8, y=8, width=230, height=525)

listbox_frame = ListboxFrame(frame_marco_indice)  # Pasar la raíz como argumento
listbox_frame.pack(fill=tk.BOTH, expand=True)

frame_info = Label(fondo_ventana_prin)
frame_info.config(bg="khaki3")
frame_info.place(x=300, y=130, width=680, height=550)

frame_marco_info = Label(frame_info)
frame_marco_info.config(bg="white")
frame_marco_info.place(x=10, y=10, width=660, height=530)

t_resultados = Text(frame_marco_info)
t_resultados.config(bg="white", fg="black", font=("MuseJazz Text", 15))
t_resultados.place(x=0, y=0, width=660, height=530)

ventana_principal.mainloop()
