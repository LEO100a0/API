from fastapi import APIRouter
from app.controllers import temperatura_controller

router = APIRouter()

# 🔹 POST → guardar
@router.post("/temperatura")
def guardar(valor: float):
    return temperatura_controller.guardar_temperatura(valor)

# 🔹 GET → obtener datos
@router.get("/datos")
def listar():
    return temperatura_controller.obtener_datos()
