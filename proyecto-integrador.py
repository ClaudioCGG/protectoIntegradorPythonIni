""" 
    *** METODOLOGÍA ***
Crear una carpeta en drive que contenga los archivos y carpetas que conforman tu proyecto. Compartir el link en el apartado de entrega en
el Campus Virtual. Al final de la cursada, serás evaluado mediante la entrega de un Proyecto Integrador, esta última instancia evaluativa es
de carácter obligatorio para finalizar el curso y obtener la certificación.  Este proyecto se construirá de manera progresiva a lo largo de
la cursada, combinando la "Pre - Entrega" y la resolución de los "Ejercicios Prácticos" siguientes presentes en las clases. Las "Rubricas de
Evaluación" del Proyecto final integrador estará constituido en gran medida por los "Ejercicios Prácticos" y las "Rutas de Avance" a lo largo
 de la cursada. Entrega: En la Clase N° 15  se discutirán las rubricas a evaluar. Tendrás 7 dias de corrido para realizar la entrega. """

"""
    *** PROYECTO ***
En Techlab recibimos un nuevo proyecto de un cliente que requiere el desarrollo de una aplicación en Python capaz de gestionar información de
clientes, productos y pedidos. La solución deberá incluir funcionalidades para registrar, consultar, actualizar y eliminar datos, utilizando
una base de datos SQLite integrada con el programa.
"""

"""
### Ruta de avance hacia el Trabajo Final Integrador (TFI) ### 

Ahora que llegaste a la clase 4, estás en una posición ideal para comenzar a trabajar en los cimientos del programa que desarrollarás como 
parte del Trabajo Final Integrador (TFI). Como sabés, en este proyecto, vas a crear una aplicación en Python que gestione información sobre 
los productos de una tienda. Es importante que empieces a planificar cómo integrar lo que aprendiste hasta ahora.
Con los conocimientos adquiridos en las clases anteriores, ya podés diseñar la estructura básica del programa. Por ejemplo, podés usar cadenas
de texto para almacenar nombres, descripciones y cualquier otro dato textual. También podés aplicar los métodos de cadenas para validar y 
formatear la información que se ingrese por la terminal, como convertir todo a minúsculas o eliminar espacios en blanco innecesarios.
La validación de las entradas es otro aspecto fundamental que podés abordar con lo aprendido en las clases 3 y 4. Las estructuras 
condicionales como if, elif y match te permiten manejar diferentes escenarios. Por ejemplo, podés validar que un correo electrónico incluya
 el carácter @ o que una edad ingresada sea un número positivo. Esto hace que tu programa sea más robusto y resistente a errores de ingreso.
También es importante planificar cómo va a interactuar el usuario con tu programa. Podés usar lo que aprendiste para mostrar menús simples 
que permitan elegir entre distintas opciones, como registrar un cliente o consultar los datos ingresados. Pensá en aplicar condicionales y 
métodos de cadenas para hacer más clara y amigable la presentación de estas opciones.
Aunque todavía no aprendiste a trabajar con bases de datos ni a guardar datos de manera persistente, no te preocupes. Más adelante en el 
curso, vamos a integrar estas herramientas con bases de datos para completar la funcionalidad del proyecto.
Como tarea concreta, te sugerimos que crees un programa que solicite los datos de un producto y los muestre en formato de tarjeta o ficha, 
utilizando f-Strings para formatear la salida. Aprovechá los métodos de cadenas para validar las entradas y asegurarte de que estén en el 
formato correcto.
Experimentá. Recordá que cada paso que avances ahora va a facilitar el desarrollo del proyecto final. Es mejor empezar con algo pequeño e ir 
construyendo sobre eso, en lugar de intentar resolver todo de una sola vez.
 """

# Diagrama: https://drive.google.com/file/d/1_kmaWON2xHdlvu21pZvtc5tqPp8wHA1U/view?usp=sharing


#############################################################################################################
############################### BASE DE DATOS CON LISTA DE PRODUCTOS INICIAL ################################
#############################################################################################################

