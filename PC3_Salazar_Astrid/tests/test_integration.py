from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sumar_integracion():
    respuesta = client.get("/sumar", params={"a": 3, "b": 4})

    assert respuesta.status_code == 200
    assert respuesta.json() == {"resultado": 7}

def test_promedio_lista_valida():
    respuesta = client.post("/promedio", json={"valores": [3, 6, 12]})

    assert respuesta.status_code == 200
    assert respuesta.json() == {"promedio": 7.0}


def test_promedio_lista_vacia():
    respuesta = client.post("/promedio", json={"valores": []})

    assert respuesta.status_code == 400
    assert respuesta.json() == {"detail": "Lista vacía"}

def test_endpoints():
    with TestClient(app) as sesion:
        respuesta_health = sesion.get("/health")
        respuesta_suma = sesion.get("/sumar", params={"a": 3, "b": 4})
        respuesta_promedio = sesion.post(
            "/promedio", json={"valores": [3, 6, 12]}
        )

        assert respuesta_health.status_code == 200
        assert respuesta_health.json() == {"status": "ok"}

        assert respuesta_suma.status_code == 200
        assert respuesta_suma.json() == {"resultado": 7}

        assert respuesta_promedio.status_code == 200
        assert respuesta_promedio.json() == {"promedio": 7.0}