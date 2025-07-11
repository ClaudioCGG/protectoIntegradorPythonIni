from crud import (
    mostrar_categorias_disponibles,
    insertar_producto,
    consultar_todos_productos,
    consultar_producto_por_id,
    buscar_productos_por_nombre,
    buscar_productos_por_categoria,
    actualizar_producto_por_id,
    eliminar_producto_por_id
)
import time # Para crear transiciones mas sutiles de menus
import os

def mostrar_menu():
    while True:
        print("\n✨ Por favor, digite una opción para continuar. 🚀")
        time.sleep(0.5)
        print("1. ➕ Insertar producto")
        print("2. 👓 Consultar todos los productos")
        print("3. Buscar por ID")
        print("4. Buscar por nombre parcial")
        print("5. Buscar por categoría")
        print("6. 📝 Actualizar producto")
        print("7. ❌ Eliminar producto")
        print("8. Consultar stock por producto")
        print("9. Filtrar stock por cantidad")
        print("10. Registrar movimiento de stock (ingreso o salida)")


        print("\n0. Salir")

        opcion = input("\n👉 Ingresá una opción: ")

        if opcion == "1":
            print("\n📦 INGRESO DE NUEVO PRODUCTO")

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
            id_actualizar = input("🔍 Ingresá el ID del producto a actualizar: ").strip()
            actualizar_producto_por_id(id_actualizar)

        elif opcion == "7":
            eliminar_producto_por_id(input("🗑️ ID a eliminar: "))

        elif opcion == "8":
            print("\n🔎 CONSULTAR STOCK POR PRODUCTO")
            id_producto = input("📦 Ingresá el ID del producto a consultar: ").strip()

            from crud import consultar_stock_por_producto
            consultar_stock_por_producto(id_producto)

        elif opcion == "9":
            print("\n📊 FILTRAR STOCK POR RANGO DE CANTIDAD")

            desde = input("🔢 Cantidad mínima (ENTER para 0): ")
            hasta = input("🔢 Cantidad máxima: ")

            from crud import filtrar_stock_por_rango_cantidad
            filtrar_stock_por_rango_cantidad(desde, hasta)

        elif opcion == "10":
            print("\n📥 REGISTRAR MOVIMIENTO DE STOCK")

            id_producto = input("🔢 ID del producto: ").strip()
            tipo = input("📤 Tipo de movimiento (ingreso/salida): ").strip().lower()
            cantidad = input("🔢 Cantidad (solo número entero): ").strip()
            origen = input("📝 Origen o motivo (ej. compra, venta, devolución): ").strip()

            from crud import registrar_movimiento_stock
            registrar_movimiento_stock(id_producto, cantidad, tipo, origen)


        elif opcion == "0":
            time.sleep(0.5)
            os.system('cls')
            print("\n\t\t👋 👋 👋 👋 👋 👋 👋 👋 👋 👋 👋 👋 👋")
            print("\n\t\t👋 👋 👋 👋 ¡Hasta luego! 👋 👋 👋 👋 👋")
            print("\n\t\t👋 👋 👋 👋 👋 👋 👋 👋 👋 👋 👋 👋 👋\n\n")
            break

        else:
            print("⚠️ Opción inválida. Probá de nuevo.")