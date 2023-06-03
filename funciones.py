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
    posicion_insercion_2= "5.0"
    # Insertar la imagen en la posición especificada
    imagen = Label(t_resultados, image=fond)
    imagen.image = fond  # Mantener una referencia a la imagen para evitar que se elimine
    t_resultados.window_create(posicion_insercion, window=imagen)
    t_resultados.insert(posicion_insercion, "\n")
    #imagen no.2
    imagen_2 = Label(t_resultados, image=fond_2)
    imagen.image = fond_2  # Mantener una referencia a la imagen para evitar que se elimine
    t_resultados.window_create(posicion_insercion_2, window=imagen_2)
    t_resultados.insert(posicion_insercion_2, "\n")
        pass

    def abrir_2(self):
        # Código para abrir_2
        # ...
        pass


root = tk.Tk()
root.title("Lista con barras de desplazamiento")
root.geometry("400x300")
listbox_frame = ListboxFrame(root)  # Pasar la raíz como argumento
listbox_frame.pack(fill=tk.BOTH, expand=True)
root.mainloop()
