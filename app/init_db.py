from app.database import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS temperaturas (
            id SERIAL PRIMARY KEY,
            valor FLOAT
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()
