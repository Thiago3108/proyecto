from tkinter import *
from tkinter import messagebox
import tkinter as tk


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
#Imagenes a usar
################################################################

fond = PhotoImage(file="fondo_v.png")
fond_2=PhotoImage(file="fondo_v2.png")


fondo_ventana_prin = Label(ventana_principal, image= fond)
fondo_ventana_prin.place(x=0,y=0)

titulo_n = Label(ventana_principal, text="Primeros Auxilios", anchor ="w")
titulo_n.config(bg = "blanched almond",fg="black", font=("italic", 30))
titulo_n.place(x=10,y=10, width=980, height=100)

frame_indice = Label(fondo_ventana_prin)
frame_indice.config(bg="red")
frame_indice.place(x=20,y=130, width= 250, height= 545)

frame_marco_indice = Label(frame_indice)
frame_marco_indice.config(bg="white")
frame_marco_indice.place(x= 8, y =8,width=230, height=525  )

frame_info = Label(fondo_ventana_prin)
frame_info.config(bg="khaki3")
frame_info.place(x=300, y = 130, width= 680, height= 550 )

frame_marco_info = Label(frame_info)
frame_marco_info.config(bg="white")
frame_marco_info.place(x=10,y=10, width=660, height=530)

t_resultados = Text(frame_marco_info)
t_resultados.config(bg="white", fg="black", font=("MuseJazz Text", 15))
t_resultados.place(x=0,y=0, width=660, height=530)

#desplazamiento 

# scroll=Scrollbar(frame_marco_indice)
# texto= tk.Text(frame_marco_indice,height=0,width=0)

# # Crear un widget asociado al desplazamiento (p. ej., un Text)
# botones = Text(frame_marco_indice, yscrollcommand=scroll.set)
# botones.place(x=5, y= 20)
# botones.config(width=10)

# # Configurar la barra de desplazamiento para desplazarse con el widget asociado
# scroll.config(command=botones.yview)

####

def abrir_1_1():
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

boton1 = Button(frame_marco_indice, text="HERIDAS", command= abrir_1_1)
boton1.place(x=0,y=0, width=230,height=40)
boton1.config(bg= "khaki3")

def abrir_2():
    t_resultados.config(state=NORMAL)
    t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
    t_resultados.delete("1.0","end")
    t_resultados.insert("end", "HEMORRAGIAS\n", "title")
    t_resultados.insert("end","Podemos definir hemorragia como la salida de sangre de los vasos \nsanguíneos como consecuencia de la rotura de los mismos.\n\nActuación:\n\n·Lavarse las manos.\n·Colocarse los guantes.\n·Detener la hemorragia: Si es abundante pedir ayuda al 112:\n\n1ª Opción: COMPRESIÓN DIRECTA DEL PUNTO SANGRANTE.\n\n·Comprimir directamente la zona que sangra, con gasas o pañuelos\n limpios.\n·Mantener la compresión entre 5 y 10 minutos, sin retirar nunca el apósito.\n·Si sigue sangrando, añadir más gasas.\n·Mantener siempre el miembro elevado.\n·Sujetar las gasas con vendaje compresivo.\n\n2ª Opción: COMPRESIÓN DE LA ARTERIA SOBRE EL HUESO\n   SUBYACENTE.\n\n·Si a pesar de lo anterior, persiste la hemorragia, realizar compresión\n directa sobre la arteria correspondiente a la zona del sangrado y siempre por encima de la misma, con:\n   a) Si la hemorragia es en el brazo: Compresión con la yema de los\n dedos sobre la arteria humeral.\n   b) Si la hemorragia es en la pierna: Compresión con el talón de la mano sobre la arteria femoral.\nQué no hacer:\n·Quitar gasas empapadas.\n·Se deben evitar los torniquetes, pues al evitar completamente el paso de sangre se dañan también zonas sanas.\nHemorragia interna. Síntomas del shock:\n·Consciente ó no.\n·Palidez.\n·Sudoración fría.\n·Extremidades frías.\n·Labios azulados.\n·Pulso débil y acelerado.\n·Respiración superficial y acelerada.\nAvisar al 112 y tumbar con la cabeza más baja que las piernas (posición de trendelenburg: con las piernas más altas que el resto del cuerpo).\nHemorragia nasal o epistaxis:\n·Comprimir ligeramente la aleta nasal del lado sangrante hacia el tabique nasal durante 10 minutos, si no cesa continuar otros 10 minutos.\n·Si continúa, coloque una gasa o algodón empapado en agua oxigenada en la fosa nasal que sangra introduciéndola poco a poco.\n·Aplique frío local en el lado sangrante.\n·Si la hemorragia dura mas de 30 minutos acudir al centro médico más cercano.")
    t_resultados.config(state=DISABLED)

