from tkinter import *
from Clases.PantallaRegRevisionManual import *
from Clases.GestorRegRevisionManual import *  
from Datos.datos import *


# Llamada a la funcion que carga los datos de 20 Eventos Sismicos de ejemplo
EventosSismicos=carga_datos()




# funcion que contiene toda la logica
def main():
    pantalla_registrar_revision_manual = PantallaRegRevisionManual()
#    gestor_registrar_revision_manual = GestorRegRevisionManual(EventosSismicos, pantalla_registrar_revision_manual)
    opcion_reg_resultado_de_Revisión_Manual=pantalla_registrar_revision_manual.opcionRegResultadoDeRevisiónManual()
    pantalla_registrar_revision_manual.habilitar_pantalla()
 

    

                                    
#    gestor_registrar_revision_manual.fin_cu()

                         
if __name__ == '__main__':
    main()
