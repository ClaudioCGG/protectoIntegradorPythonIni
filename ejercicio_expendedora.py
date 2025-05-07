""" ¡Aquí va un desafío rápido para entrenar tu mente de programador! 🚀  

🔹 **Desafío:** Escribe un programa en Python que simule una **máquina expendedora**. Debe:  
1️⃣ Mostrar un menú con al menos **3 productos** (Ejemplo: "1. Café - $100", "2. Té - $80", "3. Agua - $50").  
2️⃣ Pedir al usuario que ingrese su elección.  
3️⃣ Solicitar el dinero y verificar si es suficiente.  
4️⃣ Si el dinero es suficiente, dar el producto y calcular el vuelto. Si no, informar que falta dinero.  

💡 **Opcional:** Agregar más lógica como volver al menú si no se tiene suficiente dinero o permitir múltiples compras antes de salir.  

Intenta escribir el código **sin ayuda**, y cuando lo tengas, dime cómo te salió. ¡Vamos, programador! 😃🔥
 """
""" 
while True:
    print("Menu Principal Expendedora")
    print("1. Café - $100")
    print("2. Té - $80")
    print("3. Agua - $50")

    
    opcion_seleccionada = int(input("Seleccione una opción válida"))

    if opcion_seleccionada in (1,2,3):
        True
    
    match opcion_seleccionada:
        case 1:
            pago = float(input("Indique el monto de su pago:"))
            
            if pago < 100:
                print("Saldo insuficiente")
            elif pago > 100:
                print(f"Su vuelto es: ${pago-100}, retire su producto, gracias y disfrute su bebidad!")
            else:
                print("Retire su producto, gracias y disfrute su bebidad!")

        case 2:
            pago = float(input("Indique el monto de su pago:"))
            
            if pago < 80:
                print("Saldo insuficiente")
            elif pago > 80:
                print(f"Su vuelto es: ${pago-80}, retire su producto, gracias y disfrute su bebidad!")
            else:
                print("Retire su producto, gracias y disfrute su bebidad!")

        case 3:
            pago = float(input("Indique el monto de su pago:"))
            
            if pago < 50:
                print("Saldo insuficiente")
            elif pago > 50:
                print(f"Su vuelto es: ${pago-50}, retire su producto, gracias y disfrute su bebidad!")
            else:
                print("Retire su producto, gracias y disfrute su bebidad!")
 """

###############################################################################################################33

precios = {1: 100, 2: 80, 3: 50}  # Diccionario con precios

while True:
    print("\n--- Menu Principal Expendedora ---")
    print("1. Café - $100")
    print("2. Té - $80")
    print("3. Agua - $50")
    print("4. Salir")  # Opción para salir del programa

    opcion_seleccionada = input("Seleccione una opción válida: ")

    # Si la opción no es válida, mostramos el mensaje de error y volvemos al menú
    if opcion_seleccionada not in ("1", "2", "3", "4"):
        print("❌ Opción inválida, intenta de nuevo.")
        continue  # Vuelve al inicio del ciclo sin ejecutar lo demás

    if opcion_seleccionada == "4":
        print("Gracias por usar la expendedora. ¡Hasta luego!")
        break  # Sale del bucle y termina el programa

    pago = float(input("Indique el monto de su pago: "))
    precio = precios[int(opcion_seleccionada)]  # Obtiene el precio del diccionario

    if pago < precio:
        print("Saldo insuficiente.")
    elif pago > precio:
        print(f"Su vuelto es: ${pago - precio}. Retire su producto, gracias y disfrute su bebida!")
    else:
        print("Retire su producto, gracias y disfrute su bebida!")

    print("\n--- Menu Principal Expendedora ---")
    print("1. Café - $100")
    print("2. Té - $80")
    print("3. Agua - $50")
    print("4. Salir")  # Opción para salir del programa

    opcion_seleccionada = input("Seleccione una opción válida: ")

    if opcion_seleccionada == "4":
        print("Gracias por usar la expendedora. ¡Hasta luego!")
        break  # Sale del bucle y termina el programa

    if opcion_seleccionada in ("1", "2", "3"):
        pago = float(input("Indique el monto de su pago: "))
        precio = precios[int(opcion_seleccionada)]  # Obtiene el precio del diccionario

        if pago < precio:
            print("Saldo insuficiente.")
        elif pago > precio:
            print(f"Su vuelto es: ${pago - precio}. Retire su producto, gracias y disfrute su bebida!")
        else:
            print("Retire su producto, gracias y disfrute su bebida!")
    else:
        print("Opción inválida, intenta de nuevo.")  # Maneja opciones incorrectas