boton2 = Button(frame_marco_indice, text="HEMORRAGIAS", command= abrir_2)
boton2.place( x=0,y=40, width=230,height=40)
boton2.config(bg= "khaki3")

def abrir_3():
    t_resultados.config(state=NORMAL)
    t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
    t_resultados.delete("1.0","end")
    t_resultados.insert("end", "AMPUTACIONES TRAUMÁTICAS\n", "title")
    t_resultados.insert("end", "Actuaciones sobre la extremidad afectada:\n·Seguir el protocolo de actuación ante hemorragias. \nEl muñón debe comprimirse como se ha indicado anteriormente y luego vendarse de forma enérgica. Si con esto no cede la hemorragia, se coloca un torniquete (Con una venda ancha dar dos vueltas y en la parte superior colocar un\nbolígrafo, palo, etc., y sujetarlo con la misma venda) , que se mantendrá unos 10 minutos. Luego se retira y no se vuelve a colocar un torniquete si no reaparece el sangrado. La víctima debe ser trasladada lo antes posible a un centro sanitario.\n·Mantener el miembro elevado.\n·Actuaciones sobre el miembro amputado.\n1.Envolver el miembro con gasas estériles.\n2.Introducirlo en una primera bolsa y cerrarla.\n3.Introducir la bolsa anterior en una segunda bolsa que contenga hielo y un poco de agua.\n·Trasladar al herido y el miembro amputado de forma urgente a un centro hospitalario.")
    t_resultados.config(state=DISABLED)


boton3 = Button(frame_marco_indice, text="AMPUTACIONES TRAUMÁTICAS", command= abrir_3)
boton3.place( x=0,y=80, width=230,height=40)
boton3.config(bg= "khaki3")

def abrir_4():
    t_resultados.config(state=NORMAL)
    t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
    t_resultados.delete("1.0","end")
    t_resultados.insert("end", "CUERPOS EXTRAÑOS\n", "title")
    t_resultados.insert("end", "\nEN LOS OJOS\nActuación:\n·Lavarse las manos.\n·Colocarse los guantes.\n·Localizar el cuerpo extraño y extraerlo con ayuda de una gasa estéril o\na través de lavados abundantes con suero fisiológico o, en su defecto,\n agua.\n·Cubrir el ojo con gasa estéril y enviar a un centro sanitario.\n· Si no localizamos el cuerpo extraño, lavarlo y luego proceder como en\nel punto anterior.\nQué no hacer:\n·Frotar el ojo.\n·Usar objetos punzantes para extraer el cuerpo extraño.\n·Realizar manipulaciones innecesarias.\n·Manipular el ojo para extraer un cuerpo extraño que está clavado en el\nglobo ocular.\nEN LA NARIZ Y EN LOS OÍDOS\nNo tocarlos y acudir a un centro sanitario.")
    t_resultados.config(state=DISABLED)

boton4 = Button(frame_marco_indice, text="CUERPOS EXTRAÑOS", command= abrir_4)
boton4.place( x=0,y=120, width=230,height=40)
boton4.config(bg= "khaki3")

def abrir_5():
    t_resultados.config(state=NORMAL)
    t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
    t_resultados.delete("1.0","end")
    t_resultados.insert("end", "PICADURAS Y MORDEDURAS\n", "title")
    t_resultados.insert("end", "\nActuación :\n1.	Extraer el aguijón, si existiese, con ayuda de unas pinzas.\n2.	Limpiar la herida con agua y jabón.\n3.	Aplicar una gasa empapada en agua fría o hielo.\n4.	Traslado a un centro sanitario.\n5.	Si es posible, capturar al animal para descartar rabia.\nQué no hacer:\n· Realizar incisiones.\n· Chupar el veneno.\n· Aplicar barro, saliva, pasta de dientes u otros remedios caseros.\n· Rascarse.")
    t_resultados.config(state=DISABLED)

boton5 = Button(frame_marco_indice, text="PICADURAS Y MORDEDURAS", command= abrir_5)
boton5.place( x=0,y=160, width=230,height=40)
boton5.config(bg= "khaki3")

