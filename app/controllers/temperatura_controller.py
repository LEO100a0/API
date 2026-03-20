from app.database import get_connection

# 🔹 INSERT
def guardar_temperatura(valor: float):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO temperaturas (valor) VALUES (%s)",
        (valor,)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return {"mensaje": "Guardado en DB", "valor": valor}


# 🔹 SELECT
def obtener_datos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, valor FROM temperaturas")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    datos = [{"id": r[0], "valor": r[1]} for r in rows]

    n = len(datos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if datos[j]["valor"] < datos[j + 1]["valor"]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]

    return {"datos": datos}
    