# BASE DE DATOS PRODUCTOS INICIAL
productos = [
    {"codigo": 101, "nombre": "Celular", "precio": 400, "descripcion": "Smartphone 2025", "categoria": "Tecnologia"},
    {"codigo": 102, "nombre": "Notebook", "precio": 1000, "descripcion": "Ultrapotente Gamer", "categoria": "Tecnologia"},
    {"codigo": 103, "nombre": "Smart TV", "precio": 300, "descripcion": "Smart TV Full HD", "categoria": "Tecnologia"},
    {"codigo": 104, "nombre": "Robot Aspiradora", "precio": 250, "descripcion": "Limpia, tradea y desinfecta", "categoria": "Pequeños electrodomésticos"},
    {"codigo": 105, "nombre": "Batidora", "precio": 80, "descripcion":"Batidora Inteligente", "categoria": "Pequeños electrodomésticos"},
    {"codigo": 106, "nombre": "Microondas", "precio": 150, "descripcion": "Potente y autolimpieza", "categoria": "Cocina"}
]

# BASE DE USUARIOS INICIAL
clientes = [
    {"ID": 1, "Nombre": "Usuario", "Apellido": "Apellido1", "Email": "usuario.apellido1@gmail.com", "Fecha de Nacimiento": "01/03/1980", "Perfil": "usuario", "Password": "Usuario123"},
    {"ID": 2, "Nombre": "Vendedor", "Apellido": "Apellido2", "Email": "vendedor.apellido2@gmail.com", "Fecha de Nacimiento": "02/01/1980", "Perfil": "vendedor", "Password": "Vendedor123"},
    {"ID": 3, "Nombre": "Administrador", "Apellido": "Apellido3", "Email": "administrador.apellido3@gmail.com", "Fecha de Nacimiento": "03/01/1980", "Perfil": "administrador", "Password": "Admin1234"}
]

# BASE DE PEDIDOS INICIAL
pedidos = [
    {
        "Nro Pedido": 10,
        "Fecha Pedido": "07/05/2025",
        "Detalle Pedido": [
            {"Código Producto": 101, "Cantidad": 2, "Precio Unitario": 400, "Precio Total": 800},
            {"Código Producto": 103, "Cantidad": 1, "Precio Unitario": 300, "Precio Total": 300}
        ],
        "Estado Pedido": "Pendiente",
        "Observación": ""
    },
    {
        "Nro Pedido": 11,
        "Fecha Pedido": "06/05/2025",
        "Detalle Pedido": [
            {"Código Producto": 102, "Cantidad": 1, "Precio Unitario": 1000, "Precio Total": 1000}
        ],
        "Estado Pedido": "Cancelado",
        "Observación": "Cliente se arrepintió de la compra."
    },
    {
        "Nro Pedido": 12,
        "Fecha Pedido": "05/05/2025",
        "Detalle Pedido": [
            {"Código Producto": 104, "Cantidad": 3, "Precio Unitario": 250, "Precio Total": 750}
        ],
        "Estado Pedido": "Cancelado",
        "Observación": "No hay stock disponible del producto."
    },
    {
        "Nro Pedido": 13,
        "Fecha Pedido": "04/05/2025",
        "Detalle Pedido": [
            {"Código Producto": 106, "Cantidad": 1, "Precio Unitario": 150, "Precio Total": 150}
        ],
        "Estado Pedido": "Enviado",
        "Observación": ""
    },

]


usuario_actual = None  # Al inicio, nadie está logueado

import datetime
import re  # Para validación de contraseñas

############################################################################################################
############################################ *** MENÚ INICIO *** ###########################################