def abrir_6():
    t_resultados.config(state=NORMAL)
    t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
    t_resultados.delete("1.0","end")
    t_resultados.insert("end", "QUEMADURAS\n", "title")
    t_resultados.insert("end", "\nQUEMADURAS TÉRMICAS ( POR CALOR O LLAMA)\nActuación:\n·	Lavarse las manos.\n·Colocarse los guantes.\n·Retirar relojes, pulseras, anillos, etc.\n·Exponer la zona quemada bajo el chorro de agua fría durante 10 minutos\n(de reloj).\n·Cubrir la zona con gasas estériles, a ser posible empapadas con suero\nfisiológico o agua.\n·Elevar la zona afectada.\n·	En grandes quemados, cubrirlos con mantas.\n·Acudir a un centro sanitario.\nQué no hacer:\n·Aplicar pomadas. Aplicar remedios caseros.\n·Utilizar hielo o agua helada.\n·Romper ampollas.\n·Utilizar antisépticos con colorantes.\n·Correr en caso de que el cuerpo esté en llamas.\n·Arrancar la ropa pegada al cuerpo por la quemadura.\nQUEMADURAS QUÍMICAS (POR PRODUCTOS QUÍMICOS)\n·Quitar la ropa de la zona afectada.\n·Lavar abundantemente con agua (ducha de cuerpo entero, ducha lavaojos,\ngrifo de lavabo, etc. según cada caso), al menos durante 20 ó 30 minutos.\n·Acudir a un centro sanitario.\nQUEMADURAS ELÉCTRICAS\n1.Cortar la corriente eléctrica.\n2.	Aislarse al rescatar al herido:\n·Apartarlo de la corriente eléctrica con ayuda de una pértiga de\nmaterial aislante (por ejemplo el palo de madera de una escoba).\nSubirse sobre algo aislante (silla de madera, caja de plástico de\nrefrescos, etc.) para rescatar al accidentado.\n1.visar a los servicios sanitarios.\n2.	Valorar a la persona accidentada y socorrerla:\n·Reanimación cardio-pulmonar si fuera necesario, en lugar seguro.\n·Al valorar al herido, tener en cuenta que puede sufrir otras posibles\nlesiones y actuar en consecuencia.")
    t_resultados.config(state=DISABLED)


boton6 = Button(frame_marco_indice, text="QUEMADURAS", command= abrir_6)
boton6.place( x=0,y=200, width=230,height=40)
boton6.config(bg= "khaki3")

def abrir_7():
    t_resultados.config(state=NORMAL)
    t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
    t_resultados.delete("1.0","end")
    t_resultados.insert("end", "CONGELACIONES\n", "title")
    t_resultados.insert("end", "\n·	Calentamiento moderado con agua de la zona afectada.\n·	Aflojar ropas.\n·	No frotar la zona con nada.\n·	Acudir a un centro sanitario.")
    t_resultados.config(state=DISABLED)



boton7 = Button(frame_marco_indice, text="CONGELACIONES", command= abrir_7)
boton7.place( x=0,y=240, width=230,height=40)
boton7.config(bg= "khaki3")

def abrir_8():
    t_resultados.config(state=NORMAL)
    t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
    t_resultados.delete("1.0","end")
    t_resultados.insert("end", "INSOLACIONES\n", "title")
    t_resultados.insert("end", "\n1.Apartar a la víctima de la fuente de calor, situándolo en una\nhabitación o lugar fresco y con poca luz.\n2.Aflojar ropas.\n3.	Aplicar compresas de agua fría.\n4.	Si está consciente, dar de beber líquidos frescos.\n5.	Consultar con los servicios sanitarios.")
    t_resultados.config(state=DISABLED)


boton8 = Button(frame_marco_indice, text="INSOLACIONES", command= abrir_8)
boton8.place( x=0,y=280, width=230,height=40)
boton8.config(bg= "khaki3")

def abrir_9():
    t_resultados.config(state=NORMAL)
    t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
    t_resultados.delete("1.0","end")
    t_resultados.insert("end", "LIPOTIMIA\n", "title")
    t_resultados.insert("end", "\nDéficit transitorio del riego sanguíneo cerebral. Los síntomas son mareo,\nsudoración, pesadez, debilidad en piernas y pérdida de conocimiento de\nforma breve.\nActuación:\n·	A) Ante los primeros síntomas:\n·	Sentarlo con la cabeza entre los muslos o tumbado con los miembros\ninferiores elevados.\n·	Aflojarle la ropa.\n·	Airear el lugar y evitar curiosos.\n·	B) Ante pérdida de conocimiento:\n·	P.A.S.\n·	Tumbarlo con los miembros inferiores elevados.\n·	Colocarlo en posición lateral de seguridad (PLS).\n·	Proteger tanto del frío como del calor.\n·	Vigilar constantemente al herido: respiración, pulso.\n·	Avisar a los servicios sanitarios.\nQué no hacer:\n·	Dar de beber o comer al herido.")
    t_resultados.config(state=DISABLED)


