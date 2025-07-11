from crud import (
    insertar_producto,
    consultar_todos_productos,
    consultar_producto_por_id,
    buscar_productos_por_nombre,
    buscar_productos_por_categoria,
    actualizar_producto_por_id,
    eliminar_producto_por_id,
    mostrar_categorias_disponibles
)
import time # Para crear transiciones mas sutiles de menus

def mostrar_menu():
    while True:
        print("\n✨ Por favor, digite una opción para continuar. 🚀")
        time.sleep(0.5)
        print("1. Insertar producto")
        print("2. Consultar todos los productos")
        print("3. Buscar por ID")
        print("4. Buscar por nombre parcial")
        print("5. Buscar por categoría")
        print("6. Actualizar producto")
        print("7. Eliminar producto")
        print("0. Salir")

        opcion = input("\n👉 Ingresá una opción: ")

        if opcion == "1":
            print("\n📦 INGRESO DE NUEVO PRODUCTO")

            from crud import mostrar_categorias_disponibles, insertar_producto

            nombre = input("📛 Nombre del producto: ").strip()
            descripcion = input("📝 Descripción del producto: ").strip()
            precio = input("💲 Precio (por ejemplo 49.99): ").strip()

            mostrar_categorias_disponibles()
            categoria_id = input("🗂️ ID de categoría a asignar: ").strip()

            insertar_producto(nombre, descripcion, precio, categoria_id)

        elif opcion == "2":
            consultar_todos_productos()
        elif opcion == "3":
            consultar_producto_por_id(input("🔍 ID a buscar: "))
        elif opcion == "4":
            buscar_productos_por_nombre(input("🔍 Nombre parcial: "))
        elif opcion == "5":
            buscar_productos_por_categoria()
        elif opcion == "6":
            print("\n✏️ ACTUALIZAR PRODUCTO")

            from crud import mostrar_categorias_disponibles, actualizar_producto_por_id

            id_actualizar = input("🔍 Ingresá el ID del producto a actualizar: ").strip()
            nuevo_nombre = input("📛 Nuevo nombre: ").strip()
            nueva_descripcion = input("📝 Nueva descripción: ").strip()
            nuevo_precio = input("💲 Nuevo precio: ").strip()

            mostrar_categorias_disponibles()
            nueva_categoria = input("🗂️ Nuevo ID de categoría: ").strip()

            actualizar_producto_por_id(id_actualizar, nuevo_nombre, nueva_descripcion, nuevo_precio, nueva_categoria)
        elif opcion == "7":
            eliminar_producto_por_id(input("🗑️ ID a eliminar: "))
        elif opcion == "0":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida. Probá de nuevo.")