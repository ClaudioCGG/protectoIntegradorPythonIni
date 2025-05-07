""" print("¡Bienvenides al mundo de Python!") """
#############################################################################################################
# BASE DE DATOS CON LISTA DE PRODUCTOS INICIAL
#############################################################################################################

productos = [
    {"codigo": 101, "nombre": "Manzanas", "precio": 150.00},
    {"codigo": 102, "nombre": "Peras", "precio": 120.00},
    {"codigo": 103, "nombre": "Naranjas", "precio": 180.00},
    {"codigo": 104, "nombre": "Naranjas", "precio": 180.00},
    {"codigo": 105, "nombre": "Naranjas", "precio": 180.00},
    {"codigo": 106, "nombre": "Naranjas", "precio": 180.00}
]




# CREATE Lista para almacenar productos

while True:
    # Solicitar datos del nuevo producto
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")

    # Convertir precio a float y código a entero si es necesario
    try:
        codigo = int(codigo)
        precio = float(precio)
    except ValueError:
        print("Error: Código debe ser un número entero y precio un número decimal.")
        continue  # Volver a solicitar el producto

    # Crear diccionario del producto
    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio
    }

    # Agregar a la lista
    productos.append(nuevo_producto)

    # Preguntar si se quiere agregar más productos
    continuar = input("¿Desea agregar otro producto? (s/n): ").lower()
    if continuar != "s":
        break

print("\nLista de productos:")
for producto in productos:
    print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}")

""" 
# READ 
# # # READ: Lista Completa
print("\nLista de productos:")
for producto in productos:
    print(f"Código: {producto['codigo']}, Nombre: {producto['nombre_producto']}, Precio: ${producto['precio']:.2f}")


# # # READ: Producto Especifico
# Pedir input al usuario
entrada = input("Ingrese el código o nombre del producto: ").lower()  # Convertimos a minúsculas

# Crear una lista para almacenar los resultados
productos_encontrados = []

# Recorrer la lista y buscar coincidencias
for producto in productos:
    if str(producto["codigo"]) in entrada or producto["nombre"].lower() in entrada:
        productos_encontrados.append(producto)

# Mostrar resultados
if productos_encontrados:
    print("\nResultados encontrados:")
    for producto in productos_encontrados:
        print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}")
else:
    print("No se encontraron productos.")

# # # READ: Ordenar por precio A- B
productos_ordenados_por_precio = sorted(productos, key=lambda p: p["precio"])

print("\nProductos ordenados por precio:")
for producto in productos_ordenados_por_precio:
    print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}")

# # # READ: Ordenar por precio B - A
productos_ordenados_por_precio_desc = sorted(productos, key=lambda p: p["precio"], reverse=True)

print("\nProductos ordenados por precio (mayor a menor):")
for producto in productos_ordenados_por_precio_desc:
    print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}")


# # # READ: Ordenar por nombre A- B
productos_ordenados_por_nombre = sorted(productos, key=lambda p: p["nombre"])

print("\nProductos ordenados por nombre:")
for producto in productos_ordenados_por_nombre:
    print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}")

# # # READ: Ordenar por nombre B - A
productos_ordenados_por_nombre_desc = sorted(productos, key=lambda p: p["nombre"], reverse=True)

print("\nProductos ordenados por nombre (Z a A):")
for producto in productos_ordenados_por_nombre_desc:
    print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}")


# DELETE

# Validar que el usuario ingrese un número válido
while True:
    entrada = input("Ingrese el código del producto a eliminar: ")
    if entrada.isdigit():  # Verificar si solo contiene números
        codigo_a_eliminar = int(entrada)
        break  # Salimos del bucle si es válido
    else:
        print("Error: Debes ingresar un número entero válido.")

# Filtrar la lista excluyendo el producto con el código dado
productos = [producto for producto in productos if producto["codigo"] != codigo_a_eliminar]

# Mostrar la lista actualizada
 """

codigo_buscado = 102  # Código del producto que queremos buscar

# Buscar el producto con ese código y obtener su precio con .get()
precio_producto = next((p.get("precio") for p in productos if p.get("codigo") == codigo_buscado), "No encontrado")

print(f"El precio del producto con código {codigo_buscado} es: {precio_producto}")