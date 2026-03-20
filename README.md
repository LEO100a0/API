# 🚀 API de Temperatura con FastAPI

Este proyecto es una API básica desarrollada con **FastAPI** que permite registrar y consultar datos de temperatura.
Está diseñada como práctica para aprender a desplegar APIs en la nube (Render).

---

## 📁 Estructura del proyecto

```
mi-api/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   └── controllers/
│       └── temperatura_controller.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Requisitos

* Python 3.8+
* pip

---

## 📦 Instalación

1. Clonar el repositorio:

```
git clone https://github.com/tu-usuario/mi-api.git
cd mi-api
```

2. Instalar dependencias:

```
pip install -r requirements.txt
```

---

## ▶️ Ejecutar en local

```
uvicorn app.main:app --reload
```

Abrir en el navegador:

👉 http://127.0.0.1:8000/docs

---

## 📌 Endpoints disponibles

### 🔹 GET /

Verifica que la API está funcionando

**Respuesta:**

```
{
  "message": "API funcionando 🚀"
}
```

---

### 🔹 POST /temperatura

Guarda un valor de temperatura

**Ejemplo:**

```
/temperatura?valor=25
```

---

### 🔹 GET /datos

Obtiene todas las temperaturas registradas

---

### 🔹 GET /datos?min_temp=20&max_temp=30

Filtra temperaturas por rango

**Parámetros opcionales:**

* `min_temp`: temperatura mínima
* `max_temp`: temperatura máxima

---

## 🧠 Conceptos aprendidos

* Creación de APIs con FastAPI
* Separación por capas (routes + controllers)
* Uso de parámetros en GET (query params)
* Uso de Swagger (/docs)
* Despliegue en la nube (Render)

---

## ☁️ Deploy en Render

1. Subir el proyecto a GitHub
2. Crear un nuevo servicio en Render
3. Configurar:

**Build Command:**

```
pip install -r requirements.txt
```

**Start Command:**

```
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

---

## 💡 Mejoras futuras

* Conectar a base de datos (SQLite o PostgreSQL)
* Agregar validación con Pydantic
* Implementar autenticación
* Integrar con dispositivos IoT (ESP32)

---

## 👨‍💻 Autor

Proyecto académico - Curso de Tecnología de Información II
