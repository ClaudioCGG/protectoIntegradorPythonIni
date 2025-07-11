import sqlite3
from colorama import Fore, Style, init

init(autoreset=True)

def crear_tabla_alumnos():
    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute("BEGIN TRANSACTION")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alumnos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                edad INTEGER CHECK (edad >= 5 AND edad <= 120),
                curso TEXT NOT NULL,
                email TEXT UNIQUE CHECK (email LIKE '%@%')
            )
        ''')

        conexion.commit()
        print(Fore.GREEN + "✅ Tabla 'alumnos' creada correctamente.")

    except sqlite3.Error as e:
        print(Fore.RED + f"❌ Error al crear la tabla: {e}")
        if 'conexion' in locals():
            conexion.rollback()

    finally:
        if 'conexion' in locals():
            conexion.close()