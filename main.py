import sys
import consultar_clima


def main():
    ruta = sys.argv[1]
    estacion = sys.argv[2]

    observaciones = consultar_clima.cargar_observaciones(ruta)
    print(f"Observaciones válidas: {len(observaciones)}")
    print()

    de_la_estacion = consultar_clima.filtrar_estaciones(observaciones, estacion)
    resumen = consultar_clima.resumen_temperaturas(de_la_estacion)
    minima = resumen["minima"]
    maxima = resumen["maxima"]

    print(estacion)
    print(f"Observaciones: {resumen['cantidad']}")
    print(f"Temperatura mínima: {minima.temperatura} °C a las {minima.hora} h")
    print(f"Temperatura máxima: {maxima.temperatura} °C a las {maxima.hora} h")
    print(f"Temperatura promedio: {resumen['promedio']} °C")
    print()
    for observacion in de_la_estacion:
        print(observacion)


main()