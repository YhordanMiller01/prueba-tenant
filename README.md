# sqai-demo-repo

Repositorio de prueba para el camino feliz de **sq_ai**: una API de tareas pequeña y en memoria que sirve de sistema bajo prueba (SUT).

```
sqai-demo-repo/
├── docs/historias.md      # 4 historias con criterios de aceptación
└── tasks-api/             # servicio (carpeta de primer nivel = servicio para el escaneo de F0.1)
    ├── app/main.py        # FastAPI, 6 endpoints
    ├── openapi.json       # contrato (generado desde la app)
    ├── requirements.txt   # manifiesto del servicio
    └── tests/             # 6 pruebas pytest
```

## Ejecutar

```bash
cd tasks-api
python -m venv .venv && . .venv/Scripts/activate   # en Linux/macOS: . .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q                      # 6 pruebas
python -m uvicorn app.main:app --port 4010
```

Contrato en `http://localhost:4010/openapi.json`.

## Endpoints

| Método | Ruta | Respuestas |
|---|---|---|
| GET | `/health` | 200 |
| GET | `/tasks` | 200 |
| POST | `/tasks` | 201, 422 |
| GET | `/tasks/{id}` | 200, 404 |
| PATCH | `/tasks/{id}` | 200, 404, 422 |
| DELETE | `/tasks/{id}` | 204, 404 |

## Regenerar `openapi.json`

```bash
cd tasks-api
python -c "import json; from app.main import app; open('openapi.json','w',encoding='utf-8').write(json.dumps(app.openapi(), indent=2, ensure_ascii=False)+'\n')"
```
