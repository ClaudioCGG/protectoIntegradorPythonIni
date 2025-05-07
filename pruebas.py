""" nombre = input("Ingrese un nombre: ")

# Convertimos la variable 'nombre' a booleano y la mostramos
es_valido = bool(nombre.strip())  # Usamos .strip() para eliminar espacios en blanco
print("El valor booleano del nombre es:", es_valido)

# Validamos si el nombre es válido
if es_valido:
    print("El campo 'nombre' tiene contenido.")
else:
    print("El campo 'nombre' está vacío o tiene solo espacios.") """


""" nombre = "María" 
edad = 30 
print("Hola, {nombre}. Tenés {edad} años.") # Salida: Hola, María. Tenés 30 años. """


""" edad = int(input("Ingresá tu edad: "))

if edad < 18:

    print("Sos menor de edad.")

else:

    print("Sos mayor de edad.") """

""" texto = "¡Hola, Python!"

print(len(texto)) """

""" ingreso = 60000

edad = 25

if ingreso < 50000:

    print("Ingresos bajos.")

elif edad < 30:

    print("Joven con buenos ingresos.")

else:

    print("Adulto con buenos ingresos.") """

""" texto = "Hola"

texto[0] = "J" """

""" nota = 85

if nota >= 90:

    print("Excelente.")

elif nota >= 75:

    print("Muy bien.")

else:

    print("Suficiente.") """


""" dia = input("Ingresá un día de la semana: ")

match dia:
    case "Lunes":
        print("Inicio de semana.")
    case "Viernes":
        print("Fin de semana.")
    case _:
        print("Día intermedio.") """


""" texto = "Python"

if "P" in texto and texto.endswith("on"):
    print("Condición cumplida.")
else:
    print("Condición no cumplida.")
"""

texto = "  Python  "
print(texto.strip().upper())
