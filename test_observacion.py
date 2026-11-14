import pytest
from observacion import Observacion

def test_observacion_valida():
    obs = Observacion(
        estacion="BARILOCHE AERO",
        hora=12,
        temperatura=10.5,
        humedad=65,
        velocidad_viento=20,
    )
    
    assert obs.estacion == "BARILOCHE AERO"
    assert obs.hora == 12
    assert obs.temperatura == 10.5
    assert obs.humedad == 65
    assert obs.velocidad_viento == 20
    
def test_observacion_humedad_invalida():
    with pytest.raises(ValueError):
        Observacion(
            estacion="BARILOCHE AERO",
            hora=12,
            temperatura= 10.5,
            humedad=250,
            velocidad_viento=20,
        )