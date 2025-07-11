import sqlite3
import re
from colorama import Fore, init
from tabulate import tabulate

init(autoreset=True)


### funcion insertar producto

def insertar_producto(nombre, descripcion, precio_input, id_categoria):
    """
    Inserta un nuevo producto en la base 'inventario.db', validando todos los campos.
    """

    # Validación del nombre
    patron = "^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s\-]+$"
    if not re.match(patron, nombre.strip()) or len(nombre.strip()) > 50:
        print(Fore.RED + "❌ Nombre inválido. Sin caracteres especiales y máximo 50 caracteres.")
        return

    # Validación de descripción
    if len(descripcion.strip()) == 0 or len(descripcion.strip()) > 250:
        print(Fore.RED + "❌ Descripción inválida. Debe tener entre 1 y 250 caracteres.")
        return

    try:
        precio = float(precio_input)
        if precio < 0:
            print(Fore.RED + "❌ El precio debe ser positivo.")
            return

        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("BEGIN TRANSACTION")

        # Verificar si la categoría existe
        cursor.execute("SELECT nombre FROM categorias WHERE id = ?", (id_categoria,))
        categoria_encontrada = cursor.fetchone()
        if not categoria_encontrada:
            print(Fore.RED + f"❌ La categoría con ID {id_categoria} no existe.")
            return

        # Insertar producto
        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, precio, id_categoria)
            VALUES (?, ?, ?, ?)
        ''', (nombre.strip(), descripcion.strip(), precio, id_categoria))

        conexion.commit()
        print(Fore.GREEN + f"✅ Producto '{nombre.strip()}' agregado con éxito en la categoría '{categoria_encontrada[0]}'.")

    except ValueError:
        print(Fore.RED + "❌ Precio inválido. Usá un número como 25.50.")
        if 'conexion' in locals():
            conexion.rollback()

    except sqlite3.Error as e:
        print(Fore.RED + f"❌ Error en la base de datos: {e}")
        if 'conexion' in locals():
            conexion.rollback()

    finally:
        if 'conexion' in locals():
            conexion.close()

### funcion visualizar productos

def consultar_todos_productos():
    """
    Consulta todos los productos en la base inventario.db y muestra categoría con JOIN.
    """
    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()

        consulta = '''
            SELECT productos.id, productos.nombre, productos.descripcion,
            productos.precio, categorias.nombre AS categoria
            FROM productos
            JOIN categorias ON productos.id_categoria = categorias.id
        '''

        cursor.execute(consulta)
        productos = cursor.fetchall()

        if productos:
            print("\n📦 Productos registrados:")
            print(tabulate(
                productos,
                headers=["ID", "Nombre", "Descripción", "Precio ($)", "Categoría"],
                tablefmt="fancy_grid",
                floatfmt=".2f"
            ))
        else:
            print(Fore.YELLOW + "ℹ️ No hay productos registrados en la base.")

    except sqlite3.Error as e:
        print(Fore.RED + f"❌ Error en la consulta: {e}")

    finally:
        if 'conexion' in locals():
            conexion.close()

### funcion para actualizar el producto por Id de producto

def actualizar_producto_por_id(id_producto):
    import sqlite3
    import re
    from tabulate import tabulate
    from colorama import Fore, init
    init(autoreset=True)

    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("BEGIN TRANSACTION")

        # Obtener datos actuales
        cursor.execute('''
            SELECT productos.id, productos.nombre, productos.descripcion,
            productos.precio, productos.id_categoria, categorias.nombre
            FROM productos
            JOIN categorias ON productos.id_categoria = categorias.id
            WHERE productos.id = ?
        ''', (id_producto,))
        producto = cursor.fetchone()

        if not producto:
            print(Fore.RED + f"❌ No existe un producto con ID {id_producto}.")
            return

        print(Fore.CYAN + "\n🔍 Producto actual:")
        print(tabulate([producto], headers=["ID", "Nombre", "Descripción", "Precio ($)", "ID Cat.", "Categoría"],
        tablefmt="fancy_grid", floatfmt=".2f"))

        # Inputs opcionales
        print(Fore.BLUE + "\n📝 Ingresá nuevos datos o presioná Enter para mantener el valor actual:")

        nombre_input = input(f"📛 Nombre [{producto[1]}]: ").strip()
        nombre_final = nombre_input if nombre_input else producto[1]

        descripcion_input = input(f"📝 Descripción [{producto[2]}]: ").strip()
        descripcion_final = descripcion_input if descripcion_input else producto[2]

        precio_input = input(f"💲 Precio [{producto[3]}]: ").strip()
        try:
            precio_final = float(precio_input) if precio_input else producto[3]
            if precio_final < 0:
                print(Fore.RED + "❌ El precio no puede ser negativo.")
                return
        except ValueError:
            print(Fore.RED + "❌ Precio inválido.")
            return

        # Mostrar categorías
        cursor.execute("SELECT id, nombre FROM categorias")
        categorias = cursor.fetchall()
        print(Fore.CYAN + "\n🗂️ Categorías disponibles:")
        print(tabulate(categorias, headers=["ID", "Nombre"], tablefmt="grid"))

        categoria_input = input(f"🔢 ID de categoría [{producto[4]}]: ").strip()
        try:
            categoria_final = int(categoria_input) if categoria_input else producto[4]
        except ValueError:
            print(Fore.RED + "❌ ID de categoría inválido.")
            return

        # Validaciones
        if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s\-]+$", nombre_final) or len(nombre_final) > 50:
            print(Fore.RED + "❌ Nombre inválido.")
            return
        if len(descripcion_final) > 250 or len(descripcion_final) == 0:
            print(Fore.RED + "❌ Descripción inválida.")
            return

        cursor.execute("SELECT nombre FROM categorias WHERE id = ?", (categoria_final,))
        categoria_nombre = cursor.fetchone()
        if not categoria_nombre:
            print(Fore.RED + f"❌ La categoría con ID {categoria_final} no existe.")
            return

        # Actualizar
        cursor.execute('''
            UPDATE productos
            SET nombre = ?, descripcion = ?, precio = ?, id_categoria = ?
            WHERE id = ?
        ''', (nombre_final.strip(), descripcion_final.strip(), precio_final, categoria_final, id_producto))
        conexion.commit()

        # Mostrar resumen final
        print(Fore.GREEN + f"\n✅ Producto ID {id_producto} actualizado correctamente.\n")
        producto_final = (id_producto, nombre_final, descripcion_final, precio_final, categoria_final, categoria_nombre[0])
        print(tabulate([producto_final], headers=["ID", "Nombre", "Descripción", "Precio ($)", "ID Cat.", "Categoría"],
        tablefmt="fancy_grid", floatfmt=".2f"))

    except sqlite3.Error as e:
        print(Fore.RED + f"❌ Error en la base de datos: {e}")
        if 'conexion' in locals():
            conexion.rollback()
    finally:
        if 'conexion' in locals():
            conexion.close()


# Funcion para eliminar un producto por id de producto.

def eliminar_producto_por_id(id_producto):
    """
    Elimina un producto por su ID, con confirmación visual previa.
    """
    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("BEGIN TRANSACTION")

        cursor.execute('''
            SELECT productos.id, productos.nombre, productos.descripcion,
            productos.precio, categorias.nombre AS categoria
            FROM productos
            JOIN categorias ON productos.id_categoria = categorias.id
            WHERE productos.id = ?
        ''', (id_producto,))
        producto = cursor.fetchone()

        if not producto:
            print(Fore.YELLOW + f"ℹ️ No se encontró producto con ID {id_producto}.")
            return

        print("\n🗑️ Producto a eliminar:")
        print(tabulate([producto], headers=["ID", "Nombre", "Descripción", "Precio ($)", "Categoría"],
                tablefmt="fancy_grid", floatfmt=".2f"))

        confirmacion = input(Fore.RED + "\n⚠️ ¿Estás seguro que querés eliminar este producto? (s/n): ").strip().lower()
        if confirmacion != "s":
            print(Fore.YELLOW + "❎ Eliminación cancelada.")
            return

        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conexion.commit()
        print(Fore.GREEN + f"✅ Producto ID {id_producto} eliminado correctamente.")

    except sqlite3.Error as e:
        print(Fore.RED + f"❌ Error al eliminar el producto: {e}")
        if 'conexion' in locals():
            conexion.rollback()
    finally:
        if 'conexion' in locals():
            conexion.close()


# Consulta de producto por ID

def consultar_producto_por_id(id_buscado):
    """
    Consulta un producto por su ID, validando que sea un número válido.
    """

    # Validación de entrada
    try:
        id_buscado = int(id_buscado)
        if id_buscado <= 0:
            print(Fore.RED + "❌ El ID debe ser un número entero positivo.")
            return
    except ValueError:
        print(Fore.RED + "❌ ID inválido. Ingresá solo números enteros como 1, 2, 3...")
        return

    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("BEGIN TRANSACTION")

        cursor.execute('''
            SELECT productos.id, productos.nombre, productos.descripcion,
            productos.precio, categorias.nombre AS categoria
            FROM productos
            JOIN categorias ON productos.id_categoria = categorias.id
            WHERE productos.id = ?
        ''', (id_buscado,))
        producto = cursor.fetchall()

        if producto:
            print("\n🔍 Producto encontrado por ID:")
            print(tabulate(producto, headers=["ID", "Nombre", "Descripción", "Precio ($)", "Categoría"], tablefmt="fancy_grid", floatfmt=".2f"))
        else:
            print(Fore.YELLOW + f"ℹ️ No se encontró producto con ID {id_buscado}.")

        conexion.commit()

    except sqlite3.Error as e:
        print(Fore.RED + f"❌ Error en la consulta por ID: {e}")
        if 'conexion' in locals():
            conexion.rollback()

    finally:
        if 'conexion' in locals():
            conexion.close()


# Busqueda por nombre de producto

def buscar_productos_por_nombre(nombre_parcial):
    """
    Busca productos que coincidan parcialmente con el nombre ingresado.
    """
    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("BEGIN TRANSACTION")

        patron = f"%{nombre_parcial.strip()}%"  # Patrón tipo LIKE
        cursor.execute('''
            SELECT productos.id, productos.nombre, productos.descripcion,
            productos.precio, categorias.nombre
            FROM productos
            JOIN categorias ON productos.id_categoria = categorias.id
            WHERE productos.nombre LIKE ?
        ''', (patron,))
        resultados = cursor.fetchall()

        if resultados:
            print(Fore.CYAN + f"\n🔎 Resultados para nombre que contiene '{nombre_parcial}':")
            print(tabulate(resultados, headers=["ID", "Nombre", "Descripción", "Precio ($)", "Categoría"],
            tablefmt="fancy_grid", floatfmt=".2f"))
        else:
            print(Fore.YELLOW + "ℹ️ No se encontraron productos con ese nombre.")

        conexion.commit()

    except sqlite3.Error as e:
        print(Fore.RED + f"❌ Error en la búsqueda por nombre: {e}")
        if 'conexion' in locals():
            conexion.rollback()
    finally:
        if 'conexion' in locals():
            conexion.close()

# Busqueda por categoria de producto

def buscar_productos_por_categoria():
    """
    Lista categorías y permite buscar productos según la seleccionada por el usuario.
    """
    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("BEGIN TRANSACTION")

        # Mostrar lista de categorías
        cursor.execute("SELECT id, nombre FROM categorias")
        categorias = cursor.fetchall()

        if not categorias:
            print(Fore.YELLOW + "ℹ️ No hay categorías definidas.")
            return

        print(Fore.CYAN + "\n📚 Categorías disponibles:")
        print(tabulate(categorias, headers=["ID", "Nombre"], tablefmt="grid"))

        # Elegir categoría
        id_categoria = input(Fore.BLUE + "\n📝 Ingresá el ID de la categoría a consultar: ")
        try:
            id_categoria = int(id_categoria)
            if id_categoria <= 0:
                print(Fore.RED + "❌ ID inválido. Debe ser un número positivo.")
                return
        except ValueError:
            print(Fore.RED + "❌ Entrada no válida. Usá sólo números.")
            return

        # Mostrar productos de esa categoría
        cursor.execute('''
            SELECT productos.id, productos.nombre, productos.descripcion,
            productos.precio, categorias.nombre
            FROM productos
            JOIN categorias ON productos.id_categoria = categorias.id
            WHERE categorias.id = ?
        ''', (id_categoria,))
        productos = cursor.fetchall()

        if productos:
            print(Fore.CYAN + f"\n📦 Productos en la categoría '{productos[0][4]}':")
            print(tabulate(productos, headers=["ID", "Nombre", "Descripción", "Precio ($)", "Categoría"],
            tablefmt="fancy_grid", floatfmt=".2f"))
        else:
            print(Fore.YELLOW + "ℹ️ No hay productos registrados en esa categoría.")

        conexion.commit()

    except sqlite3.Error as e:
        print(Fore.RED + f"❌ Error en la búsqueda por categoría: {e}")
        if 'conexion' in locals():
            conexion.rollback()
    finally:
        if 'conexion' in locals():
            conexion.close()

# funcion para mostrar las categorias
def mostrar_categorias_disponibles():
    """
    Consulta y muestra todas las categorías registradas en inventario.db.
    """
    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()

        cursor.execute("SELECT id, nombre FROM categorias")
        categorias = cursor.fetchall()
        conexion.close()

        if categorias:
            print(Fore.CYAN + "\n🗂️ Categorías disponibles:")
            print(tabulate(categorias, headers=["ID", "Nombre"], tablefmt="grid"))
        else:
            print(Fore.YELLOW + "ℹ️ No hay categorías registradas.")
    except sqlite3.Error as e:
        print(Fore.RED + f"❌ Error al consultar categorías: {e}")
