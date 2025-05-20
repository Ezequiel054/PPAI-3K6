from tkinter import *
from tkinter import messagebox,ttk,simpledialog,font
from datetime import datetime
from tkcalendar import Calendar, DateEntry
from tkinter.ttk import Combobox

class PantallaRegRevisionManual():
    def __new__(cls):
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self):
        pass
    
    # Esta función crea una ventana de interfaz gráfica con un botón para generar un reporte de ranking de vinos.
    def opcionRegResultadoDeRevisiónManual(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Red Sísmica")
        self.root.resizable(False, False)

        self.root.configure(bg="#050c57")

        self.cerrar_presionado = False

        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        self.boton = Button(self.root, text="Registrar resultado de revisión manual", font=mi_tipo_de_letra, command=self.root.quit)
        self.boton.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.boton.config(height=3, width=35) 
        self.boton.place(relx=0.5, rely=0.5, anchor="center")

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        center_window(self.root)
        self.root.mainloop()

        if self.cerrar_presionado:
            return True
        else:return False

    def habilitar_pantalla(self):
        pass
    
    # Esta función crea una ventana de interfaz gráfica para seleccionar un rango de fechas "Desde" y "Hasta".
    # Permite al usuario seleccionar las fechas, validar el periodo, y confirmar su selección.
    # Retorna True si se presiona el botón de cerrar, o las fechas seleccionadas en formato "dd-mm-yyyy" si se confirma la selección
    def mostrarEventosSismicosASeleccionar(self, datos):
        ventana = Tk()
        ventana.title("Tabla de Eventos Sismicos Autodetectados")

        encabezados_Eventos = ['FechaHoraOcurrencia', 'LatitudEpicentro', 'LongitudHipocentro', 'ValorMagnitud', 'LongitudEpicentro', 'LatitudHipocentro']

        tabla = ttk.Treeview(ventana, columns=encabezados_Eventos, show="headings")
        for encabezado in encabezados_Eventos:
            ancho_columna = 150  
            tabla.heading(encabezado, text=encabezado, anchor=CENTER)
            tabla.column(encabezado, width=ancho_columna, anchor=CENTER)

        for fila_datos in datos[:6]:
            
            if len(fila_datos) >= 6:
                datos_eventos = [fila_datos[0], fila_datos[1], fila_datos[2], fila_datos[3], fila_datos[3], fila_datos[4], fila_datos[5]]

                tabla.insert("", "end", values=datos_eventos)
            else:
                pass
        else:
            print("Error: El número de elementos en la fila no es suficiente.")

        for encabezado in encabezados_Eventos:
            tabla.heading(encabezado, text=encabezado, command=lambda _encabezado=encabezado: treeview_sort_column(tabla, _encabezado, False))
        
        tabla.pack(expand=True, fill=BOTH)
        
        boton_cerrar = Button(ventana, text="Cerrar Todo", command=ventana.quit)
        boton_cerrar.pack(pady=10)

        center_window(ventana)
        ventana.mainloop()

    
    def validar_periodo(self):
        fecha_desde = self.cal_desde.get_date()
        fecha_hasta = self.cal_hasta.get_date()

        if fecha_desde >= fecha_hasta:
            self.error_label.config(text="La fecha hasta debe ser mayor que la fecha desde.")
            return

        self.error_label.config(text="Fechas validas ...")
        self.root.quit()
    
    # Esta función crea una ventana de interfaz gráfica para seleccionar el tipo de reseña.
    def solicitar_sel_tipo_resenia(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Red Sísmica")
        self.root.configure(bg="#800020")

        self.tomar_tipo_resenia()

        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        self.boton = Button(self.root, text="Enviar", command=self.root.quit, font=mi_tipo_de_letra, fg="black")
        self.boton.config(height=3, width=25)  
        self.boton.place(relx=0.5, rely=0.9, anchor='center')

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        center_window(self.root)
        self.root.mainloop()

        if self.cerrar_presionado:
            return True
        else:
            return self.tipo_resenia.get()

    # Esta función crea y configura un combobox para seleccionar el tipo de reseña en la ventana principal.
    def tomar_tipo_resenia(self):
        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        # Crear y posicionar la etiqueta
        label = Label(self.root, text="Seleccionar Tipo de Reseña", foreground="black", font=mi_tipo_de_letra)
        label.place(relx=0.5, rely=0.3, anchor='center')  # Posicionar en el centro de la ventana

        # Crear y posicionar el combo box
        self.tipo_resenia = StringVar(self.root)
        self.tipo_resenia.set("Sommelier")  # Valor por defecto
        opciones_resenia = ["Reseñas normales", "Sommelier", "Amigos"]
        self.combo_resenia = Combobox(self.root, textvariable=self.tipo_resenia, values=opciones_resenia)
        self.combo_resenia.place(relx=0.5, rely=0.4, anchor='center')  # Posicionar en el centro de la ventana
        self.combo_resenia.configure(state="readonly")

    # Esta función crea una ventana de interfaz gráfica para seleccionar el tipo de visualización.
    def solicitar_sel_tipo_visualizacion(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Red Sísmica")

        self.root.configure(bg="#800020")

        self.tomar_tipo_visualizacion()

        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        self.boton = Button(self.root, text="Enviar", command=self.root.quit, font=mi_tipo_de_letra, fg="black")
        self.boton.config(height=3, width=25)  
        self.boton.place(relx=0.5, rely=0.9, anchor='center')

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        center_window(self.root)
        self.root.mainloop()

        if self.cerrar_presionado:
            return True
        else:
            return self.tipo_visualizacion.get()

    # Esta función crea y configura un combobox para seleccionar el tipo de visualización en la ventana principal.
    def tomar_tipo_visualizacion(self):
        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        label = Label(self.root, text="Seleccionar Tipo de Visualizacion", foreground="black", font=mi_tipo_de_letra)
        label.place(relx=0.5, rely=0.3, anchor='center')

        self.tipo_visualizacion = StringVar(self.root)
        self.tipo_visualizacion.set("Excel")
        opciones_visualizacion = ["Excel", "PDF", "Pantalla"]
        self.combo_visualizacion = Combobox(self.root, textvariable=self.tipo_visualizacion, values=opciones_visualizacion)
        self.combo_visualizacion.place(relx=0.5, rely=0.4, anchor='center')
        self.combo_visualizacion.configure(state="readonly")

    # Funcion para tomar el cierre de la ventana
    def cerrar_press(self):
        self.cerrar_presionado = True
        self.root.quit()

    # Esta función crea una ventana para solicitar la confirmación del usuario antes de generar el reporte de ranking.
    def solicitar_confirmacion_gen_reporte(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Red Sísmica")
        self.root.configure(bg="#800020")

        self.confirmado = False

        self.label_confirmacion = Label(self.root, text="¿Desea generar el reporte Ranking?", font=("Arial", 16), bg="#800020", fg="white")
        self.label_confirmacion.place(relx=0.5, rely=0.4, anchor="center")

        self.tomar_confirmacion_gen_reporte()

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        center_window(self.root)
        self.root.mainloop()

        if self.confirmado:
            return True
        else:
            return False

    # funcion propia del boton   
    def confirmar(self):
        self.confirmado = True
        self.root.quit()

    # funcion propia del boton 
    def cancelar(self):
        self.confirmado = False
        self.root.quit()

    # Esta función configura los botones de confirmación y cancelación en la ventana de confirmación para generar el reporte de ranking.
    def tomar_confirmacion_gen_reporte(self):
        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        self.boton_confirmar = Button(self.root, text="Confirmar", command=self.confirmar, font=mi_tipo_de_letra, fg="black")
        self.boton_confirmar.config(height=3, width=12)
        self.boton_confirmar.place(relx=0.35, rely=0.6, anchor="center")

        self.boton_cancelar = Button(self.root, text="Cancelar", command=self.cancelar, font=mi_tipo_de_letra, fg="black")
        self.boton_cancelar.config(height=3, width=12)
        self.boton_cancelar.place(relx=0.65, rely=0.6, anchor="center")


    def confirmar_exportacion(self,tipo):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Red Sísmica")
        self.root.configure(bg="#800020")

        self.confirmado = False

        texto=f'¿Desea confirmar la exportacion en {tipo}?'
        self.label_confirmacion = Label(self.root, text=texto, font=("Arial", 16), bg="#800020", fg="white")
        self.label_confirmacion.place(relx=0.5, rely=0.4, anchor="center")

        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        self.boton_confirmar = Button(self.root, text="Confirmar", command=self.confirmar, font=mi_tipo_de_letra, fg="black")
        self.boton_confirmar.config(height=3, width=12)
        self.boton_confirmar.place(relx=0.35, rely=0.6, anchor="center")

        self.boton_cancelar = Button(self.root, text="Cancelar", command=self.cancelar, font=mi_tipo_de_letra, fg="black")
        self.boton_cancelar.config(height=3, width=12)
        self.boton_cancelar.place(relx=0.65, rely=0.6, anchor="center")

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        center_window(self.root)
        self.root.mainloop()

        if self.confirmado:
            return True
        else:
            return False

    

# funcion propia del lenguaje para centrar las ventanas       
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry("{}x{}+{}+{}".format(width, height, x, y))

# Función propia del lenguaje para ordenar las columnas de mostrar por pantalla el ranking.
def treeview_sort_column(tabla, col, reverse):
    lista = [(tabla.set(k, col), k) for k in tabla.get_children('')]
    lista.sort(reverse=reverse)

    for index, (valor, k) in enumerate(lista):
        tabla.move(k, '', index)

    tabla.heading(col, command=lambda: treeview_sort_column(tabla, col, not reverse))