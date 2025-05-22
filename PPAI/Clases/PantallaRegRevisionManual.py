from tkinter import *
from tkinter import messagebox,ttk,simpledialog,font
from datetime import datetime
from tkcalendar import Calendar, DateEntry
from tkinter.ttk import Combobox
from Clases.GestorRegRevisionManual import * 
from Clases.Estado import * 
from Clases.Sesion import * 
from tkinter import *
from PIL import Image, ImageTk
import os

class PantallaRegRevisionManual():
    def __new__(cls):
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self):
        self.gestor = None
        ruta_imagen = os.path.join(os.path.dirname(__file__), "sismograma.png")
        self.imagen = ImageTk.PhotoImage(Image.open(ruta_imagen))

    
    # Esta función crea una ventana de interfaz gráfica con un botón para generar un reporte de ranking de vinos.
    def opcionRegResultadoDeRevisiónManual(self):
        self.habilitar_pantalla()
        

    def habilitar_pantalla(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Red Sísmica")
        self.root.resizable(False, False)

        self.root.configure(bg="#050c57")

        self.cerrar_presionado = True

        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        self.boton = Button(self.root, text="Registrar resultado de revisión manual", font=mi_tipo_de_letra, command=self.root.quit)
        self.boton.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.boton.config(height=3, width=35) 
        self.boton.place(relx=0.5, rely=0.5, anchor="center")

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        center_window(self.root)
        self.root.mainloop()

        if self.cerrar_presionado:
            self.gestor = GestorRegRevisionManual(self)
            self.gestor.opcRegRevisionManual()
            
            
            return True
        else:return False
  
    def mostrarEventosSismicosASeleccionar(self, datos):
        self.root = Tk()
        self.root.geometry("900x300")
        self.root.title("Red Sísmica")
        self.root.resizable(False, False)

        
        encabezados_Eventos = [
            'FechaHoraOcurrencia', 'LatitudEpicentro', 'LongitudHipocentro',
            'ValorMagnitud', 'LongitudEpicentro', 'LatitudHipocentro'
        ]

        # Permitir selección múltiple
        self.tabla_eventos = ttk.Treeview(self.root, columns=encabezados_Eventos, show="headings", selectmode="extended")
        for encabezado in encabezados_Eventos:
            ancho_columna = 150
            self.tabla_eventos.heading(encabezado, text=encabezado, anchor=CENTER)
            self.tabla_eventos.column(encabezado, width=ancho_columna, anchor=CENTER)
        
        
        for fila_datos in datos[:6]:
            print(fila_datos)
            datos_eventos = [
                fila_datos['fechaHoraOcurrencia'], fila_datos['latitudEpicentro'],
                fila_datos['longitudHipocentro'], fila_datos['valorMagnitud'],
                fila_datos['longitudEpicentro'], fila_datos['latitudHipocentro']
            ]
            self.tabla_eventos.insert("", "end", values=datos_eventos)

        for encabezado in encabezados_Eventos:
            self.tabla_eventos.heading(encabezado, text=encabezado, command=lambda _encabezado=encabezado: treeview_sort_column(self.tabla_eventos, _encabezado, False))

        self.tabla_eventos.pack(expand=True, fill=BOTH)

        frame_botones = Frame(self.root)
        frame_botones.pack(pady=5)

        boton_enviar = Button(frame_botones, text="Enviar", command=self.tomarSeleccionEventoSismico)
        boton_enviar.pack(side=LEFT, padx=10)

        boton_cancelar = Button(frame_botones, text="Cancelar", command=self.cancelar)
        boton_cancelar.pack(side=LEFT, padx=10)

        center_window(self.root)
        self.seleccion_eventos = None
        self.root.mainloop()

        return self.seleccion_eventos

    def tomarSeleccionEventoSismico(self):
        items = self.tabla_eventos.selection()
        if items:
            
            self.seleccion_eventos = [self.tabla_eventos.item(item, 'values') for item in items]
            self.root.quit()
            self.gestor.tomarSeleccionEventoSismico(self.seleccion_eventos)
            
            
        else:
            messagebox.showwarning("Selección requerida", "Por favor seleccione al menos una fila antes de enviar.")
    """   
    def mostrarDatosEventosSismicos(self, detalles):

        print(detalles)
    
        self.root = Tk()
        self.root.geometry("900x300")
        self.root.title("Red Sísmica")
        self.root.resizable(False, False)
        self.cerrar_presionado = False

        encabezados_Eventos = ["Alcance:", "Clasificación:", "Origen de Generación:"]
        self.tabla_eventos = ttk.Treeview(self.root, columns=encabezados_Eventos, show="headings", selectmode="extended")
        for encabezado in encabezados_Eventos:
            ancho_columna = 150
            self.tabla_eventos.heading(encabezado, text=encabezado, anchor=CENTER)
            self.tabla_eventos.column(encabezado, width=ancho_columna, anchor=CENTER)

        for fila_datos in detalles:
            datos_eventos = [
                fila_datos.fechaHoraOcurrencia, fila_datos.latitudEpicentro,
                fila_datos.longitudHipocentro, fila_datos.valorMagnitud,
                fila_datos.longitudEpicentro, fila_datos.latitudHipocentro
            ]
            self.tabla_eventos.insert("", "end", values=datos_eventos)

        for encabezado in encabezados_Eventos:
            self.tabla_eventos.heading(encabezado, text=encabezado, command=lambda _encabezado=encabezado: treeview_sort_column(self.tabla_eventos, _encabezado, False))

        self.tabla_eventos.pack(expand=True, fill=BOTH)

        frame_botones = Frame(self.root)
        frame_botones.pack(pady=5)

        boton_enviar = Button(frame_botones, text="Enviar", command=self.tomarSeleccionEventoSismico)
        boton_enviar.pack(side=LEFT, padx=10)

        boton_cancelar = Button(frame_botones, text="Cancelar", command=self.cancelar)
        boton_cancelar.pack(side=LEFT, padx=10)

        center_window(self.root)
        self.seleccion_eventos = None
        self.root.mainloop()

        return self.seleccion_eventos
    """
    def mostrarDatosEventosSismicos(self, DATOS):

        import tkinter as tk
        from tkinter import messagebox
        
        # Verificamos que la lista tenga 3 elementos
        if len(DATOS) != 3:
            messagebox.showerror("Error", "Se esperaban 3 datos: alcance, clasificación y origen.")
            return

        alcance, clasificacion, origen = DATOS

        # Crear ventana principal
        ventana = tk.Tk()
        ventana.title("Datos del Evento Sísmico")
        ventana.geometry("400x200")

        # Etiquetas para mostrar los datos
        tk.Label(ventana, text="Alcance:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10, 0))
        tk.Label(ventana, text=alcance, font=("Arial", 12)).pack(anchor="w", padx=20)

        tk.Label(ventana, text="Clasificación:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10, 0))
        tk.Label(ventana, text=clasificacion, font=("Arial", 12)).pack(anchor="w", padx=20)

        tk.Label(ventana, text="Origen de Generación:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10, 0))
        tk.Label(ventana, text=origen, font=("Arial", 12)).pack(anchor="w", padx=20)

        # Botón para cerrar la ventana
        tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=15)

        ventana.mainloop()

    def mostrarSismograma(self):


        ventana = tk.Tk()
        ventana.title("Sismograma")

        # Cargar la imagen
        try:
            imagen = Image.open(self.imagen)
            imagen = imagen.resize((500, 300))  # Ajustar tamaño si es necesario
            imagen_tk = ImageTk.PhotoImage(imagen)
        except Exception as e:
            tk.messagebox.showerror("Error al cargar imagen", str(e))
            return

        # Mostrar imagen
        etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
        etiqueta_imagen.image = imagen_tk  # Importante para que no se libere la memoria
        etiqueta_imagen.pack(pady=10)

        # Mostrar leyenda
        etiqueta_leyenda = tk.Label(ventana, text="Sismograma por estación sismológica", font=("Arial", 12, "italic"))
        etiqueta_leyenda.pack()

        # Botón para cerrar
        tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=10)

        ventana.mainloop()



    def habilitarOpcionVisualizarMapa(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Red Sísmica")
        self.root.configure(bg="#050c57")

        self.confirmado = False

        self.label_confirmacion = Label(self.root, text="¿Desea visualizar en un mapa el evento sísmico y las estaciones sismológicas involucradas?", font=("Arial", 16), bg="#050c57", fg="white")
        self.label_confirmacion.place(relx=0.5, rely=0.4, anchor="center")

        self.tomarOpcionConfirmacionMapa()

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        center_window(self.root)
        self.root.mainloop()

        if self.confirmado:
            return True
        else:
            return False
    
    def tomarOpcionConfirmacionMapa(self):
        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        self.boton_confirmar = Button(self.root, text="Confirmar", command=self.confirmar, font=mi_tipo_de_letra, fg="black")
        self.boton_confirmar.config(height=3, width=12)
        self.boton_confirmar.place(relx=0.35, rely=0.6, anchor="center")

        self.boton_cancelar = Button(self.root, text="Cancelar", command=self.cancelar, font=mi_tipo_de_letra, fg="black")
        self.boton_cancelar.config(height=3, width=12)
        self.boton_cancelar.place(relx=0.65, rely=0.6, anchor="center")
        
    def habilitarOpcionModificarDatosEvento(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Red Sísmica")
        self.root.configure(bg="#050c57")

        self.confirmado = False

        self.label_confirmacion = Label(self.root, text="¿Desea modificar los datos del evento sísmico?", font=("Arial", 16), bg="#050c57", fg="white")
        self.label_confirmacion.place(relx=0.5, rely=0.4, anchor="center")

        self.tomarOpcionModificarDatosEvento()

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)

        center_window(self.root)
        self.root.mainloop()

        if self.confirmado:
            return True
        else:
            return False

    def tomarOpcionModificarDatosEvento(self):
        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        self.boton_confirmar = Button(self.root, text="Confirmar", command=self.confirmar, font=mi_tipo_de_letra, fg="black")
        self.boton_confirmar.config(height=3, width=12)
        self.boton_confirmar.place(relx=0.35, rely=0.6, anchor="center")

        self.boton_cancelar = Button(self.root, text="Cancelar", command=self.cancelar, font=mi_tipo_de_letra, fg="black")
        self.boton_cancelar.config(height=3, width=12)
        self.boton_cancelar.place(relx=0.65, rely=0.6, anchor="center")
    
    def mostrarOpcionesParaSeleccionar(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Red Sísmica")
        self.root.configure(bg="#050c57")

        self.confirmado = False

        self.label_confirmacion = Label(self.root, text="Seleccionar una accion para realizar sobre el Evento", font=("Arial", 16), bg="#050c57", fg="white")
        self.label_confirmacion.place(relx=0.5, rely=0.4, anchor="center")
        
        self.tomarSeleccionAccion()
        
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_press)
        center_window(self.root)
        self.root.mainloop()

        if self.confirmado:
            return True
        else:
            return False

    def tomarSeleccionAccion(self):
        mi_tipo_de_letra = font.Font(family="Arial", size=14, weight="bold")

        self.boton_confirmar = Button(self.root, text="Confirmar", command=self.confirmar, font=mi_tipo_de_letra, fg="black")
        self.boton_confirmar.config(height=3, width=12)
        self.boton_confirmar.place(relx=0.35, rely=0.6, anchor="center")

        self.boton_cancelar = Button(self.root, text="Cancelar", command=self.cancelar, font=mi_tipo_de_letra, fg="black")
        self.boton_cancelar.config(height=3, width=12)
        self.boton_cancelar.place(relx=0.65, rely=0.6, anchor="center")
        
        self.boton_cancelar = Button(self.root, text="Rechazar", command=self.cancelar, font=mi_tipo_de_letra, fg="black")
        self.boton_cancelar.config(height=3, width=12)
        self.boton_cancelar.place(relx=0.95, rely=0.6, anchor="center")
        
        self.boton_cancelar = Button(self.root, text="Solicitar revisión a experto", command=self.cancelar, font=mi_tipo_de_letra, fg="black")
        self.boton_cancelar.config(height=3, width=12)
        self.boton_cancelar.place(relx=0.95, rely=0.6, anchor="center")
    
    # Funcion para tomar el cierre de la ventana
    def cerrar_press(self):
        self.cerrar_presionado = True
        self.root.quit()

    # funcion propia del boton   
    def confirmar(self):
        self.confirmado = True
        self.root.quit()

    # funcion propia del boton 
    def cancelar(self):
        self.confirmado = False
        self.root.quit()
    
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