boton9 = Button(frame_marco_indice, text="LIPOTIMIA", command= abrir_9)
boton9.place( x=0,y=320, width=230,height=40)
boton9.config(bg= "khaki3")

def abrir_10():
    t_resultados.config(state=NORMAL)
    t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
    t_resultados.delete("1.0","end")
    t_resultados.insert("end", "CONVULSIONES\n", "title")
    t_resultados.insert("end", "\nSuelen darse en pacientes epilépticos. La epilepsia es una enfermedadneurológica producida por una lesión cerebral y que puede provocar crisis\nconvulsivas potentes llamadas ""ataques o crisis epilépticas"". Los signos y\nsíntomas que presenta son: caída al suelo con pérdida de conciencia, ojos cerrados o entreabiertos y en blanco, boca cerrada, encajada, convulsiones (movimientos repetitivos e involuntarios) y en ocasión relajación de\nesfínteres.\nLa actuación a seguir en estos casos es:\n·Durante las convulsiones:\n·Pedir ayuda.\n·Retirar los objetos de alrededor que puedan dañar a la víctima.\n·Aflojar la ropa que pueda comprimirle.\n·Evitar que se lastime sujetando a la persona sin violencia. Proteger la\ncabeza.\n·No intentar abrir la boca.\n·Gire de lado a la víctima si presenta vómito.\n·Cuando cese la crisis:\n·Colocar al paciente en posición lateral de seguridad.\n·	Esperar hasta que llegue la asistencia sanitaria.\nQué no hacer:\n·Taponar la boca.\n·Si tiene la boca cerrada, intentar colocarle un objeto entre sus dientes.")
    t_resultados.config(state=DISABLED)


boton10 = Button(frame_marco_indice, text="CONVULSIONES", command= abrir_10)
boton10.place( x=0,y=360, width=230,height=40)
boton10.config(bg= "khaki3")

def abrir_11():
    t_resultados.config(state=NORMAL)
    t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
    t_resultados.delete("1.0","end")
    t_resultados.insert("end", "CONTUSIONES, ESGUINCES Y LUXACIONES\n", "title")
    t_resultados.insert("end", "\nCONTUSIÓN\nEs una lesión por impacto de un objeto en el cuerpo, que no produce la\npérdida de continuidad de la piel, pero puede producir lesión por debajo de\nella y afectar a otras estructuras. Según la intensidad del impacto puede\naparecer hematoma, edema y aplastamiento intenso de partes blandas.\nActuación:\n·Aplicar frío local sin contacto directo con la piel (envuelto en un\npaño).\n·Elevación del miembro si se trata de una extremidad.\n·En aplastamientos intensos debe inmovilizarse la zona afectada, como si\nse tratara de una lesión ósea.\nESGUINCE\nSeparación momentánea de las superficies articulares que produce una\ndistensión (o rotura) de los ligamentos. Síntomas: dolor, inflamación,\nimpotencia funcional.\nActuación:\n·En las primeras 36-48 horas aplicar frío en la zona, en forma de bolsas\nfrías o compresas.\n·	Reposo de la articulación mediante inmovilización.\n·Elevación de la zona lesionada. El brazo en cabestrillo y la pierna\nhorizontal.\n·Derivar a centro sanitario.\nLUXACIÓN\nEs la separación mantenida de las superficies articulares. Se produce por\nuna flexión o extensión más allá de los límites normales o bien por un\ngolpe directo en la articulación. A diferencia del esguince, las\nsuperficies articulares quedan separadas y acompañándose de desgarro o\nrotura de ligamentos. Se manifiesta por dolor muy intenso, hinchazón,\npérdida de fuerza y deformidad de la articulación.\nActuación:\n·Aplicar frío local.\n·Dejar la articulación tal y como se encuentre sin intentar corregir la\ndeformidad.\n·Inmovilizar.\n·Evacuar a centro sanitario.\nQué no hacer en caso de contusiones, esguinces y luxaciones:\n·Movilizar la zona o articulación dañada.\n·Intentar corregir la deformidad.\n·	Aplicar pomadas o analgésicos.")

    t_resultados.config(state=DISABLED)


boton11 = Button(frame_marco_indice, text="CONTUSIONES, ESGUINCES Y LUXACIONES", command= abrir_11)
boton11.place( x=0,y=400, width=230,height=40)
boton11.config(bg= "khaki3")

