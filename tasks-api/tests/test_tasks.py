from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_crear_y_consultar_tarea():
    r = client.post("/tasks", json={"title": "Comprar pan"})
    assert r.status_code == 201
    tarea = r.json()
    assert tarea["title"] == "Comprar pan" and tarea["done"] is False
    assert client.get(f"/tasks/{tarea['id']}").json() == tarea


def test_titulo_vacio_se_rechaza():
    assert client.post("/tasks", json={"title": ""}).status_code == 422


def test_completar_tarea():
    tid = client.post("/tasks", json={"title": "Pagar luz"}).json()["id"]
    r = client.patch(f"/tasks/{tid}", json={"done": True})
    assert r.status_code == 200 and r.json()["done"] is True


def test_eliminar_tarea():
    tid = client.post("/tasks", json={"title": "Borrar"}).json()["id"]
    assert client.delete(f"/tasks/{tid}").status_code == 204
    assert client.get(f"/tasks/{tid}").status_code == 404


def test_tarea_inexistente():
    assert client.get("/tasks/99999").status_code == 404
