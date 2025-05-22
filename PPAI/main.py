from tkinter import *
from Clases.PantallaRegRevisionManual import *
from Clases.GestorRegRevisionManual import *  
from Datos.datos import *


def main():
    # Inicializar la ventana principal  
    pantalla_registrar_revision_manual = PantallaRegRevisionManual()
    pantalla_registrar_revision_manual.opcionRegResultadoDeRevisiónManual()
    
    
if __name__ == '__main__':
    main()
