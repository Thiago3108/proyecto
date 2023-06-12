from tkinter import *

# Función para mostrar el texto o información en otro frame
def mostrar_info(texto):
    info_frame.config(text=texto)

# Crear la ventana principal
ventana = Tk()
ventana.title("Primeros Auxilios")
ventana.geometry("800x600")

# Crear el espacio para mostrar la información
info_frame = Label(ventana, text="", font=("Arial", 14), wraplength=600)
info_frame.pack(pady=20)

# Agregar imágenes
imagen1 = PhotoImage(file="fondo_v.png")
imagen2 = PhotoImage(file="fondo_v2.png")

# Botones para mostrar diferentes temas de primeros auxilios
boton1 = Button(ventana, text="Quemaduras", font=("Arial", 12), command=lambda: mostrar_info("PROTOCOLO DE ACTUACION ANTE UNA PARADA CARDIORESPIRATORIA\nEn primer lugar se deben evitar peligros tanto para el herido como para el reanimador (Proteger). A continuación valoraremos su estado de consciencia.\n1. VALORAR SU ESTADO DE CONCIENCIA\n   Arrodillado a la altura de los hombros de la persona accidentada, preguntarle qué le ocurre y sacudirle ligeramente. Si la persona está consciente, seguir pasos de la evaluación primaria y secundaria. Si la persona no responde, es decir, está inconsciente, se debe pedir ayuda de forma inmediata. Debe gritar pidiendo ayuda. Haga que alguien telefoneé al 112 e indique su situación y lo que está ocurriendo.\n2. ABRIR LA VÍA AÉREA Y VALORAR RESPIRACIÓN\n   Ante una persona inconsciente de la que sospechemos haya podido sufrir una parada cardiorrespiratoria, lo ideal es colocarla en el suelo (plano duro y horizontal), tumbada boca arriba (decúbito supino) con los brazos estirados a lo largo del cuerpo. Si la víctima es una mujer embarazada, se le colocará en la parte derecha de su espalda algún objeto (toalla, cojín, etc.), de manera que quede algo inclinada hacia la izquierda, con el objetivo de desplazar su útero para que no dificulte el retorno de la sangre por las venas que llegan al corazón cuando se está realizando la RCP.\n   Aflojar todas las ropas que puedan oprimirle y desvestir el tórax.\n   Tras gritar pidiendo ayuda, y haber colocado con cuidado a la víctima en posición de RCP, se debe abrir la vía aérea.\n   Es muy importante que el camino que debe seguir el aire desde el exterior hasta los pulmones esté despejado. Cuando una persona pierde el conocimiento, lo más probable es que su lengua ""caiga"" hacia atrás y obstruya el paso hasta los pulmones.\n   Es necesario, por tanto, realizar una maniobra de extensión del cuello inclinando hacia atrás, lo más posible, la cabeza del paciente. De esta forma, la lengua se eleva y deja libre el paso del aire. La maniobra, conocida como maniobra frente-mentón, se realiza colocando una mano en la frente de la víctima y dos dedos de la otra mano en su barbilla, y procediendo entonces a practicar una extensión máxima del cuello tirando con cuidado de la cabeza hacia atrás.\n   Además de la lengua, otros obstáculos pueden impedir el paso de aire. Debemos mirar dentro de la boca y extraer restos de comida, dentaduras postizas, etc., y si son visibles, extraer con dedos en ""gancho"". Debido a que la parada cardiorrespiratoria por atragantamiento es rara, no es necesario mirar la boca de forma rutinaria cuando se hace una RCP. Se mirará si tras iniciar la ventilación, ésta no es efectiva.\n   Una vez abierta la vía aérea, debemos comprobar si el paciente respira o no. En ocasiones, es obvio (el paciente habla o se aprecian movimientos respiratorios). En cualquier caso, lo correcto es acercar nuestra oreja y nuestra mejilla a la boca y nariz del accidentado para ""SENTIR Y ESCUCHAR"" su respiración. A la vez, nuestra mirada debe dirigirse al tórax del paciente para VER si existen movimientos respiratorios. No deben emplearse más de 10 segundos.\n   Si la víctima respira (a veces, la simple maniobra de apertura de vías es suficiente para recuperar la respiración espontánea, por ejemplo tras una sofocación), continuar la evaluación primaria y secundaria y, si sus lesiones no lo impiden, colocarla en posición lateral de seguridad hasta la llegada del personal especializado, enviar o pedir ayuda de nuevo, y revalorar periódicamente comprobando que la víctima continúa respirando con normalidad.\n3. Si el paciente no respira: CONSEGUIR AYUDA, el reanimador debe llamar al 112 si está solo o enviar a alguien. Se debe indicar que se va a iniciar la maniobra de RCP.\nCIRCULACIÓN: Según las normas ILCOR 2005, el socorrista lego (ciudadano no sanitario) no deberá buscar indicios de circulación, simplemente comenzar la maniobra de masaje cardíaco junto a la de respiración artificial.\n4. INICIAR RCP\n   En el momento de detectar una ausencia respiratoria, deben iniciarse maniobras de resucitación.\n   Lo primero que debe hacer el reanimador es dar 30 compresiones torácicas, mediante lo que se denomina como masaje cardíaco:\n   5. Recordar que la víctima debe estar sobre un plano duro.\n   6. Colocarse de rodillas a un lado de la víctima, a la altura de sus hombros.\n   7. Se sitúa el talón de la mano en el centro del pecho (donde se encuentra el punto donde se cruzarían dos líneas imaginarias que fueran, una de ellas de mamila a mamila y, otra, de nariz a ombligo), y el talón de la otra mano sobre la primera. Entrelazar los dedos y asegurarse de no aplicar presión sobre las costillas, parte superior del abdomen o parte final del esternón.\n   8. Colocar verticalmente sobre el pecho de la víctima, y con los brazos rectos, comprimir el esternón de 4 a 5 centímetros. Tras cada compresión, se debe liberar la presión sobre el pecho sin que las manos dejen de contactar con él y repetir las compresiones a un ritmo de 100 por minuto. Para no perder la cuenta, es recomendable contar en voz alta de cinco en cinco compresiones o a partir de la nº 25.\n   Tras comenzar el masaje cardíaco, el reanimador debe combinar las 30 compresiones con 2 ventilaciones de rescate.\n   Para ello, ha de abrir de nuevo la vía aérea (maniobra frente-mentón) y pinzar la nariz con los dedos índice y pulgar de la mano colocada sobre la frente del paciente, tomar una inspiración normal (Vol. Unos 500 cc.) e insuflar firmemente el aire en la boca de la víctima durante 1 seg., comprobando que el pecho se eleva. Esta técnica de respiración artificial se conoce como ventilación boca a boca. Retirar la boca de la víctima y, manteniendo la vía aérea abierta, comprobar que el pecho desciende conforme sale el aire insuflado.\n   En este caso, respiración boca a boca o sus variantes (boca a nariz sí la boca está lesionada o existía dentadura postiza; o boca a estoma en personas laringectomizados), insuflando aire directamente sobre el paciente.\n   Repetir la maniobra para aplicar, así, 2 ventilaciones de rescate efectivas.\n   Hecho esto y sin retraso, el reanimador debe colocar sus manos en el centro del pecho y dar 30 compresiones torácicas. Debe proseguir, ininterrumpidamente, combinando compresiones torácicas y ventilaciones de rescate a un ritmo de 30:2.\n   Si la primera ventilación de rescate no consigue elevar el pecho, antes del siguiente intento se debe revisar la boca de la víctima y sacar de ella cualquier cuerpo extraño, así como confirmar que la maniobra se está ejecutando correctamente.\n   Cuando la víctima es atendida por más de un reanimador, el masaje y la ventilación deben ser realizados por uno de ellos exclusivamente, que será sustituido por el otro, para evitar cansancio, aproximadamente cada 2 minutos. Este cambio se debe realizar sin interrumpir las maniobras (el primer reanimador está realizando su último ciclo de 2 ventilaciones, el segundo reanimador se coloca al lado de la víctima para aplicar las compresiones en cuanto se haya ejecutado la segunda insuflación de aire).\n   La RCP debe realizarse de forma continua hasta que: llegue la ayuda cualificada y se haga cargo de la situación, la víctima comience a respirar con normalidad, o el reanimador llegue a estar agotado.\n"))
boton1.pack(pady=10)

boton2 = Button(ventana, text="Heridas", font=("Arial", 12), command=lambda: mostrar_info("Información sobre heridas"))
boton2.pack(pady=10)

# Toplevel para almacenar números telefónicos
toplevel = Toplevel(ventana)
toplevel.title("Números Telefónicos")

# Agregar números telefónicos
telefono1 = Label(toplevel, text="123-456-7890", font=("Arial", 12))
telefono1.pack(pady=10)

telefono2 = Label(toplevel, text="987-654-3210", font=("Arial", 12))
telefono2.pack(pady=10)

# Personalizar colores
ventana.configure(bg="lightblue")
info_frame.configure(bg="lightblue")
boton1.configure(bg="white", fg="black")
boton2.configure(bg="white", fg="black")
toplevel.configure(bg="lightblue")
telefono1.configure(bg="lightblue")
telefono2.configure(bg="lightblue")

# Ejecutar la aplicación
ventana.mainloop()