def abrir_12():
    t_resultados.config(state=NORMAL)
    t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
    t_resultados.delete("1.0","end")
    t_resultados.insert("end", "FRACTURAS\n", "title")
    t_resultados.insert("end", "\nDefinimos fractura como la pérdida de la continuidad de un hueso (desde\nsimple fisura a rotura total). Pueden ser: cerradas, no producen herida en\nla piel, o abiertas, el hueso sale al exterior produciendo herida en la\npiel, por lo que existe peligro de infección.\nSíntomas: dolor intenso, deformidad, desdibujo, acortamiento, inflamación y\ntumefacción, impotencia funcional acusada, oyó crujido.\nActuación:\n·	No movilizar, a menos que sea necesario.\n·	No reducir la fractura, es decir, no intentar introducir fragmentos\nóseos que sobresalgan de la piel.\n·	Retirar objetos que puedan oprimir debido a la inflamación de la zona\nafectada (anillos, pulseras...).\n·	En fracturas cerradas aplicar frío local, protegiendo la piel (hielo\nenvuelto en un paño).\n·	Si hay que mover o trasladar a la persona accidentada, inmovilizar sin\nreducir la zona fracturada, incluyendo articulaciones adyacentes.\n·	No realizar movimientos bruscos.\n·	Si es una fractura abierta, cubrir la herida con apósitos estériles ó\nlimpios antes de inmovilizar.\n·	Pedir ayuda al 112 y traslado a centro sanitario.\nPara inmovilizar una fractura se deben seguir las siguientes\nrecomendaciones:\n·	Inmovilizar con material rígido (férulas) o bien con aquel material que\nuna vez colocado haga la misma función que el rígido (pañuelos\ntriangulares).\n·	Almohadillar las férulas que se improvisen (maderas, troncos...).\n·	Inmovilizar una articulación por encima y otra por debajo del punto de\nfractura:\n·	Antebrazo: desde raíz de los dedos a axila, codo a 90° y muñeca en\nextensión.\n·	Muñeca: desde raíz de los dedos a codo, muñeca en extensión.\n·	Dedos mano: desde punta de los dedos a muñeca, dedos en semiflexión.\n·	Fémur y pelvis: desde raíz de los dedos a costillas, cadera y rodillas\nen extensión; tobillo a 90°.\n·	Tibia y peroné: desde raíz de los dedos a ingle, rodilla en extensión,\ntobillo a 90°.\n·	Tobillo y pie: desde raíz de los dedos a rodilla, tobillo a 90°.\n·	Inmovilizar en posición funcional (si se puede) y con los dedos\nvisibles.\n·	Nunca reducir una fractura (no poner el hueso en su sitio).\n·	Evacuar siempre a un centro hospitalario.\nQué no hacer:\n·	Realizar movimientos innecesarios.\n·	Aplicar calor.\n·	Dar pomadas, analgésicos, antiinflamatorios, etc., ya que pueden\nenmascarar síntomas.\n·	Intentar reducir fracturas o luxaciones.")
    t_resultados.config(state=DISABLED)


boton12 = Button(frame_marco_indice, text="FRACTURAS", command= abrir_12)
boton12.place( x=0,y=440, width=230,height=40)
boton12.config(bg= "khaki3")

def abrir_13():
    t_resultados.config(state=NORMAL)
    t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
    t_resultados.delete("1.0","end")
    t_resultados.insert("end", "FRACTURAS DE CONSIDERACIÓN IMPORTANTE\n", "title")
    t_resultados.insert("end", "\nA) FRACTURAS DE CRÁNEO\n·Se sospechará ante la observación de hemorragia nasal u ótica o salida\nde líquido transparente (líquido cefalorraquídeo).\nB) FRACTURAS DE COLUMNA VERTEBRAL\n·Se sospechará si la persona no puede mover alguna extremidad.\nActuaciones en ambas situaciones:\n·No tocar al accidentado, indicando a la persona que debe permanecer\ninmóvil. No permitir que flexione o gire el cuello. No flexionar nunca al\nherido.\n·Avisar a los servicios sanitarios, para ser trasladado en condiciones\nadecuadas. Mover siempre en bloque y en plano duro por más de una persona.\n·Permanecer a su lado, controlando consciencia, respiración y pulso.")
    t_resultados.config(state=DISABLED)


boton13 = Button(frame_marco_indice, text="FRACTURAS DE CONSIDERACIÓN IMPORTANTE", command= abrir_13)
boton13.place( x=0,y=480, width=230,height=40)
boton13.config(bg= "khaki3")

ventana_principal.mainloop()