while True:  # MENÚ INICIO

    print("╔═════════════════════════════════════════════════════════════╗")
    print("║  🎉 ¡BIENVENIDO AL PROYECTO INTEGRADOR PRE-ENTREGABLE! 🎉   ║")
    print("╚═════════════════════════════════════════════════════════════╝")
    print("\n✨ Por favor, digite una opción para continuar. 🚀")


    print("-" * 60)  # Puedes ajustar el número para ver cuándo corta la línea
    print("\n🔹 Menú de Inicio\n")
    print("\t1. 📝 Registrarse")
    print("\t2. 🔒 Iniciar Sesión")
    print("\t3. ❌ Salir")

    opcion_inicio = input("\nElegí una opción: ")

    ###########################################################################################
    #################################### SUB MENU REGISTRO ####################################
    if opcion_inicio == "1":

        ###

        while True:  # Validar nombre con espacios
            nombre = input("Ingresá tu nombre: ").strip()
            if re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ]+( [A-Za-zÁÉÍÓÚáéíóúÑñ]+)*$", nombre):
                break
            else:
                print("❌ Error: El nombre solo debe contener letras y espacios.")

        while True:  # Validar apellido con espacios
            apellido = input("Ingresá tu apellido: ").strip()
            if re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ]+( [A-Za-zÁÉÍÓÚáéíóúÑñ]+)*$", apellido):
                break
            else:
                print("❌ Error: El apellido solo debe contener letras y espacios.")

        while True:  # Validación del email
            email = input("Ingresá tu email: ").strip()
            if re.match(r"[^@]+@[^@]+\.[a-zA-Z]{2,}", email):
                break
            else:
                print("❌ Email inválido. Ingresá un email correcto.")

        while True:  # Validación de fecha de nacimiento
            nacimiento = input("Ingresá tu fecha de nacimiento (dd/mm/aaaa): ").strip()
            try:
                fecha_nac = datetime.datetime.strptime(nacimiento, "%d/%m/%Y")  # Convertir a fecha válida
                break  # Si es correcta, salir del bucle
            except ValueError:
                print("❌ Fecha inválida. Ingresá una fecha correcta.")

        while True:  # Validación de contraseña segura
            password = input("Ingresá una contraseña segura: ").strip()
            if (8 <= len(password) <= 20 and
                re.search(r'[A-Z]', password) and
                re.search(r'[a-z]', password) and
                re.search(r'[0-9]', password)):
                break
            else:
                print("❌ Contraseña inválida. Debe tener al menos 8 caracteres, incluir una mayúscula y un número.")



        # Buscar el último ID y sumar 1
        nuevo_id = max([c["ID"] for c in clientes], default=0) + 1

        # ALTA REGISTRO CLIENTE
        clientes.append({
            "ID": nuevo_id,
            "Nombre": nombre,
            "Apellido": apellido,
            "Fecha de Nacimiento": nacimiento,
            "Email": email,
            "Perfil": "usuario",  # Perfil por defecto
            "Password": password
        })

        usuario_actual = clientes[-1]  # Guarda el usuario logueado
        print(f"✅ ¡Registro exitoso! Bienvenido {nombre}!")

    ###########################################################################################
    ##################################### SUB MENU LOGIN ######################################
    elif opcion_inicio == "2":
        email = input("Ingresá tu email: ").strip()
        password = input("Ingresá tu contraseña: ").strip()

        for cliente in clientes: #**** mejora>  posiblemente la validacion verifica que exista el usuario y contraseña pero no valida que sea el mismo índice
            if cliente["Email"] == email and cliente["Password"] == password:
                usuario_actual = cliente
                print(f"✅ Inicio de sesión exitoso. Bienvenido, {cliente['Nombre']}.")
                break
        else:
            print("❌ Email o contraseña incorrectos.")
            continue  # Volver a pedir credenciales

    elif opcion_inicio == "3":  # SALIR DEL PROGRAMA
        print("\n\t\t🔚 ¡Hasta luego! 👋 👋 👋\n")
        break  # Finaliza el programa

    else:
        print("❌ Opción inválida.")
        continue  # Volver al menú

    ###########################################################################################
    ###################### MENÚ PRINCIPAL (solo si hay usuario logueado) ######################

    while usuario_actual:
        print("\n📌 Menú Principal\n")
        print("\t1. ✍   Mis Datos")
        print("\t2. 📦  Productos")
        print("\t3. 🛒  Pedidos")
        print("\t4. ❌  Cerrar Sesión")

        opcion_principal = input("\nElegí una opción: ")

        ###########################################################################################
        ########################## 1 SUB MENÚ MIS DATOS CRUD (actualizar o baja) ##################
        if opcion_principal == "1":
            while usuario_actual:
                print("\n👤 Gestión de Usuario\n")
                print("\t1. Ver mis datos")
                print("\t2. Modificar mis datos")
                print("\t3. Eliminar mi cuenta")
                print("\t4. Volver al menú principal\n")

                opcion_usuario = input("Elegí una opción: ")

                if opcion_usuario == "1":  # LEER DATOS DEL USUARIO
                    print("\n📌 Datos de tu perfil:")
                    print(f"Nombre: {usuario_actual['Nombre']}")
                    print(f"Apellido: {usuario_actual['Apellido']}")
                    print(f"Fecha de Nacimiento: {usuario_actual['Fecha de Nacimiento']}")
                    print(f"Perfil: {usuario_actual['Perfil']}")  # No se permite modificar
                    print("🔒 Email y ID protegidos (no modificables)")

                elif opcion_usuario == "2":  # MODIFICAR DATOS
                    usuario_actual["Nombre"] = input(f"Nuevo nombre ({usuario_actual['Nombre']}): ") or usuario_actual["Nombre"]
                    usuario_actual["Apellido"] = input(f"Nuevo apellido ({usuario_actual['Apellido']}): ") or usuario_actual["Apellido"]
                    usuario_actual["Fecha de Nacimiento"] = input(f"Nueva fecha de nacimiento ({usuario_actual['Fecha de Nacimiento']}): ") or usuario_actual["Fecha de Nacimiento"]
                    nueva_password = input("Nueva contraseña: ")

                    if nueva_password:
                        usuario_actual["Password"] = nueva_password  # Permitir cambio de contraseña

                    print("✅ Datos actualizados con éxito.")

                elif opcion_usuario == "3":  # ELIMINAR CUENTA
                    confirmar = input("⚠ ¿Estás seguro de eliminar tu cuenta? (Sí/No): ").strip().lower()

                    if confirmar == "sí":
                        clientes.remove(usuario_actual)  # Eliminar usuario de la lista
                        usuario_actual = None  # Cerrar sesión
                        print("🔴 Tu cuenta ha sido eliminada. Volviendo al menú de inicio...")
                        break  # Salir del menú de usuario y regresar al inicio

                    else:
                        print("❌ Cancelación de eliminación.")

                elif opcion_usuario == "4":  # VOLVER AL MENÚ PRINCIPAL
                    print("🔙 Volviendo al menú principal...")
                    break  

                else:
                    print("❌ Opción inválida, intentá de nuevo.")


        ###########################################################################################
        ###################V########### 2 SUB MENÚ PRODUCTOS CRUD #################################

        elif opcion_principal == "2":
            while True:
                print("\n📦 Gestión de Productos\n")
                print("\t1. Agregar producto")
                print("\t2. Ver productos") # Se podria mejorar agregando filtros de busqueda por categoria o precio
                print("\t3. Modificar producto")
                print("\t4. Eliminar producto")
                print("\t5. Salir\n")

                opcion_producto = input("Elegí una opción: ")

                if opcion_producto == "1":  # CREAR PRODUCTO
                    nombre = input("Nombre del producto: ").strip()
                    precio = input("Precio: ").strip()
                    descripcion = input("Descripción: ").strip()
                    categoria = input("Categoría: ").strip()

                    # Buscar el último código y sumarle 1
                    nuevo_codigo = max([p["codigo"] for p in productos], default=100) + 1

                    # Agregar el producto a la lista
                    productos.append({
                        "codigo": nuevo_codigo,
                        "nombre": nombre,
                        "precio": int(precio),
                        "descripcion": descripcion,
                        "categoria": categoria
                    })

                    print(f"✅ Producto {nombre} agregado con código {nuevo_codigo}.")

                elif opcion_producto == "2":  # LEER PRODUCTOS
                    print("\n📋 Lista de Productos:")
                    for p in productos:
                        print("Cod. | Nombre | Precio unit | Descripción | Categoría")
                        print(f"{p['codigo']} - {p['nombre']} | ${p['precio']} | {p['descripcion']} | {p['categoria']}")

                elif opcion_producto == "3":  # ACTUALIZAR PRODUCTO
                    codigo_buscar = int(input("Ingresá el código del producto a modificar: "))

                    for producto in productos:
                        if producto["codigo"] == codigo_buscar:
                            print(f"Producto encontrado: {producto['nombre']}")

                            producto["nombre"] = input(f"Nuevo nombre ({producto['nombre']}): ") or producto["nombre"]
                            producto["precio"] = float(input(f"Nuevo precio ({producto['precio']}): ") or producto["precio"])
                            producto["descripcion"] = input(f"Nueva descripción ({producto['descripcion']}): ") or producto["descripcion"]
                            producto["categoria"] = input(f"Nueva categoría ({producto['categoria']}): ") or producto["categoria"]

                            print(f"✅ Producto {codigo_buscar} actualizado.")
                            break
                    else:
                        print("❌ Producto no encontrado.")

                elif opcion_producto == "4":  # ELIMINAR PRODUCTO
                    codigo_buscar = int(input("Ingresá el código del producto a eliminar: "))

                    for i, producto in enumerate(productos):
                        if producto["codigo"] == codigo_buscar:
                            productos.pop(i)  # Eliminar el producto
                            print(f"✅ Producto {codigo_buscar} eliminado.")
                            break
                    else:
                        print("❌ Producto no encontrado.")

                elif opcion_producto == "5":  # SALIR DEL SUBMENÚ
                    print("🔚 Volviendo al menú principal...")
                    break  

                else:
                    print("❌ Opción inválida, intentá de nuevo.")


        ###########################################################################################
        ###################V########### 3 SUB MENÚ PEDIDOS CRUD #################################
        elif opcion_principal == "3":
                print("\n📦 Gestión de Pedidos\n")
                print("\t 1. Listar productos disponibles")
                print("\t 2. Crear pedido")
                print("\t 3. Ver pedidos")
                print("\t 4. Modificar cantidad")
                print("\t 5. Cancelar pedido")
                print("\t 6. Modificar estado del pedido")
                print("\t 7. Salir\n")

                opcion_pedido = input("Elegí una opción: ")

                if opcion_pedido == "1":  # LISTAR PRODUCTOS
                    print("\n📋 Lista de productos:")
                    for p in productos:
                        print(f"Código: {p['Código']} | Nombre: {p['Nombre']} | Precio: ${p['Precio']}")

                elif opcion_pedido == "2":  # CREAR PEDIDO
                    nro_pedido = len(pedidos) + 1  # Generar número de pedido
                    fecha_pedido = datetime.datetime.now().strftime("%d/%m/%Y")  # Fecha actual
                    detalle_pedido = []

                    while True:
                        codigo = int(input("Código del producto (0 para finalizar): "))
                        if codigo == 0:
                            break

                        producto_seleccionado = next((p for p in productos if p["Código"] == codigo), None)
                        if producto_seleccionado:
                            cantidad = int(input(f"Cantidad de {producto_seleccionado['Nombre']}: "))
                            precio_total = cantidad * producto_seleccionado["Precio"]
                            detalle_pedido.append({
                                "Código Producto": codigo,
                                "Cantidad": cantidad,
                                "Precio Unitario": producto_seleccionado["Precio"],
                                "Precio Total": precio_total
                            })
                        else:
                            print("❌ Código no válido.")

                    pedidos.append({
                        "Nro Pedido": nro_pedido,
                        "Fecha Pedido": fecha_pedido,
                        "Detalle Pedido": detalle_pedido,
                        "Estado Pedido": "Pendiente",
                        "Observación": ""
                    })
                    print(f"✅ Pedido {nro_pedido} creado con fecha {fecha_pedido}.")

                elif opcion_pedido == "3":  # LEER PEDIDOS
                    print("\n📌 Lista de pedidos:")
                    for pedido in pedidos:
                        print(f"Nro: {pedido['Nro Pedido']} | Fecha: {pedido['Fecha Pedido']} | Estado: {pedido['Estado Pedido']}")
                        for item in pedido["Detalle Pedido"]:
                            print(f"   - {item['Código Producto']} | Cantidad: {item['Cantidad']} | Total: ${item['Precio Total']}")
                        if pedido["Observación"]:
                            print(f"   📝 Observación: {pedido['Observación']}")

                elif opcion_pedido == "4":  # ACTUALIZAR CANTIDAD
                    nro_pedido = int(input("Número de pedido a modificar: "))
                    pedido_seleccionado = next((p for p in pedidos if p["Nro Pedido"] == nro_pedido), None)

                    if pedido_seleccionado and pedido_seleccionado["Estado Pedido"] == "Pendiente":
                        codigo_modificar = int(input("Código de producto a modificar: "))
                        for item in pedido_seleccionado["Detalle Pedido"]:
                            if item["Código Producto"] == codigo_modificar:
                                nueva_cantidad = int(input(f"Nueva cantidad para {codigo_modificar}: "))
                                item["Cantidad"] = nueva_cantidad
                                item["Precio Total"] = nueva_cantidad * item["Precio Unitario"]
                                print("✅ Cantidad actualizada.")
                                break
                        else:
                            print("❌ Código de producto no encontrado en el pedido.")
                    else:
                        print("❌ No se puede modificar un pedido Enviado/Entregado/Cancelado.")

                elif opcion_pedido == "5":  # CANCELAR PEDIDO
                    nro_pedido = int(input("Número de pedido a cancelar: "))
                    pedido_seleccionado = next((p for p in pedidos if p["Nro Pedido"] == nro_pedido), None)

                    if pedido_seleccionado and pedido_seleccionado["Estado Pedido"] == "Pendiente":
                        motivo = input("Motivo de cancelación (Ej: Arrepentido, Sin stock, Tardanza): ")
                        pedido_seleccionado["Estado Pedido"] = "Cancelado"
                        pedido_seleccionado["Observación"] = motivo
                        print(f"✅ Pedido {nro_pedido} cancelado. Motivo: {motivo}")
                    else:
                        print("❌ No se puede cancelar un pedido Enviado/Entregado.")

                elif opcion_pedido == "6":  # MODIFICAR ESTADO DEL PEDIDO
                    nro_pedido = int(input("\nNúmero de pedido a modificar: "))
                    pedido_seleccionado = next((p for p in pedidos if p["Nro Pedido"] == nro_pedido), None)

                    if pedido_seleccionado:
                        if pedido_seleccionado["Estado Pedido"] == "Pendiente":
                            print("\nEstados posibles: Pendiente → Enviado → Entregado / Cancelado")
                            nuevo_estado = input("\nNuevo estado del pedido: ").strip().capitalize()

                            if nuevo_estado in ["Enviado", "Entregado"]:
                                pedido_seleccionado["Estado Pedido"] = nuevo_estado
                                print(f"\n✅ Pedido {nro_pedido} actualizado a '{nuevo_estado}'")
                            else:
                                print("\n❌ Estado inválido. Solo se puede cambiar a 'Enviado' o 'Entregado'.")
                        else:
                            print("\n❌ No se puede modificar el estado de un pedido Cancelado o ya Enviado.")
                    else:
                        print("\n❌ Pedido no encontrado.")

                ###
                elif opcion_pedido == "6":  # SALIR DEL SUBMENÚ
                    print("\n🔚 Volviendo al menú principal...")
                    break 

                else:
                    print("\n❌ Opción inválida, intentá de nuevo.")

        ###########################################################################################
        ##################################### 4 OPCION CERRAR #####################################
        elif opcion_principal == "4":  # Cerrar sesión
            print("\t\t🔒 Sesión cerrada.\n")
            usuario_actual = None  # Reinicia usuario
            break  # Vuelve al menú de inicio
        else:
            print("\n❌ Opción inválida.")


""" Lista de mejoras a futuro:

✔️ Control de permisos → Definir quién puede modificar estados de pedidos.
✔️ Historial de pedidos → Guardar registros anteriores para reportes.
✔️ Filtros en consulta de productos → Búsqueda por precio, categoría, ordenación por nombre o precio.
 """