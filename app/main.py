from fastapi import FastAPI
from app.routes import router
from app.init_db import init_db

app = FastAPI()

init_db()  # crea tabla automáticamente

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}
