import json
from observacion import Observacion

def cargar_observaciones(ruta_archivo):
    with open(ruta_archivo, "r") as archivo:
        datos = json.load(archivo)
        
    observaciones = []
    
    for reg in datos:
        try:
            obs = Observacion(
                reg["estacion"],
                reg["hora"],
                reg["temperatura"],
                reg["humedad"],
                reg["velocidad_viento"],
            )
            observaciones.append(obs)
        except(ValueError, KeyError):
            continue
        
    return observaciones

def filtrar_estaciones(observaciones, nombre_estacion):
    filtradas = []
    for obs in observaciones:
        if obs.es_estacion(nombre_estacion):
            filtradas.append(obs)
    return filtradas

    
def resumen_temperaturas(observaciones):
    if len(observaciones) == 0:
        return {
           "cantidad": 0,
           "minima": None,
           "maxima": None,
           "promedio": 0.0,
       }
    obs_minima = observaciones[0]
    obs_maxima = observaciones [0]
    suma = 0.0
    horas_helada = 0
    
    for obs in observaciones:
        if obs.temperatura < obs_minima.temperatura:
            obs_minima = obs
        if obs.temperatura > obs_maxima.temperatura:
            obs_maxima = obs
        if obs.es_helada():
            horas_helada += 1
        
        
        suma = suma + obs.temperatura
    
    cantidad = len(observaciones)
    promedio = (suma/cantidad)
    
    return{
        "cantidad": cantidad,
        "minima": obs_minima,
        "maxima": obs_maxima,
        "promedio": promedio,
        "horas": horas_helada,
    }

def obtener_heladas(observaciones):
    heladas = []
    for obs in observaciones:
        if obs.es_helada():
            heladas.append(obs)
    return heladas
