# Trabajo Práctico Recuperatorio - Estaciones del SMN

**Materia:** Programación 1 - UNRN   Comision 3 - Ingenieria en Telecomunicaciones.  
**Estudiante:** Alan Michael Mendoza Ruffin  
**Docente:** Lautaro Yamil Linquiman Ventura  

## Descripción del proyecto
Este programa sirve para procesar un archivo JSON con observaciones del SMN, valida los registros y consulta el resumen de temperaturas.

## Configuración del entorno

Crear el ambiente virtual:
```bash
python -m venv .venv
```

Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución del programa

Consulta por estación meteorológica (ejemplo con `AEROPARQUE AERO`):

```bash
python main.py observaciones.json "AEROPARQUE AERO"
```

## Ejecución de pruebas

Correr las pruebas unitarias:

```bash
pytest
```