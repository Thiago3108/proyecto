from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter as ttk

#scrollbar 
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

        self.listbox.insert(tk.END, "-FASE DE ACTUACION: PAS")
        self.listbox.insert(tk.END, "-VALORACION DEL ACCIDENTADO")
        self.listbox.insert(tk.END, "-SOPORTE VITAL BASICO Y RCP BASICO")
        self.listbox.insert(tk.END, "-PROTOCOLO DE ACTUACION ANTE UNA PARADA CARDIORESPIRATORIA")
        self.listbox.insert(tk.END, "-POSICION LATERAL DE SEGURIDAD")
        self.listbox.insert(tk.END, "-PROTOCOLO DE ACTUACION ANTE UNA OBSTRUCCION DE LA VIA AEREA")
        self.listbox.insert(tk.END, "-HERIDAS")
        self.listbox.insert(tk.END, "-HEMORRAGIAS")
        self.listbox.insert(tk.END, "-AMPUTACIONES TRAUMARICAS")
        self.listbox.insert(tk.END, "-CUERPOS EXTRAÑOS")
        self.listbox.insert(tk.END, "-PICADURAS O MORDEDURAS")
        self.listbox.insert(tk.END, "-QUEMADURAS")
        self.listbox.insert(tk.END, "-CONGELACIONES")
        self.listbox.insert(tk.END, "-INSOLACIONES")
        self.listbox.insert(tk.END, "-LIPOTIMIA")
        self.listbox.insert(tk.END, "-CONVULSIONES")
        self.listbox.insert(tk.END, "-CONTUSIONES, ESQUINCES Y LUXACIONES")
        self.listbox.insert(tk.END, "-FRACTURAS")
        self.listbox.insert(tk.END, "-FRACTURAS DE CONSIDERACION IMPORTANTE")
        self.listbox.insert(tk.END, "-ACTUACION ANTE INTOXICACIONES")

        self.listbox.bind("<<ListboxSelect>>", self.on_select)  # Agregar evento de selección

    def on_select(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            if index == 0:
                self.abrir_1()
            elif index == 1:
                self.abrir_2()
            elif index == 2:
                self.abrir_3()
            elif index == 3:
                self.abrir_4()
            elif index == 4:
                self.abrir_5()
            elif index == 5:
                self.abrir_6()
            elif index == 6:
                self.abrir_7()
            elif index == 7:
                self.abrir_8()
            elif index == 8:
                self.abrir_9()
            elif index == 9:
                self.abrir_10()
            elif index == 10:
                self.abrir_11()
            elif index == 11:
                self.abrir_12()
            elif index == 12:
                self.abrir_13()
            elif index == 13:
                self.abrir_14()
            elif index == 14:
                self.abrir_15()
            elif index == 15:
                self.abrir_16()
            elif index == 16:
                self.abrir_17()
            elif index == 17:
                self.abrir_18()
            elif index == 18:
                self.abrir_19()
            elif index == 19:
                self.abrir_20()      

    def abrir_1(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"),     foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "FASE DE ACTUACION: PAS\n", "title")
        t_resultados.insert("end","PROTEGER EL LUGAR DE LOS HECHOS\nProtección del accidentado y del socorrista. Es preferible alejar el peligro que movilizar al accidentado. Hay que hacer seguro el lugar de la emergencia (señalizar, retirar peligros, iluminar…):\n·Fugas de gas: cortar el gas, no encender fuego, no fumar.\n·Coche: quitar contacto, aparcar bien, señalizarlo.\n·Electricidad: desconectar la corriente antes de tocar al accidentado.\n\nAVISAR A LOS SERVICIOS DE SOCORRO: 112\nInformar correctamente sobre:\n·Lugar exacto.\n·Tipo de accidente.\n·Número de heridos y situación.\n·Identificarse (las llamadas anónimas no inspiran confianza).\n·Colgar en último lugar.\n\nSOCORRER: APLICAR LOS CONOCIMIENTOS\n·Actuar rápidamente pero con calma.\n·Actuar siguiendo un orden de prioridades:\n\n1.Salvar la vida.\n2.Evitar que se agraven las lesiones.\n\n·Realizar maniobras sencillas encaminadas a evitar lesiones (no somos\nmédicos).\n·Como norma general no inmovilizar al accidentado. Si hubiera que\nhacerlo, moverlo en bloque.\n·Organizar: alejar a los curiosos, dar instrucciones.\n")
        t_resultados.config(state=DISABLED)

    def abrir_2(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"),     foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "VALORACION DEL ACCIDENTADO\n", "title")
        t_resultados.insert("end","En la Valoración inicial de un accidentado nos debemos marcar como objetivo prioritario el reconocimiento de lesiones o situaciones que sean potencialmente peligrosas para la vida del paciente; así mismo, hay que tener muy claro que las maniobras a realizar, se deben practicar en el lugar del accidente, salvo que concurran situaciones potencialmente peligrosas tanto para el herido como para el rescatador; como son la presencia de humos, gases, sustancias explosivas, riesgos de derrumbamiento, etc. En dichas situaciones se practicarán rescates de emergencia previos a la valoración del paciente.\n\nValoración del accidentado:\n\n·Evaluación Primaria: Se debe valorar el estado de conciencia (comprobar si responde), y valorar la respiración (oír, ver y sentir la respiración).\n\n·Evaluación Secundaria: Consiste en una exploración complementaria del paciente, para detectar otras lesiones: hemorragias, heridas, quemaduras, fracturas, etc., y aplicarles primeros auxilios hasta la llegada de los servicios médicos pertinentes.")
        t_resultados.config(state=DISABLED)
    
    def abrir_3(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"),     foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "SOPORTE VITAL BASICO Y RCP BASICO\n", "title")
        t_resultados.insert("end","En ocasiones, por diversas causas, la respiración y la circulación de una persona se interrumpen de forma brusca, inesperada y potencialmente reversible. Esa interrupción se conoce con el nombre de parada cardiorrespiratoria (PCR). \n\nSi esta situación se prolonga durante algunos minutos, la persona que la sufre muere, porque sus células dejan de recibir oxígeno y alimento. El cerebro no resiste esta situación más de 4 o 5 minuto, por este motivo es importante actuar de forma inmediata.\n\nLas maniobras de RCP básica tratan de sustituir la falta de respiración, ejecutando la ventilación artificial mediante la técnica conocida como ""ventilación boca a boca"", y la falta de latido cardíaco, ejecutando compresiones torácicas, es decir mediante el ""masaje cardíaco"".\nLa RCP básica la puede ejecutar cualquier persona entrenada sin necesidad de dispositivos especiales.\n\nEl SVB es el conjunto de actuaciones que puede ejecutar cualquier persona sin requerimientos especiales y que pretende: prevenir situaciones que puedan desencadenar una PCR o cualquier otra emergencia, conocer el sistema de emergencias y cómo activarlo de forma adecuada, y ejecutar de las propias técnicas de RCP.\n\nAnte una posible emergencia se debe seguir una secuencia de actuación que se conoce como algoritmo de soporte vital básico.")
        t_resultados.config(state=DISABLED) 

    def abrir_4(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "PROTOCOLO DE ACTUACION ANTE UNA PARADA \nCARDIORESPIRATORIA\n", "title")
        t_resultados.insert("end","\nEn primer lugar se deben evitar peligros tanto para el herido como para el reanimador (Proteger). A continuación valoraremos su estado de \nconsciencia.\n\n1. VALORAR SU ESTADO DE CONCIENCIA\n\nArrodillado a la altura de los hombros de la persona accidentada, preguntarle qué le ocurre y sacudirle ligeramente. Si la persona está consciente, seguir pasos de la evaluación primaria y secundaria. Si la persona no responde, es decir, está inconsciente, se debe pedir ayuda de forma inmediata. Debe gritar pidiendo ayuda. Haga que alguien telefoneé al 112 e indique su situación y lo que está ocurriendo.\n\n2. ABRIR LA VÍA AÉREA Y VALORAR RESPIRACIÓN\n\nAnte una persona inconsciente de la que sospechemos haya podido sufrir una parada cardiorrespiratoria, lo ideal es colocarla en el suelo (plano duro y horizontal), tumbada boca arriba (decúbito supino) con los brazos estirados a lo largo del cuerpo. Si la víctima es una mujer embarazada, se le colocará en la parte derecha de su espalda algún objeto (toalla, cojín, etc.), de manera que quede algo inclinada hacia la izquierda, con el objetivo de desplazar su útero para que no dificulte el retorno de la sangre por las venas que llegan al corazón cuando se está realizando la RCP.\n\nAflojar todas las ropas que puedan oprimirle y desvestir el tórax.\n\nTras gritar pidiendo ayuda, y haber colocado con cuidado a la víctima en posición de RCP, se debe abrir la vía aérea.\n\nEs muy importante que el camino que debe seguir el aire desde el exterior hasta los pulmones esté despejado. Cuando una persona pierde el conocimiento, lo más probable es que su lengua ""caiga"" hacia atrás y obstruya el paso hasta los pulmones.\n\nEs necesario, por tanto, realizar una maniobra de extensión del cuello inclinando hacia atrás, lo más posible, la cabeza del paciente. De esta forma, la lengua se eleva y deja libre el paso del aire. La maniobra, conocida como maniobra frente-mentón, se realiza colocando una mano en la frente de la víctima y dos dedos de la otra mano en su barbilla, y procediendo entonces a practicar una extensión máxima del cuello tirando con cuidado de la cabeza hacia atrás.\n\nAdemás de la lengua, otros obstáculos pueden impedir el paso de aire. Debemos mirar dentro de la boca y extraer restos de comida, dentaduras postizas, etc., y si son visibles, extraer con dedos en ""gancho"". Debido a que la parada cardiorrespiratoria por atragantamiento es rara, no es necesario mirar la boca de forma rutinaria cuando se hace una RCP. Se mirará si tras iniciar la ventilación, ésta no es efectiva.\n\nUna vez abierta la vía aérea, debemos comprobar si el paciente respira o no. En ocasiones, es obvio (el paciente habla o se aprecian movimientos respiratorios). En cualquier caso, lo correcto es acercar nuestra oreja y nuestra mejilla a la boca y nariz del accidentado para ""SENTIR Y ESCUCHAR"" su respiración. A la vez, nuestra mirada debe dirigirse al tórax del paciente para VER si existen movimientos respiratorios. No deben emplearse más de 10 segundos.\n\nSi la víctima respira (a veces, la simple maniobra de apertura de vías es suficiente para recuperar la respiración espontánea, por ejemplo tras una sofocación), continuar la evaluación primaria y secundaria y, si sus lesiones no lo impiden, colocarla en posición lateral de seguridad hasta la llegada del personal especializado, enviar o pedir ayuda de nuevo, y revalorar periódicamente comprobando que la víctima continúa respirando con \nnormalidad.\n\n3. Si el paciente no respira: \n\nCONSEGUIR AYUDA, el reanimador debe llamar al 112 si está solo o enviar a alguien. Se debe indicar que se va a iniciar la maniobra de RCP.\n\nCIRCULACIÓN: Según las normas ILCOR 2005, el socorrista lego (ciudadano no sanitario) no deberá buscar indicios de circulación, simplemente comenzar la maniobra de masaje cardíaco junto a la de respiración artificial.\n\n4. INICIAR RCP\nEn el momento de detectar una ausencia respiratoria, deben iniciarse maniobras de resucitación.\nLo primero que debe hacer el reanimador es dar 30 compresiones torácicas, mediante lo que se denomina como masaje cardíaco:\n\n\n5. Recordar que la víctima debe estar sobre un plano duro.\n\n6. Colocarse de rodillas a un lado de la víctima, a la altura de sus hombros.\n\n7. Se sitúa el talón de la mano en el centro del pecho (donde se \nencuentra el punto donde se cruzarían dos líneas imaginarias que fueran, una de ellas de mamila a mamila y, otra, de nariz a ombligo), y el talón de la otra mano sobre la primera. Entrelazar los dedos y asegurarse de no aplicar presión sobre las costillas, parte superior del abdomen o parte final del esternón.\n\n8. Colocar verticalmente sobre el pecho de la víctima, y con los brazos rectos, comprimir el esternón de 4 a 5 centímetros. Tras cada compresión, se debe liberar la presión sobre el pecho sin que las manos dejen de contactar con él y repetir las compresiones a un ritmo de 100 por minuto. Para no perder la cuenta, es recomendable contar en voz alta de cinco en cinco compresiones o a partir de la nº 25.\n\nTras comenzar el masaje cardíaco, el reanimador debe combinar las 30 compresiones con 2 ventilaciones de rescate.\n\nPara ello, ha de abrir de nuevo la vía aérea (maniobra frente-mentón) y pinzar la nariz con los dedos índice y pulgar de la mano colocada sobre la frente del paciente, tomar una inspiración normal (Vol. Unos 500 cc.) e insuflar firmemente el aire en la boca de la víctima durante 1 seg., comprobando que el pecho se eleva. Esta técnica de respiración artificial se conoce como ventilación boca a boca. Retirar la boca de la víctima y, manteniendo la vía aérea abierta, comprobar que el pecho desciende conforme sale el aire insuflado.\n\nEn este caso, respiración boca a boca o sus variantes (boca a nariz sí la boca está lesionada o existía dentadura postiza; o boca a estoma en personas laringectomizados), insuflando aire directamente sobre el paciente.\nRepetir la maniobra para aplicar, así, 2 ventilaciones de rescate efectivas.\nHecho esto y sin retraso, el reanimador debe colocar sus manos en el centro del pecho y dar 30 compresiones torácicas. Debe proseguir, ininterrumpidamente, combinando compresiones torácicas y ventilaciones de rescate a un ritmo de 30:2.\n\nSi la primera ventilación de rescate no consigue elevar el pecho, antes del siguiente intento se debe revisar la boca de la víctima y sacar de ella cualquier cuerpo extraño, así como confirmar que la maniobra se está ejecutando correctamente.\n\nCuando la víctima es atendida por más de un reanimador, el masaje y la ventilación deben ser realizados por uno de ellos exclusivamente, que será sustituido por el otro, para evitar cansancio, aproximadamente cada 2 minutos. Este cambio se debe realizar sin interrumpir las maniobras (el primer reanimador está realizando su último ciclo de 2 ventilaciones, el segundo reanimador se coloca al lado de la víctima para aplicar las compresiones en cuanto se haya ejecutado la segunda insuflación de aire).\n\nLa RCP debe realizarse de forma continua hasta que: llegue la ayuda cualificada y se haga cargo de la situación, la víctima comience a respirar con normalidad, o el reanimador llegue a estar agotado.\n")
        t_resultados.config(state=DISABLED)
        
        posicion_insercion = "18.1"  # Posición donde se insertará la imagen
        posicion_insercion_2= "22.0"
        posicion_insercion_3= "26.0"
        posicion_insercion_4= "40.0"
        posicion_insercion_5= "47.0"
        posicion_insercion_6= "49.0"
        # Insertar la imagen en la posición especificada
        imagen = Label(t_resultados, image=img1)
        imagen.image = fond 
        t_resultados.window_create(posicion_insercion, window=imagen)
        t_resultados.insert(posicion_insercion, "\n\n")
        #imagen no.2
        imagen_2 = Label(t_resultados, image=img2)
        imagen.image = fond_2 
        t_resultados.window_create(posicion_insercion_2, window=imagen_2)
        t_resultados.insert(posicion_insercion_2, "\n\n")

        imagen_3 = Label(t_resultados, image=img3)
        imagen.image = fond_2
        t_resultados.window_create(posicion_insercion_3, window=imagen_3)
        t_resultados.insert(posicion_insercion_3, "\n\n")

        imagen_4 = Label(t_resultados, image=img4)
        imagen.image = fond_2
        t_resultados.window_create(posicion_insercion_4, window=imagen_4)
        t_resultados.insert(posicion_insercion_4, "\n\n")

        imagen_5 = Label(t_resultados, image=img5)
        imagen.image = fond_2
        t_resultados.window_create(posicion_insercion_5, window=imagen_5)
        t_resultados.insert(posicion_insercion_5, "\n\n")

        imagen_6 = Label(t_resultados, image=img6)
        imagen.image = fond_2
        t_resultados.window_create(posicion_insercion_6, window=imagen_6)
        t_resultados.insert(posicion_insercion_5, "\n\n")


    def abrir_5(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "POSICION LATERAL DE SEGURIDAD\n", "title")
        t_resultados.insert("end","\n·Apartar el brazo que está entre el socorrista y el herido y ponerlo cerca de la cabeza.\n\n·Flexionamos la pierna más lejana del herido y acercamos la mano a la rodilla de dicha pierna sin estirarle el brazo, sino llevando la rodilla hacia el brazo.\n\n·Haciendo fuerza, hacemos girar al herido desde la rodilla y el hombro hasta que descanse sobre la rodilla flexionada, recogemos el brazo que gira externamente para darle dos puntos de soporte (rodilla y brazo).\n\n·Rectificar la posición de la cabeza para mantener la vía aérea abierta.\n\n·Le abrimos la boca para facilitar el vómito y escuchamos si se mantiene la respiración.")
        t_resultados.config(state=DISABLED)

    def abrir_6(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "PROTOCOLO DE ACTUACION ANTE UNA OBSTRUCCION DE LA VIA AEREA\n", "title")
        t_resultados.insert("end","La obstrucción de las vías respiratorias superiores es una situación de urgencia que puede ser vital si no se practican de forma inmediata las maniobras necesarias para dejar libres dichas vías.\n\nLa vía respiratoria superior comprende el tramo que va desde la cavidad bucal y las fosas nasales, pasando por la faringe laringe y tráquea.\n\nLas causas más frecuentes de obstrucción de la vía aérea se pueden resumir en dos grandes grupos:\n\n·En personas conscientes:\n\n\t-La aspiración de alimentos (atragantamiento) por \n\tdescoordinación entre la deglución y la respiración en un \n\tmomento determinado.\n\t-El paso hacia las vías respiratorias de objetos o cuerpos \n\textraños del interior de la boca como prótesis dentales, \n\tcoágulos de sangre, vómito.\n\n·En personas inconscientes:\n\n\t-La causa más frecuente de obstrucción, es la caída de la \n\tlengua hacia atrás, ocluyendo la faringe.\n\t-La obstrucción de la vía aérea puede ser completa \n\t o incompleta.\n\nHemos de comprobar la dificultad al paso del aire que presenta la persona accidentada, y una vez determinada la situación por la ausencia de movimientos respiratorios o excesivos esfuerzos para respirar procederemos a aplicar las siguientes maniobras:\n\n·En personas conscientes:\n\n\t·Si la obstrucción no es completa le animaremos a toser de \n\tforma enérgica para que expulse el cuerpo extraño.\n\n\t·Si la víctima ya no puede toser más, se le deben dar 5 golpes \n\ten la espalda, entre los omóplatos (las ""paletillas""), de forma \n\tvigorosa, seca y seguida, comprobando con cada uno de ellos \n\tsi se resuelve o no el atragantamiento. Para ello, el reanimador \n\ttiene que colocar a la víctima, estando en pie, con el tronco \n\ttligeramente inclinado hacia delante, sujetando el pecho con \n\tuna mano, y con el talón de la otra se aplican los 5 golpes \n\tinterescapulares.\n\n\t·Si a pesar de los 5 golpes en la espalda la víctima continua \n\tatragantada, es preciso aplicar compresiones abdominales, \n\thaciendo lo que se denomina maniobra de Heimlich, que \n\tconsiste en colocarnos por detrás del paciente, abrazarle de \n\tatrás a delante y cruzaremos las manos en la ""boca del \n\testómago"", dejando flexionar ligeramente al paciente. \n\n\tDe forma vigorosa aplicaremos 5 compresiones, de delante \n\tatrás y de abajo arriba. Si la víctima es muy obesa o está \n\tembarazada, las compresiones se efectuarán a nivel del pecho.\n\n\tEn caso de que las compresiones tampoco resuelvan el \n\tatragantamiento, debemos alternar golpes en la espalda y \n\tcompresiones abdominales, hasta que el problema se \n\tresuelva o la víctima pierda el conocimiento y muestre signos \n\tde que se derrumba y cae al suelo.\n\n·En personas inconscientes:\n\n\t·Si el atragantamiento es prolongado y provoca la pérdida de \n\tconocimiento, el reanimador tiene que: tender a la víctima en \n\tel suelo con cuidado, activar si no se ha hecho hasta ahora el \n\tsistema de emergencias, realizar la apertura de la vía aérea \n\t(maniobra frente-mentón) y observar dentro de la boca si el \n\tobjeto causante del atragantamiento es visible y accesible. \n\tSi es así realizar un barrido digital, es decir, con los dedos se \n\tprocede a retirar el objeto causante del atragantamiento.\n\n\t·Comenzar con la RCP, masaje y ventilaciones, a una relación \n\tde 30:2, preferentemente con la cabeza ladeada mientras se \n\thacen las compresiones, por si el objeto subiera a la boca.\n\n")
        t_resultados.config(state=DISABLED)

    def abrir_7(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "HERIDAS\n", "title")
        t_resultados.insert("end","\nUna herida es la pérdida de continuidad de la piel o de las mucosas a consecuencia de un traumatismo, provocanto la comunicación del interior con el exterior del cuerpo.\n\nActuación:\n1.Lavarse las manos.\n2.Colocarse unos guantes.\n3 Limpiar la herida con agua y jabón.\n4.Secar la herida con gasa desde el centro hacia la periferia de la misma.\n5.Desinfectar la herida con un antiséptico.\n6.Cubrirla con gasa y esparadrapo.\n7.Retirar guantes y lavarse las manos.\n8.Advertir sobre la vacunación antitetánica.\n9.Solicitar valoración sanitaria ante heridas profundas y vacunación antitetánica.\n\nQué no debo hacer:\n·Emplear algodón, pomadas, polvos, etc., sobre la herida.\n·Manipulaciones innecesarias de la herida.\n·Limpiar la herida con manos, trapos, pañuelos, sucios.")
        t_resultados.config(state=DISABLED)

    def abrir_8(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"),     foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "HEMORRAGIAS\n", "title")
        t_resultados.insert("end","\nPodemos definir hemorragia como la salida de sangre de los vasos \nsanguíneos como consecuencia de la rotura de los mismos.\n\nActuación:\n\n·Lavarse las manos.\n·Colocarse los guantes.\n·Detener la hemorragia: Si es abundante pedir ayuda al 112:\n\n1ª Opción: COMPRESIÓN DIRECTA DEL PUNTO SANGRANTE.\n\n·Comprimir directamente la zona que sangra, con gasas o pañuelos\n limpios.\n·Mantener la compresión entre 5 y 10 minutos, sin retirar nunca el \napósito.\n·Si sigue sangrando, añadir más gasas.\n·Mantener siempre el miembro elevado.\n·Sujetar las gasas con vendaje compresivo.\n\n2ª Opción: COMPRESIÓN DE LA ARTERIA SOBRE EL HUESO\n   SUBYACENTE.\n\n·Si a pesar de lo anterior, persiste la hemorragia, realizar compresión\n directa sobre la arteria correspondiente a la zona del sangrado y siempre por encima de la misma, con:\n   a) Si la hemorragia es en el brazo: Compresión con la yema de los\n dedos sobre la arteria humeral.\n   b) Si la hemorragia es en la pierna: Compresión con el talón de la mano sobre la arteria femoral.\n\nQué no hacer:\n\n·Quitar gasas empapadas.\n·Se deben evitar los torniquetes, pues al evitar completamente el paso de sangre se dañan también zonas sanas.\n\nHemorragia interna. Síntomas del shock:\n·Consciente ó no.\n·Palidez.\n·Sudoración fría.\n·Extremidades frías.\n·Labios azulados.\n·Pulso débil y acelerado.\n·Respiración superficial y acelerada.\n\nAvisar al 112 y tumbar con la cabeza más baja que las piernas (posición de trendelenburg: con las piernas más altas que el resto del cuerpo).\n\nHemorragia nasal o epistaxis:\n\n·Comprimir ligeramente la aleta nasal del lado sangrante hacia el \ntabique nasal durante 10 minutos, si no cesa continuar otros 10 minutos.\n·Si continúa, coloque una gasa o algodón empapado en agua oxigenada en la fosa nasal que sangra introduciéndola poco a poco.\n·Aplique frío local en el lado sangrante.\n·Si la hemorragia dura mas de 30 minutos acudir al centro médico más cercano.\n\n")
        t_resultados.config(state=DISABLED)

    def abrir_9(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", " AMPUTACIONES TRAUMÁTICAS\n", "title")
        t_resultados.insert("end", " \n • Actuaciones sobre la extremidad afectada:\n\n - Seguir el protocolo de actuación ante hemorragias. \n\n · El muñón debe comprimirse como se ha indicado anteriormente y luego    vendarse de forma enérgica. Si con esto no cede la hemorragia, se\n   coloca un torniquete (Con una venda ancha dar dos vueltas y en la parte   superior colocar un bolígrafo, palo, etc, y sujetarlo con la misma venda),   que se mantendrá unos 10 minutos. \n\n · Luego se retira y no se vuelve a colocar un torniquete si no reaparece \n   el sangrado. La víctima debe ser trasladada lo antes posible a un\n   centro sanitario.\n\n · Mantener el miembro elevado.\n\n • Actuaciones sobre el miembro amputado.\n\n · Envolver el miembro con gasas estériles.\n · Introducirlo en una primera bolsa y cerrarla.\n · Introducir la bolsa anterior en una segunda bolsa que contenga hielo y\n   un poco de agua.\n · Trasladar al herido y el miembro amputado de forma urgente a un \n   centro hospitalario.")
        t_resultados.config(state=DISABLED)

    def abrir_10(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", " CUERPOS EXTRAÑOS\n", "title")
        t_resultados.insert("end", "\n • EN LOS OJOS\n\n - Actuación:\n\n  ·Lavarse las manos.\n  ·Colocarse los guantes.\n  ·Localizar el cuerpo extraño y extraerlo con ayuda de una gasa estéril o     a través de lavados abundantes con suero fisiológico o, en su defecto,\n   agua.\n  ·Cubrir el ojo con gasa estéril y enviar a un centro sanitario.\n  · Si no localizamos el cuerpo extraño, lavarlo y luego proceder como en\n    el punto anterior.\n\n - Qué no hacer:\n\n ·Frotar el ojo.\n ·Usar objetos punzantes para extraer el cuerpo extraño.\n ·Realizar manipulaciones innecesarias.\n ·Manipular el ojo para extraer un cuerpo extraño que está clavado en el\n  globo ocular.\n\n • EN LA NARIZ Y EN LOS OÍDOS\n\n ·No tocarlos y acudir a un centro sanitario.\n")
        t_resultados.config(state=DISABLED)

    def abrir_11(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", " PICADURAS Y MORDEDURAS\n", "title")
        t_resultados.insert("end", "\n • Actuación:\n\n  1. Extraer el aguijón, si existiese, con ayuda de unas pinzas.\n  2. Limpiar la herida con agua y jabón.\n  3. Aplicar una gasa empapada en agua fría o hielo.\n  4. Traslado a un centro sanitario.\n  5. Si es posible, capturar al animal para descartar rabia.\n\n • Qué no hacer:\n\n · Realizar incisiones.\n · Chupar el veneno.\n · Aplicar barro, saliva, pasta de dientes u otros remedios caseros.\n · Rascarse.")
        t_resultados.config(state=DISABLED)

    def abrir_12(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"),     foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", " QUEMADURAS\n", "title")
        t_resultados.insert("end", "\n • QUEMADURAS TÉRMICAS ( POR CALOR O LLAMA)\n\n - Actuación:\n  ·Lavarse las manos.\n  ·Colocarse los guantes.\n  ·Retirar relojes, pulseras, anillos, etc.\n  ·Exponer la zona quemada bajo el chorro de agua fría durante 10\n   minutos (de reloj).\n  ·Cubrir la zona con gasas estériles, a ser posible empapadas con suero\n   fisiológico o agua.\n  ·Elevar la zona afectada.\n  ·En grandes quemados, cubrirlos con mantas.\n  ·Acudir a un centro sanitario.\n\n - Qué no hacer:\n\n ·Aplicar pomadas. Aplicar remedios caseros.\n ·Utilizar hielo o agua helada.\n ·Romper ampollas.\n ·Utilizar antisépticos con colorantes.\n ·Correr en caso de que el cuerpo esté en llamas.\n ·Arrancar la ropa pegada al cuerpo por la quemadura.\n\n• QUEMADURAS QUÍMICAS (POR PRODUCTOS QUÍMICOS)\n\n ·Quitar la ropa de la zona afectada.\n ·Lavar abundantemente con agua (ducha de cuerpo entero, ducha\n  lavaojos, grifo de lavabo, etc. según cada caso), al menos durante 20 ó    30 minutos.\n ·Acudir a un centro sanitario.\n\n • QUEMADURAS ELÉCTRICAS\n\n  1.Cortar la corriente eléctrica.\n\n  2.Aislarse al rescatar al herido:\n\n   ·Apartarlo de la corriente eléctrica con ayuda de una pértiga de material      aislante (por ejemplo el palo de madera de una escoba).\n   ·Subirse sobre algo aislante (silla de madera, caja de plástico de\n    refrescos, etc.) para rescatar al accidentado.\n\n  3.visar a los servicios sanitarios.\n\n  4.Valorar a la persona accidentada y socorrerla:\n\n   ·Reanimación cardio-pulmonar si fuera necesario, en lugar seguro.\n   ·Al valorar al herido, tener en cuenta que puede sufrir otras posibles\n     lesiones y actuar en consecuencia.")
        t_resultados.config(state=DISABLED)

    def abrir_13(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"),foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "CONGELACIONES\n\n", "title")
        t_resultados.insert("end", " Puedes tratar la congelación de primer grado volviendo a calentar la piel.  Todos los otros tipos de congelación requieren atención médica ya que     puede dañar la piel, los músculos, los huesos y otros tejidos de forma       permanente.\n\n · Calentamiento moderado con agua de la zona afectada.\n · Aflojar ropas.\n · No frotar la zona con nada.\n · Acudir a un centro sanitario.\n · Quitarse la ropa mojada\n · Proteger el área afectada para evitar una nueva exposición al frío\n · No caminar si tienes los pies congelados\n · Aliviar el dolor con un analgésico")
        t_resultados.config(state=DISABLED)

    def abrir_14(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", " INSOLACIONES\n", "title")
        t_resultados.insert("end","\n 1.Apartar a la víctima de la fuente de calor, situándolo en una\n    habitación o lugar fresco y con poca luz.\n 2.Aflojar ropas.\n 3.Aplicar compresas de agua fría.\n 4.Si está consciente, dar de beber líquidos frescos.\n 5.Consultar con los servicios sanitarios.")
        t_resultados.config(state=DISABLED)

    def abrir_15(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", " LIPOTIMIA\n", "title")
        t_resultados.insert("end", "\n Déficit transitorio del riego sanguíneo cerebral. Los síntomas son mareo,\n sudoración, pesadez, debilidad en piernas y pérdida de conocimiento de\n forma breve.\n\n - Actuación:\n\n • Ante los primeros síntomas:\n  · Sentarlo con la cabeza entre los muslos o tumbado con los miembros\n     inferiores elevados.\n  · Aflojarle la ropa.\n  · Airear el lugar y evitar curiosos.\n\n • Ante pérdida de conocimiento:\n  · P.A.S.\n  · Tumbarlo con los miembros inferiores elevados.\n  · Colocarlo en posición lateral de seguridad (PLS).\n  · Proteger tanto del frío como del calor.\n  · Vigilar constantemente al herido: respiración, pulso.\n  · Avisar a los servicios sanitarios.\n\n • Qué no hacer:\n  · Dar de beber o comer al herido.")
        t_resultados.config(state=DISABLED)

    def abrir_16(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", " CONVULSIONES\n", "title")
        t_resultados.insert("end", "\n Suelen darse en pacientes epilépticos. La epilepsia es una enfermedad\n neurológica producida por una lesión cerebral y que puede provocar \n crisis convulsivas potentes llamadas ""ataques o crisis epilépticas"".\n\n • síntomas:\n  · caída al suelo con pérdida de conciencia.\n  · ojos cerrados o entreabiertos y en blanco.\n  · boca cerrada, encajada.\n  · movimientos repetitivos e involuntarios.\n  · relajación de esfínteres.\n\n • actuación :\n\n  - Durante las convulsiones:\n   · Pedir ayuda.\n   · Retirar los objetos de alrededor que puedan dañar a la víctima.\n   · Aflojar la ropa que pueda comprimirle.\n   · Evitar que se lastime sujetando a la persona sin violencia.\n   · Proteger la cabeza.\n   · No intentar abrir la boca.\n   · Gire de lado a la víctima si presenta vómito.\n\n  - Cuando cese la crisis:\n   · Colocar al paciente en posición lateral de seguridad.\n   · Esperar hasta que llegue la asistencia sanitaria.\n\n • Qué no hacer:\n\n  · Taponar la boca.\n  · Si tiene la boca cerrada, intentar colocarle un objeto entre sus dientes.")
        t_resultados.config(state=DISABLED)

    def abrir_17(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "CONTUSIONES, ESGUINCES Y LUXACIONES\n", "title")
        t_resultados.insert("end", "\nCONTUSIÓN\n\nEs una lesión por impacto de un objeto en el cuerpo, que no produce la\npérdida de continuidad de la piel, pero puede producir lesión por debajo \nde ella y afectar a otras estructuras. Según la intensidad del impacto puede aparecer hematoma, edema y aplastamiento intenso de partes \nblandas.\n\nActuación:\n·Aplicar frío local sin contacto directo con la piel (envuelto en un\npaño).\n·Elevación del miembro si se trata de una extremidad.\n·En aplastamientos intensos debe inmovilizarse la zona afectada, como si\nse tratara de una lesión ósea.\n\nESGUINCE\nSeparación momentánea de las superficies articulares que produce una\ndistensión (o rotura) de los ligamentos. \n\nSíntomas: dolor, inflamación,impotencia funcional.\n\nActuación:\n·En las primeras 36-48 horas aplicar frío en la zona, en forma de bolsas\nfrías o compresas.\n·Reposo de la articulación mediante inmovilización.\n·Elevación de la zona lesionada. El brazo en cabestrillo y la pierna\nhorizontal.\n·Derivar a centro sanitario.\n\nLUXACIÓN\n\nEs la separación mantenida de las superficies articulares. Se produce por\nuna flexión o extensión más allá de los límites normales o bien por un\ngolpe directo en la articulación. A diferencia del esguince, las\nsuperficies articulares quedan separadas y acompañándose de desgarro o rotura de ligamentos. Se manifiesta por dolor muy intenso, hinchazón,\npérdida de fuerza y deformidad de la articulación.\n\nActuación:\n·Aplicar frío local.\n·Dejar la articulación tal y como se encuentre sin intentar corregir la\ndeformidad.\n·Inmovilizar.\n·Evacuar a centro sanitario.\n\nQué no hacer en caso de contusiones, esguinces y luxaciones:\n·Movilizar la zona o articulación dañada.\n·Intentar corregir la deformidad.\n·Aplicar pomadas o analgésicos.\n")
        t_resultados.config(state=DISABLED)

    def abrir_18(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "FRACTURAS\n", "title")
        t_resultados.insert("end", "\nDefinimos fractura como la pérdida de la continuidad de un hueso (desde simple fisura a rotura total). Pueden ser: cerradas, no producen herida en la piel, o abiertas, el hueso sale al exterior produciendo herida en la piel, \npor lo que existe peligro de infección.\n\nSíntomas: dolor intenso, deformidad, desdibujo, acortamiento, inflamación y tumefacción, impotencia funcional acusada, oyó crujido.\n\nActuación:\n·No movilizar, a menos que sea necesario.\n·No reducir la fractura, es decir, no intentar introducir fragmentos óseos \nque sobresalgan de la piel.\n·Retirar objetos que puedan oprimir debido a la inflamación de la zona \nafectada (anillos, pulseras...).\n·En fracturas cerradas aplicar frío local, protegiendo la piel (hielo envuelto en un paño).\n·Si hay que mover o trasladar a la persona accidentada, inmovilizar sin reducir la zona fracturada, incluyendo articulaciones adyacentes.\n·No realizar movimientos bruscos.\n·Si es una fractura abierta, cubrir la herida con apósitos estériles ó limpios antes de inmovilizar.\n·Pedir ayuda al 112 y traslado a centro sanitario.\n\nPara inmovilizar una fractura se deben seguir las siguientes recomendaciones:\n·Inmovilizar con material rígido (férulas) o bien con aquel material que una vez colocado haga la misma función que el rígido (pañuelos triangulares).\n·Almohadillar las férulas que se improvisen (maderas, troncos...).\n·Inmovilizar una articulación por encima y otra por debajo del punto de fractura:\n·Antebrazo: desde raíz de los dedos a axila, codo a 90° y muñeca en extensión.\n·Muñeca: desde raíz de los dedos a codo, muñeca en extensión.\n·Dedos mano: desde punta de los dedos a muñeca, dedos en semiflexión.\n·Fémur y pelvis: desde raíz de los dedos a costillas, cadera y rodillas en extensión; tobillo a 90°.\n·Tibia y peroné: desde raíz de los dedos a ingle, rodilla en extensión, tobillo a 90°.\n·Tobillo y pie: desde raíz de los dedos a rodilla, tobillo a 90°.\n·Inmovilizar en posición funcional (si se puede) y con los dedos visibles.\n·Nunca reducir una fractura (no poner el hueso en su sitio).\n·Evacuar siempre a un centro hospitalario.\n\nQué no hacer:\n·Realizar movimientos innecesarios.\n·Aplicar calor.\n·Dar pomadas, analgésicos, antiinflamatorios, etc., ya que pueden enmascarar síntomas.\n·Intentar reducir fracturas o luxaciones.\n")
        t_resultados.config(state=DISABLED)

    def abrir_19(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "FRACTURAS DE CONSIDERACIÓN IMPORTANTE\n", "title")
        t_resultados.insert("end", "\nA) FRACTURAS DE CRÁNEO\n·Se sospechará ante la observación de hemorragia nasal u ótica o salida\nde líquido transparente (líquido cefalorraquídeo).\n\nB) FRACTURAS DE COLUMNA VERTEBRAL\n·Se sospechará si la persona no puede mover alguna extremidad.\n\nActuaciones en ambas situaciones:\n·No tocar al accidentado, indicando a la persona que debe permanecer\ninmóvil. No permitir que flexione o gire el cuello. No flexionar nunca al\nherido.\n·Avisar a los servicios sanitarios, para ser trasladado en condiciones\nadecuadas. Mover siempre en bloque y en plano duro por más de una persona.\n·Permanecer a su lado, controlando consciencia, respiración y pulso.")
        t_resultados.config(state=DISABLED)

    def abrir_20(self):
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "ACTUACIÓN ANTE INTOXICACIONES\n", "title")
        t_resultados.insert("end", "Ante la sospecha de intoxicación es de vital importancia conocer el producto causante. A la persona afectada y a los compañeros, preguntarles:\n\n·¿Qué producto se ha manejado y en que cantidad?\n·¿Cuándo y durante cuanto tiempo se ha manejado?\n·¿Qué EPIs y ropa de trabajo se han empleado?\n·¿Qué tipo de síntomas se han observado?\n·¿Había tomado alcohol o alguna medicina?\n\nINGESTIÓN\n·Conocer el producto causante.\n·Llamar al Instituto Nacional de Toxicología: 91 562 04 20.\n·Avisar al 112 y trasladarle a un hospital.\n·No provocar el vómito en caso de ingestión de sustancias cáusticas., o en caso de que el herido esté inconsciente.\n·En casos excepcionales y si el paciente está consciente: administrar agua albuminosa (seis claras de huevo disuelto en un litro de agua). Dar a cucharadas, como máximo 1/2 litro.\n\nSALPICADURAS\n·Retirar toda la ropa y joyas.\n·Lavado exhaustivo con agua.\n\nSALPICADURA EN OJO\n·Lavado con agua, al menos 20 minutos, del ojo afectado.\n\nINTOXICACIÓN POR INHALACIÓN\n\n1.Protegerse/Avisar:\n·Evitar actuar solo.\n·Usar mascarillas adecuadas.\n·Si es necesario utilizar equipos autónomos.\n·Utilizar un trapo húmedo, sujetarse con una cuerda…\n·Valorar la causa de intoxicación: gases pesados y no pesados, plaguicidas, etc.\n·Avisar al Instituto Nacional de Toxicología y al 112.\n\n2.Socorrer:\n·Retirar al accidentado del ambiente tóxico.\n·Valorar nivel de conciencia y respiración, si es necesario realizar RCP.\n·Administrar oxígeno.\n·Trasladar a un centro hospitalario.")
        t_resultados.config(state=DISABLED)


def abrir_3():
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"),     foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "SOPORTE VITAL BASICO Y RCP BASICO\n", "title")
        t_resultados.insert("end","En ocasiones, por diversas causas, la respiración y la circulación de una persona se interrumpen de forma brusca, inesperada y potencialmente reversible. Esa interrupción se conoce con el nombre de parada cardiorrespiratoria (PCR). \n\nSi esta situación se prolonga durante algunos minutos, la persona que la sufre muere, porque sus células dejan de recibir oxígeno y alimento. El cerebro no resiste esta situación más de 4 o 5 minuto, por este motivo es importante actuar de forma inmediata.\n\nLas maniobras de RCP básica tratan de sustituir la falta de respiración, ejecutando la ventilación artificial mediante la técnica conocida como ""ventilación boca a boca"", y la falta de latido cardíaco, ejecutando compresiones torácicas, es decir mediante el ""masaje cardíaco"".\nLa RCP básica la puede ejecutar cualquier persona entrenada sin necesidad de dispositivos especiales.\n\nEl SVB es el conjunto de actuaciones que puede ejecutar cualquier persona sin requerimientos especiales y que pretende: prevenir situaciones que puedan desencadenar una PCR o cualquier otra emergencia, conocer el sistema de emergencias y cómo activarlo de forma adecuada, y ejecutar de las propias técnicas de RCP.\n\nAnte una posible emergencia se debe seguir una secuencia de actuación que se conoce como algoritmo de soporte vital básico.")
        t_resultados.config(state=DISABLED) 
        top.destroy()

def abrir_8():
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"),     foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "HEMORRAGIAS\n", "title")
        t_resultados.insert("end","\nPodemos definir hemorragia como la salida de sangre de los vasos \nsanguíneos como consecuencia de la rotura de los mismos.\n\nActuación:\n\n·Lavarse las manos.\n·Colocarse los guantes.\n·Detener la hemorragia: Si es abundante pedir ayuda al 112:\n\n1ª Opción: COMPRESIÓN DIRECTA DEL PUNTO SANGRANTE.\n\n·Comprimir directamente la zona que sangra, con gasas o pañuelos\n limpios.\n·Mantener la compresión entre 5 y 10 minutos, sin retirar nunca el \napósito.\n·Si sigue sangrando, añadir más gasas.\n·Mantener siempre el miembro elevado.\n·Sujetar las gasas con vendaje compresivo.\n\n2ª Opción: COMPRESIÓN DE LA ARTERIA SOBRE EL HUESO\n   SUBYACENTE.\n\n·Si a pesar de lo anterior, persiste la hemorragia, realizar compresión\n directa sobre la arteria correspondiente a la zona del sangrado y siempre por encima de la misma, con:\n   a) Si la hemorragia es en el brazo: Compresión con la yema de los\n dedos sobre la arteria humeral.\n   b) Si la hemorragia es en la pierna: Compresión con el talón de la mano sobre la arteria femoral.\n\nQué no hacer:\n\n·Quitar gasas empapadas.\n·Se deben evitar los torniquetes, pues al evitar completamente el paso de sangre se dañan también zonas sanas.\n\nHemorragia interna. Síntomas del shock:\n·Consciente ó no.\n·Palidez.\n·Sudoración fría.\n·Extremidades frías.\n·Labios azulados.\n·Pulso débil y acelerado.\n·Respiración superficial y acelerada.\n\nAvisar al 112 y tumbar con la cabeza más baja que las piernas (posición de trendelenburg: con las piernas más altas que el resto del cuerpo).\n\nHemorragia nasal o epistaxis:\n\n·Comprimir ligeramente la aleta nasal del lado sangrante hacia el \ntabique nasal durante 10 minutos, si no cesa continuar otros 10 minutos.\n·Si continúa, coloque una gasa o algodón empapado en agua oxigenada en la fosa nasal que sangra introduciéndola poco a poco.\n·Aplique frío local en el lado sangrante.\n·Si la hemorragia dura mas de 30 minutos acudir al centro médico más cercano.\n\n")
        t_resultados.config(state=DISABLED)
        top.destroy()

def abrir_6():
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "PROTOCOLO DE ACTUACION ANTE UNA OBSTRUCCION DE LA VIA AEREA\n", "title")
        t_resultados.insert("end","La obstrucción de las vías respiratorias superiores es una situación de urgencia que puede ser vital si no se practican de forma inmediata las maniobras necesarias para dejar libres dichas vías.\n\nLa vía respiratoria superior comprende el tramo que va desde la cavidad bucal y las fosas nasales, pasando por la faringe laringe y tráquea.\n\nLas causas más frecuentes de obstrucción de la vía aérea se pueden resumir en dos grandes grupos:\n\n·En personas conscientes:\n\n\t-La aspiración de alimentos (atragantamiento) por \n\tdescoordinación entre la deglución y la respiración en un \n\tmomento determinado.\n\t-El paso hacia las vías respiratorias de objetos o cuerpos \n\textraños del interior de la boca como prótesis dentales, \n\tcoágulos de sangre, vómito.\n\n·En personas inconscientes:\n\n\t-La causa más frecuente de obstrucción, es la caída de la \n\tlengua hacia atrás, ocluyendo la faringe.\n\t-La obstrucción de la vía aérea puede ser completa \n\t o incompleta.\n\nHemos de comprobar la dificultad al paso del aire que presenta la persona accidentada, y una vez determinada la situación por la ausencia de movimientos respiratorios o excesivos esfuerzos para respirar procederemos a aplicar las siguientes maniobras:\n\n·En personas conscientes:\n\n\t·Si la obstrucción no es completa le animaremos a toser de \n\tforma enérgica para que expulse el cuerpo extraño.\n\n\t·Si la víctima ya no puede toser más, se le deben dar 5 golpes \n\ten la espalda, entre los omóplatos (las ""paletillas""), de forma \n\tvigorosa, seca y seguida, comprobando con cada uno de ellos \n\tsi se resuelve o no el atragantamiento. Para ello, el reanimador \n\ttiene que colocar a la víctima, estando en pie, con el tronco \n\ttligeramente inclinado hacia delante, sujetando el pecho con \n\tuna mano, y con el talón de la otra se aplican los 5 golpes \n\tinterescapulares.\n\n\t·Si a pesar de los 5 golpes en la espalda la víctima continua \n\tatragantada, es preciso aplicar compresiones abdominales, \n\thaciendo lo que se denomina maniobra de Heimlich, que \n\tconsiste en colocarnos por detrás del paciente, abrazarle de \n\tatrás a delante y cruzaremos las manos en la ""boca del \n\testómago"", dejando flexionar ligeramente al paciente. \n\n\tDe forma vigorosa aplicaremos 5 compresiones, de delante \n\tatrás y de abajo arriba. Si la víctima es muy obesa o está \n\tembarazada, las compresiones se efectuarán a nivel del pecho.\n\n\tEn caso de que las compresiones tampoco resuelvan el \n\tatragantamiento, debemos alternar golpes en la espalda y \n\tcompresiones abdominales, hasta que el problema se \n\tresuelva o la víctima pierda el conocimiento y muestre signos \n\tde que se derrumba y cae al suelo.\n\n·En personas inconscientes:\n\n\t·Si el atragantamiento es prolongado y provoca la pérdida de \n\tconocimiento, el reanimador tiene que: tender a la víctima en \n\tel suelo con cuidado, activar si no se ha hecho hasta ahora el \n\tsistema de emergencias, realizar la apertura de la vía aérea \n\t(maniobra frente-mentón) y observar dentro de la boca si el \n\tobjeto causante del atragantamiento es visible y accesible. \n\tSi es así realizar un barrido digital, es decir, con los dedos se \n\tprocede a retirar el objeto causante del atragantamiento.\n\n\t·Comenzar con la RCP, masaje y ventilaciones, a una relación \n\tde 30:2, preferentemente con la cabeza ladeada mientras se \n\thacen las compresiones, por si el objeto subiera a la boca.\n\n")
        t_resultados.config(state=DISABLED)
        top.destroy()

def abrir_12():
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"),     foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", " QUEMADURAS\n", "title")
        t_resultados.insert("end", "\n • QUEMADURAS TÉRMICAS ( POR CALOR O LLAMA)\n\n - Actuación:\n  ·Lavarse las manos.\n  ·Colocarse los guantes.\n  ·Retirar relojes, pulseras, anillos, etc.\n  ·Exponer la zona quemada bajo el chorro de agua fría durante 10\n   minutos (de reloj).\n  ·Cubrir la zona con gasas estériles, a ser posible empapadas con suero\n   fisiológico o agua.\n  ·Elevar la zona afectada.\n  ·En grandes quemados, cubrirlos con mantas.\n  ·Acudir a un centro sanitario.\n\n - Qué no hacer:\n\n ·Aplicar pomadas. Aplicar remedios caseros.\n ·Utilizar hielo o agua helada.\n ·Romper ampollas.\n ·Utilizar antisépticos con colorantes.\n ·Correr en caso de que el cuerpo esté en llamas.\n ·Arrancar la ropa pegada al cuerpo por la quemadura.\n\n• QUEMADURAS QUÍMICAS (POR PRODUCTOS QUÍMICOS)\n\n ·Quitar la ropa de la zona afectada.\n ·Lavar abundantemente con agua (ducha de cuerpo entero, ducha\n  lavaojos, grifo de lavabo, etc. según cada caso), al menos durante 20 ó    30 minutos.\n ·Acudir a un centro sanitario.\n\n • QUEMADURAS ELÉCTRICAS\n\n  1.Cortar la corriente eléctrica.\n\n  2.Aislarse al rescatar al herido:\n\n   ·Apartarlo de la corriente eléctrica con ayuda de una pértiga de material      aislante (por ejemplo el palo de madera de una escoba).\n   ·Subirse sobre algo aislante (silla de madera, caja de plástico de\n    refrescos, etc.) para rescatar al accidentado.\n\n  3.visar a los servicios sanitarios.\n\n  4.Valorar a la persona accidentada y socorrerla:\n\n   ·Reanimación cardio-pulmonar si fuera necesario, en lugar seguro.\n   ·Al valorar al herido, tener en cuenta que puede sufrir otras posibles\n     lesiones y actuar en consecuencia.")
        t_resultados.config(state=DISABLED)
        top.destroy()

def abrir_19():
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "FRACTURAS DE CONSIDERACIÓN IMPORTANTE\n", "title")
        t_resultados.insert("end", "\nA) FRACTURAS DE CRÁNEO\n·Se sospechará ante la observación de hemorragia nasal u ótica o salida\nde líquido transparente (líquido cefalorraquídeo).\n\nB) FRACTURAS DE COLUMNA VERTEBRAL\n·Se sospechará si la persona no puede mover alguna extremidad.\n\nActuaciones en ambas situaciones:\n·No tocar al accidentado, indicando a la persona que debe permanecer\ninmóvil. No permitir que flexione o gire el cuello. No flexionar nunca al\nherido.\n·Avisar a los servicios sanitarios, para ser trasladado en condiciones\nadecuadas. Mover siempre en bloque y en plano duro por más de una persona.\n·Permanecer a su lado, controlando consciencia, respiración y pulso.")
        t_resultados.config(state=DISABLED)
        top.destroy()

def abrir_20():
        t_resultados.config(state=NORMAL)
        t_resultados.tag_configure("title", font=("Arial", 16, "bold"), foreground="blue")
        t_resultados.delete("1.0","end")
        t_resultados.insert("end", "ACTUACIÓN ANTE INTOXICACIONES\n", "title")
        t_resultados.insert("end", "Ante la sospecha de intoxicación es de vital importancia conocer el producto causante. A la persona afectada y a los compañeros, preguntarles:\n\n·¿Qué producto se ha manejado y en que cantidad?\n·¿Cuándo y durante cuanto tiempo se ha manejado?\n·¿Qué EPIs y ropa de trabajo se han empleado?\n·¿Qué tipo de síntomas se han observado?\n·¿Había tomado alcohol o alguna medicina?\n\nINGESTIÓN\n·Conocer el producto causante.\n·Llamar al Instituto Nacional de Toxicología: 91 562 04 20.\n·Avisar al 112 y trasladarle a un hospital.\n·No provocar el vómito en caso de ingestión de sustancias cáusticas., o en caso de que el herido esté inconsciente.\n·En casos excepcionales y si el paciente está consciente: administrar agua albuminosa (seis claras de huevo disuelto en un litro de agua). Dar a cucharadas, como máximo 1/2 litro.\n\nSALPICADURAS\n·Retirar toda la ropa y joyas.\n·Lavado exhaustivo con agua.\n\nSALPICADURA EN OJO\n·Lavado con agua, al menos 20 minutos, del ojo afectado.\n\nINTOXICACIÓN POR INHALACIÓN\n\n1.Protegerse/Avisar:\n·Evitar actuar solo.\n·Usar mascarillas adecuadas.\n·Si es necesario utilizar equipos autónomos.\n·Utilizar un trapo húmedo, sujetarse con una cuerda…\n·Valorar la causa de intoxicación: gases pesados y no pesados, plaguicidas, etc.\n·Avisar al Instituto Nacional de Toxicología y al 112.\n\n2.Socorrer:\n·Retirar al accidentado del ambiente tóxico.\n·Valorar nivel de conciencia y respiración, si es necesario realizar RCP.\n·Administrar oxígeno.\n·Trasladar a un centro hospitalario.")
        t_resultados.config(state=DISABLED)
        top.destroy()

# top level de numeros 

def abrir_numeros():
        global toplevel_numeros
        toplevel_numeros = Toplevel()
        toplevel_numeros.title("Numeros de Emergencia")
        toplevel_numeros.resizable(False, False)
        toplevel_numeros.geometry("520x300")
        toplevel_numeros.config(bg="light steel blue")

        #fondo del top level de quimica
        frame_fon = Label(toplevel_numeros, image= fondo_num )
        frame_fon.place(x=5,y=6)

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

################################################################
# ventana secundaria
################################################################

top = tk.Toplevel()
ventana_principal.lift()
top.title("Ventana de accion rapida")
ventana_principal.withdraw()
# ---
# ------------------------------------------------------
#Lo que va a ver en el top
#------------------------------------------------------
top.geometry("500x350")
top.resizable(False, False)
top.config(bg="aquamarine2")
usuar = StringVar()
code = StringVar()
frame_top = Frame(top)
frame_top.config(bg="aquamarine2", width=399, height=500)
frame_top.place(x=0, y=0)

def aceptar():
    top.destroy()

titulo_n = Label(top, text="Nota: ¡Hola! Te encuentras en una situación en la que tu ayuda es vital.              \n-Por favor, mantén la calma y recuerda que tus acciones marcarán la diferencia.\n-Recuerda llamar a los servicios de emergencia para obtener asistencia médica \n profesional lo antes posible.                                                                          ", anchor ="n")
titulo_n.config(bg = "lightskyblue1",fg="black", font=("italic", 10))
titulo_n.place(x=10,y=10, width=470, height=80)

bt_aceptar = Button(frame_top,text="Aceptar", command=aceptar)
bt_aceptar.place(x=200, y=140, width=100, height=30)

bt_paro_cardiaco = Button(frame_top,text="Paro Cardiaco", command=abrir_3)
bt_paro_cardiaco.place(x=50, y=100, width=100, height=30)

bt_Hemorragias = Button(frame_top,text="Hemorragia", command=abrir_8)
bt_Hemorragias.place(x=50, y=140, width=100, height=30)

bt_Asfixia = Button(frame_top,text="Asfixia", command=abrir_6)
bt_Asfixia.place(x=50, y=180, width=100, height=30)

bt_quemaduras_graves = Button(frame_top,text="Quemaduras", command=abrir_12)
bt_quemaduras_graves.place(x=50, y=220, width=100, height=30)

bt_Lesiones_oseas = Button(frame_top,text="Fracturas", command=abrir_19)
bt_Lesiones_oseas.place(x=50, y=260, width=100, height=30)

bt_alergias = Button(frame_top,text="Alergias", command=abrir_20)
bt_alergias.place(x=50, y=300, width=100, height=30)

################################################################
#Imagenes a usar
################################################################

fond = PhotoImage(file="img/fondo_v.png")
fond_2=PhotoImage(file="img/fondo_v2.png")
img1 = PhotoImage(file="img/imagen-1.png")
img2 = PhotoImage(file="img/imagen-2.png")
img3 = PhotoImage(file="img/image-3.png")
img4 = PhotoImage(file="img/image-4.png")
img5 = PhotoImage(file="img/imagen-5.png")
img6 = PhotoImage(file="img/imagen-6.png")
################################################################
# contenido
################################################################

fondo_ventana_prin = Label(ventana_principal, image= fond)
fondo_ventana_prin.place(x=0,y=0)

titulo_n = Label(ventana_principal, text="Primeros Auxilios", anchor ="w")
titulo_n.config(bg = "lightskyblue1",fg="black", font=("italic", 30))
titulo_n.place(x=10,y=10, width=980, height=100)

frame_indice = Label(fondo_ventana_prin)
frame_indice.config(bg="antiquewhite2")
frame_indice.place(x=20,y=130, width= 250, height= 545)

frame_marco_indice = Label(frame_indice)
frame_marco_indice.config(bg="white")
frame_marco_indice.place(x= 8, y =8,width=230, height=270)

listbox_frame = ListboxFrame(frame_marco_indice)
listbox_frame.pack(fill=tk.BOTH, expand=True)

frame_info = Label(fondo_ventana_prin)
frame_info.config(bg="ivory2")
frame_info.place(x=300, y = 130, width= 680, height= 550 )

num= PhotoImage(file="img/num_t (1).png")

# boton de label de notas de CALCULO 1
bt_notas = Button(frame_indice, image= num, command= abrir_numeros )
bt_notas.place(x=20, y=340)
bt_notas.config(bg = "light blue")

frame_marco_info = Label(frame_info)
frame_marco_info.config(bg="white")
frame_marco_info.place(x=10,y=10, width=660, height=530)

t_resultados = Text(frame_marco_info)
t_resultados.config(bg="azure", fg="black", font=("MuseJazz Text", 15), state=DISABLED)
t_resultados.place(x=0,y=0, width=655, height=525)

fondo_num = PhotoImage(file = "img/n_e (3) (1).png")

ventana_principal.wait_window(top)
ventana_principal.deiconify()
ventana_principal.mainloop()