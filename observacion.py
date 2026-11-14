class Observacion:
    def __init__(self, estacion, hora, temperatura, humedad, velocidad_viento):
        if not isinstance(estacion, str) or estacion.strip() == "":
            raise ValueError("La estación no puede estar vacía.")
        if not isinstance(hora, int) or not (0<=hora<=23):
            raise ValueError("La hora debe ser un entero y debe estar entre 0 y 23.")
        if None in (temperatura, humedad, velocidad_viento):
            raise ValueError("La temperatura, la humedad y la velocidad del viento no pueden faltar.")
        if not isinstance(temperatura, (int, float)):
            raise ValueError("La temperatura debe ser un valor numérico.")
        if not isinstance(humedad, (int, float)) or not (0<=humedad<=100):
            raise ValueError("La humedad debe ser un valor numérico y debe estar entre 0 y 100.")
        if not isinstance(velocidad_viento, (int, float)) or not (0<=velocidad_viento):
            raise ValueError("La velocidad del viento tiene que ser un valor númerico y no puede ser negativa.")
        
        self.estacion = estacion.strip()
        self.hora = hora
        self.temperatura = float(temperatura)
        self.humedad = humedad
        self.velocidad_viento = velocidad_viento
        
    def es_estacion(self, nombre_estacion):
        if not isinstance(nombre_estacion, str):
            return False
        if self.estacion.upper() == nombre_estacion.strip().upper():
            return True
        else:
            return False
        
    def intensidad_viento(self):
       if self.velocidad_viento < 2:
           return "calma"
       elif self.velocidad_viento < 20:
           return "leve"
       elif self.velocidad_viento < 40:
           return "moderado"
       return "fuerte"
   
    def __str__(self):
        intensidad = self.intensidad_viento()
        return (f"{self.estacion} | {self.hora} h | {self.temperatura} °C | {self.humedad} % | {self.velocidad_viento} km/h ({intensidad})" )