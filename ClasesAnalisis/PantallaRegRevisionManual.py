from ClasesAnalisis.GestorRegRevisionManual import GestorRegRevisionManual
from tkinter import *
from tkinter import ttk, font, messagebox
from PIL import Image, ImageTk


class PantallaRegRevisionManual:
    def __init__(self):
        self.gestor = GestorRegRevisionManual(self)
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.title("Red Sismica")
        self.root.resizable(False, False)
        self.fuente = font.Font(family="Arial", size=14, weight="bold")
        self.fuente2 = font.Font(family="Arial", size=12, weight="bold")
        self.boton = Button(self.root, text="Registrar resultado de revisión manual", font=self.fuente,
                            command=self.root.destroy)
        self.frameOpcionActual = None


    def opcionRegResultadoDeRevisionManual(self):
        self.habilitarVentana()


    def habilitarVentana(self):
        self.root.configure(bg="#050c57")
        self.boton.pack(expand=True)
        self.root.mainloop()

        self.gestor.opcRegRevisionManual()


    def mostrarEventosSismicosASeleccionar(self, datosEventos):
        print("Mostrar Eventos")
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.title("Red Sismica")
        self.root.resizable(False, False)

        encabezados_Eventos = [
            'FechaHoraOcurrencia', 'LatitudEpicentro', 'LongitudEpicentro',
            'LongitudHipocentro', 'LatitudHipocentro', 'ValorMagnitud'
        ]

        self.tabla_eventos = ttk.Treeview(self.root, columns=encabezados_Eventos, show="headings")

        for encabezado in encabezados_Eventos:
            ancho_columna = 130
            self.tabla_eventos.heading(encabezado, text=encabezado, anchor=CENTER)
            self.tabla_eventos.column(encabezado, width=ancho_columna, anchor=CENTER)

        for id, datos in datosEventos.items():
            valoresDatos = list(datos.values())
            self.tabla_eventos.insert("", "end", values=valoresDatos)

        botonEnviar = Button(self.root, text="Enviar", font=self.fuente,
                            command=self.tomarSeleccionEventoSismico)

        self.tabla_eventos.pack(expand=True, fill=BOTH)
        botonEnviar.pack()
        self.root.mainloop()


    def tomarSeleccionEventoSismico(self):
        indice = self.tabla_eventos.selection()[0] # I001
        print("Indice seleccionado:", indice)
        if indice:
            seleccion = int(indice[1:]) - 1 # Indice de la tabla -1 es el indice de la lista
            self.root.destroy()
            print("Seleccionado:", seleccion)
            self.gestor.tomarSeleccionEventoSismico(seleccion)
        else:
            messagebox.showwarning("Selección requerida",
                                   "Por favor seleccione al menos una fila antes de enviar.")


    # Alternativo 1
    def noHayEventosParaMostrar(self):
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.title("Red Sismica")
        self.root.resizable(False, False)
        self.root.configure(bg="#050c57")
        Label(self.root, text="No hay eventos sismicos autodetectados", bg="#050c57",
              font=self.fuente, fg="white").pack(expand=True)

        self.root.mainloop()


    def mostrarDatosEventosSismicos(self, datos, sismogramasPorEstacion):
        print("Mostrar Datos Evento")
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.title("Red Sismica")
        self.root.resizable(False, False)

        frame = ttk.Frame(self.root)

        # Datos: Alcance, Clasificacion y Origen
        valoresDatos = list(datos[0])
        frameDatos = ttk.LabelFrame(frame, text="Datos de Evento")
        frameDatos.grid(row=0, column=0)
        (Label(frameDatos, text="Alcance:", font=self.fuente2).
         grid(row=0, column=0, sticky="w", pady=5))
        (Label(frameDatos, text=valoresDatos[0], font=self.fuente2)
         .grid(row=0, column=1, sticky="w", pady=5))

        (Label(frameDatos, text="Clasificacion:", font=self.fuente2)
         .grid(row=1, column=0, sticky="w", pady=5))
        (Label(frameDatos, text=valoresDatos[1], font=self.fuente2)
         .grid(row=1, column=1, sticky="w", pady=5))

        (Label(frameDatos, text="Origen:", font=self.fuente2)
         .grid(row=2, column=0, sticky="w", pady=5))
        (Label(frameDatos, text=valoresDatos[2], font=self.fuente2)
         .grid(row=2, column=1, sticky="w", pady=5))

        # Series
        series = datos[1]
        frameSeries = ttk.LabelFrame(frame, text="Serie Temporal")
        i2 = 0
        for ser in series:
            i2 += 1
            # Cada serie : [CondicionAlarma, FechaInicio, Frecuencia], [Muestras]
            Label(frameSeries, text="Fecha de Inicio:").grid(row=0, column=0, sticky="w")
            Label(frameSeries, text=ser[0][1]).grid(row=0, column=1, sticky="w")

            Label(frameSeries, text="Frecuencia:").grid(row=1, column=0, sticky="w")
            Label(frameSeries, text=ser[0][2]).grid(row=1, column=1, sticky="w")

            Label(frameSeries, text="Alerta de Alarma:").grid(row=2, column=0, sticky="w")
            Label(frameSeries, text=str(ser[0][0])).grid(row=2, column=1, sticky="w")

            for muestra in ser[1]:
                # Cada muestra: Fecha, [ [Detalle1], [Detalle2] ]
                Label(frameSeries, text=muestra[0]).grid(sticky="w")
                for detalle in muestra[1]:
                    detalleCompleto = str(detalle[1]) + ": " + str(detalle[0]) + str(detalle[2])
                    Label(frameSeries, text="   " + detalleCompleto).grid(sticky="w")


        # Sismogramas
        frameSismogramas = Frame(self.root)
        frameSis = None
        i = 0
        imagenes = []
        for sismograma in sismogramasPorEstacion:
            # Sismograma: [nombreEstacion, sismograma]
            i += 1
            frameSis = ttk.LabelFrame(frameSismogramas, text=sismograma[0])
            frameSis.grid(row=0, column=i)
            image_pil = Image.open(sismograma[1])
            image = ImageTk.PhotoImage(image_pil)
            imagenes.append(image)
            Label(frameSis, image=imagenes[i-1]).grid(row=0, column=i)

        frame.pack(ipadx=30, anchor="center")
        frameDatos.pack(side="left")
        frameSeries.pack(side="right")
        if frameSis:
            frameSismogramas.pack()

        # Opcion Visualiza Mapa
        self.habilitarOpcionVisualizarMapa()

        self.root.mainloop()


    def mostrarSismograma(self, sismogramasPorEstacion):
        # [nombreEstacion, sismograma]
        pass


    def habilitarOpcionVisualizarMapa(self):
        self.frameOpcionActual = ttk.Frame(self.root)
        labelMapa = Label(self.frameOpcionActual, text="Desea visualizar en un mapa?", font=self.fuente)
        botonSi = Button(self.frameOpcionActual, text="Si", font=self.fuente,
                         command=self.tomarOpcionConfirmacionMapa)
        botonNo = Button(self.frameOpcionActual, text="No", font=self.fuente,
                             command=self.tomarOpcionConfirmacionMapa)
        self.frameOpcionActual.pack(anchor="center")
        labelMapa.grid(row=0, column=0, columnspan=2)
        botonSi.grid(row=1, column=0, sticky="nsew")
        botonNo.grid(row=1, column= 1, sticky="nsew")


    def tomarOpcionConfirmacionMapa(self):
        self.frameOpcionActual.destroy()
        # Opcion Modificar Datos
        self.habilitarOpcionModificacionDatosEvento()


    def habilitarOpcionModificacionDatosEvento(self):
        self.frameOpcionActual = ttk.Frame(self.root)
        labelModificar = Label(self.frameOpcionActual, text="Desea modificar los datos?", font=self.fuente)
        botonSi = Button(self.frameOpcionActual, text="Si", font=self.fuente,
                         command=self.tomarOpcionModificarDatosEvento)
        botonNo = Button(self.frameOpcionActual, text="No", font=self.fuente,
                         command=self.tomarOpcionModificarDatosEvento)
        self.frameOpcionActual.pack()
        labelModificar.grid(row=0, column=0, columnspan=2)
        botonSi.grid(row=1, column=0, sticky="nsew")
        botonNo.grid(row=1, column= 1, sticky="nsew")


    def tomarOpcionModificarDatosEvento(self):
        self.frameOpcionActual.destroy()

        self.mostrarOpcionesParaSeleccionar()


    def mostrarOpcionesParaSeleccionar(self):
        self.frameOpcionActual = ttk.LabelFrame(self.root, text="Que desea realizar con el Evento Sismico?")
        botonConfirmar = Button(self.frameOpcionActual, text="Confirmar", font=self.fuente,
                         command=self.confirmarEvento) # ALTERNATIVO
        botonRechazar = Button(self.frameOpcionActual, text="Rechazar", font=self.fuente,
                         command=self.tomarSeleccionAccion)
        botonDerivar = Button(self.frameOpcionActual, text="Derivar", font=self.fuente,
                         command=self.frameOpcionActual.destroy)

        self.frameOpcionActual.pack()
        botonConfirmar.grid(row=0, column=0, padx=10)
        botonRechazar.grid(row=0, column=1, padx=10)
        botonDerivar.grid(row=0, column=2, padx=10)



    def tomarSeleccionAccion(self):
        self.gestor.tomarSeleccionAccion()
        self.root.destroy()


    # Alternativo = Confirmar Evento
    def confirmarEvento(self):
        self.gestor.confirmarEvento()
        self.root.destroy()
