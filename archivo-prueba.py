""" resultado = 10 + 20 + \
           30 + 40
print("Hola\r", resultado) """

"""
    *** 
lista = [
    "Manzana",
    "Banana",
    "Cereza"
]
print(lista) """


import time

""" 
    *** USO UN CONTADOR QUE CON UN FOR QUE COMBINA CON \R PARA LIMPIAR EL CARRO
for i in range(10):
    print(f"\rContando: {i}", end="")
    time.sleep(1) """



""" 
    *** OPCION PARA MOSTRAR DINAMICAMENTE UN TEXTO, SUMANDO CARACTERES
mensaje = "Hola, Claudio! Retomando Python con estilo..."
for letra in mensaje:
    print(letra, end="", flush=True)
    time.sleep(0.1)  # Pausa breve para simular escritura lenta
 """

""" 
    *** FUNCION CON flush=True Y time.sleep(2) PARA MOSTRAR TEXTO TEMPORIZADAMENTE
print("Escribiendo...", end="", flush=True)
time.sleep(2)
print(" ¡Listo!") """


"""
    **** flush=True ***
El parámetro flush=True en print() fuerza la salida del texto inmediatamente. Normalmente, Python almacena temporalmente los datos en un
búfer antes de imprimirlos, especialmente cuando se usa end="" para evitar saltos de línea. Con flush=True, le decimos a Python que vacíe
ese búfer de inmediato y muestre el contenido en pantalla sin retrasos.
Es útil en situaciones donde quieres asegurarte de que el texto se imprima en tiempo real, como en animaciones o procesos interactivos. Sin
flush=True, el programa podría acumular caracteres en memoria y mostrarlos todos juntos más tarde.

"""

""" 
    *** OPCION PARA HACER UN SALTO DE LINEA  EN  LA \ U OTRA OPCION SELECCIONANDOLO Y LOGRANDO QUE EL INTERPRETE NO DE ERROR
opcion = "n"  # Puede cambiarse a otra letra si quieres probar
texto = f"Texto con \{opcion} incluido"  

# Reemplazamos '\n' cuando opcion es 'n'
texto = texto.replace("\\n", "\n")  

print(texto) """
def decorador(func):
    def nueva_funcion():
        print("Antes de ejecutar la función")
        func()
        print("Después de ejecutar la función")
    return nueva_funcion

@decorador
def saludo():
    print("Hola, Claudio!")

saludo()





