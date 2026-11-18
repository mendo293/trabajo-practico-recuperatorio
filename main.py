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
    heladas = consultar_clima.obtener_heladas(de_la_estacion)
    
    print(estacion)
    print(f"Observaciones: {resumen['cantidad']}")
    print(f"Temperatura mínima: {minima.temperatura} °C a las {minima.hora} h")
    print(f"Temperatura máxima: {maxima.temperatura} °C a las {maxima.hora} h")
    print(f"Temperatura promedio: {resumen['promedio']} °C")
    print()
    print(f"Horas de helada: {len(heladas)}")
    for obs in heladas:
        print(f"  {obs.estacion} a las {obs.hora} h ({obs.temperatura} °C)")
    print()
    for observacion in observaciones:
        if observacion.es_helada():
            print(f"{observacion} | ES HELADA")
        else:
            print(f"{observacion} | No es helada")


main()
