def main():
        evento1 = {"FechaHoraOcurrencia": 3, "LatitudEpicentro": 2, "LongitudHipocentro": 1}
        evento2 = {"FechaHoraOcurrencia": 1, "LatitudEpicentro": 2, "LongitudHipocentro": 3}
        eventosAutodetectados = [evento1, evento2]  # Changed to a list instead of a set
        ordenado_por_valor = sorted(eventosAutodetectados, key=lambda item: item["FechaHoraOcurrencia"])  # Sorting by "FechaHoraOcurrencia"
        print(ordenado_por_valor)

if __name__ == '__main__':
        main()
