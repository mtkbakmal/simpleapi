from fastapi import FastAPI
from a2wsgi import ASGIMiddleware

app = FastAPI()

@app.get("/")
def test_root():
    return {"message": "Ура, FastAPI на PythonAnywhere наконец-то работает!"}

wsgi_app = ASGIMiddleware(app)  # type: ignore