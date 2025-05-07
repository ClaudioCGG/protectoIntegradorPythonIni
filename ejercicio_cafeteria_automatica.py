""" ¡Me encanta tu entusiasmo por mejorar tus habilidades! 🚀 Aquí tienes tu próximo desafío de submenús, basado en una cafetería virtual:
🔥 Desafío: Cafetería interactiva
Objetivo:
1️⃣ Menú principal donde el usuario pueda elegir entre comprar una bebida o un snack.
2️⃣ Si elige bebida, mostrará un submenú con opciones como café, té y jugo.
3️⃣ Si elige snack, mostrará otro submenú con torta, galleta y tostada.
4️⃣ Pedirá el monto del pago y verificará si es suficiente.
5️⃣ Si el usuario elige "salir", el programa debe terminar correctamente.
💡 Opcional: Puedes agregar un sistema de vuelto, mejorar mensajes o incluir más opciones.
📌 Ejemplo de flujo esperado:
--- Menú Principal ---
1. Bebida
2. Snack
3. Salir

Elige una opción: 1

--- Menú de Bebidas ---
1. Café - $100
2. Té - $80
3. Jugo - $120
4. Volver al Menú Principal

Elige una bebida: 2
Indique el monto de pago: 100
Su vuelto es $20. Retire su té, gracias y disfrute!



 """

nombres = ["Carlos", "Ana", "Mariana", "Juan", "Pedro"]
letra_eliminar = input("Indica la letra a eliminar: ").lower()  # Convertir a minúscula para evitar errores

# Filtrar nombres que NO contengan la letra dada
nombres_filtrados = [nombre for nombre in nombres if letra_eliminar not in nombre.lower()]

print("Lista actualizada:", nombres_filtrados)