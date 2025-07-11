import sqlite3
from colorama import Fore, Style, init
init(autoreset=True)

# funcion para crear la base de datos
def crear_base_datos(nombre_db):

    """
        Solicita un nombre para la creacion de la base de datos, validando la entrada. 
    """

    try:
        conexion = sqlite3.connect(nombre_db)
        cursor = conexion.cursor()
        cursor.execute("BEGIN TRANSACTION")

        conexion.commit()
        print(Fore.GREEN + f"✅ Base de datos '{nombre_db}' creada correctamente.")

    except sqlite3.Error as e:
        print(Fore.RED + f"❌ Error al crear la base de datos: {e}")
        if 'conexion' in locals():
            conexion.rollback()

    finally:
        if 'conexion' in locals():
            conexion.close()


# funcion para crear la tabla productos
def crear_tabla_producto():

    """
        Crea la tabla productos en la base de datos inventario.db
    """

    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("BEGIN TRANSACTION")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL CHECK (LENGTH(nombre) <= 50),
                descripcion TEXT NOT NULL CHECK (LENGTH(descripcion) <= 250),
                precio REAL NOT NULL CHECK (precio >= 0),
                id_categoria INTEGER NOT NULL,
                FOREIGN KEY (id_categoria) REFERENCES categorias(id)
            )
        ''')

        conexion.commit()
        print(Fore.GREEN + "✅ Tabla 'productos' creada correctamente.")

    except sqlite3.Error as e:
        print(Fore.RED + f"❌ Error al crear la tabla: {e}")
        if 'conexion' in locals():
            conexion.rollback()

    finally:
        if 'conexion' in locals():
            conexion.close()


# funcion para crear la tabla categorias
def crear_tabla_categorias():
    """
    Crea la tabla 'categorias' en inventario.db con tres categorías iniciales.
    """
    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("BEGIN TRANSACTION")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT UNIQUE NOT NULL CHECK (LENGTH(nombre) <= 20)
            )
        ''')

        # Insertar categorías base — evita duplicados con OR IGNORE
        categorias_base = ["Electrónica", "Alimentos", "Libros"]
        for categoria in categorias_base:
            cursor.execute("INSERT OR IGNORE INTO categorias (nombre) VALUES (?)", (categoria,))

        conexion.commit()
        print(Fore.GREEN + "✅ Tabla 'categorias' creada con éxito y categorías iniciales insertadas.")

    except sqlite3.Error as e:
        print(Fore.RED + f"❌ Error al crear la tabla de categorías: {e}")
        if 'conexion' in locals():
            conexion.rollback()

    finally:
        if 'conexion' in locals():
            conexion.close()

### funcion para crear tabla stock 
def crear_tabla_stock():
    """
    Crea la tabla 'stock' en inventario.db para registrar ingresos de productos.
    """
    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("BEGIN TRANSACTION")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stock (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_producto INTEGER NOT NULL,
                fecha TEXT NOT NULL,
                cantidad INTEGER NOT NULL CHECK (cantidad >= 0),
                origen TEXT,
                tipo TEXT CHECK (tipo IN ('ingreso', 'salida')),
                FOREIGN KEY (id_producto) REFERENCES productos(id)
            )
        ''')

        conexion.commit()
        print(Fore.GREEN + "✅ Tabla 'stock' creada correctamente.")

    except sqlite3.Error as e:
        print(Fore.RED + f"❌ Error al crear la tabla 'stock': {e}")
        if 'conexion' in locals():
            conexion.rollback()
    finally:
        if 'conexion' in locals():
            conexion.close()
