from tkinter import *
from Clases.PantallaRegRevisionManual import *
from Clases.GestorRegRevisionManual import *  
from Datos.datos import *


# Llamada a la funcion que carga los datos de 20 Eventos Sismicos de ejemplo





# funcion que contiene toda la logica
def main():
    # pantalla_registrar_revision_manual = PantallaRegRevisionManual()
#    gestor_registrar_revision_manual = GestorRegRevisionManual(EventosSismicos, pantalla_registrar_revision_manual)
    # opcion_reg_resultado_de_Revisión_Manual=pantalla_registrar_revision_manual.opcionRegResultadoDeRevisiónManual()
    # pantalla_registrar_revision_manual.habilitar_pantalla()

#    gestor_registrar_revision_manual.fin_cu()
    
    
    eventos = generar_eventos_sismicos(5)
    for e in eventos:
        print(f"Sismo del {e.fechaHoraOcurrencia}: Magnitud {e.valorMagnitud} Richter, Clasificacion {e.clasificacion.getNombre()}, Origen {e.origenGeneracion.getNombre()}, Alcance {e.alcanceSismo.getNombre()}")
        
        print(f"        Hipocentro {e.latitudHipocentro} , {e.longitudHipocentro}: Epicentro {e.latitudEpicentro}, {e.longitudEpicentro}")


    print(datetime.now())            

                         
if __name__ == '__main__':
    main()
