from tkinter import *
from Clases.PantallaRegRevisionManual import *
from Clases.GestorRegRevisionManual import *  
from Datos.datos import *

# funcion que contiene toda la logica
def main():
    pantalla_registrar_revision_manual = PantallaRegRevisionManual()
    #gestor_registrar_revision_manual = GestorRegRevisionManual(EventosSismicos, pantalla_registrar_revision_manual)
    opcion_reg_resultado_de_Revisión_Manual=pantalla_registrar_revision_manual.opcionRegResultadoDeRevisiónManual()
    pantalla_registrar_revision_manual.habilitar_pantalla()
    
    #gestor_registrar_revision_manual.fin_cu()
    
    
    eventos = generar_eventos_sismicos(5)
    mostrarEventos=pantalla_registrar_revision_manual.mostrarEventosSismicosASeleccionar(eventos)       
    print(mostrarEventos)
                         
if __name__ == '__main__':
    main()
