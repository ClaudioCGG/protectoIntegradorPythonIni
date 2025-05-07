
#####################################
###        *** CLASE 1 ***        ###
#####################################


# Primer Programa "Hola Mundo!"
""" print("¡Hola, Mundo!") """


#####################################
###        *** CLASE 2 ***        ###
#####################################

# Asignación Multiple
""" x, y, z = 1, 2, 3
print("*** Asignación Multiple ***")
print(x,end="\n \n ") """

#La función print() y la coma para concatenar
""" nombre = "Mundo"
print("*** La función print() y la coma para concatenar ***")
print("Hola,", nombre, end="\n  \n ") # “Hola” y nombre son dos argumentos. # Salida: Hola, Mundo """

# La función input()
""" print("*** La función input() ***")
nombre = input("Introduce tu nombre: ")
print("Hola", nombre, end="\n \n ") """

# Conversión entre tipos de datos
""" entero = 10
decimal = float(entero)
print("El numero entero 10 es Float es: ",decimal, end="\n \n ") # 10.0 """

#float(entero)
#int(decimal)
#str(edad), ej: edad = 25  / mensaje = "Tengo " + str(edad) + " años." / print(mensaje) # Tengo 25 años.
#int(str), ej: cadena_numerica = "123" / numero = int(cadena_numerica) / print(numero + 7) # 13
#Conversión entre booleanos y otros tipos de datos: 1 (verdadero) y 0 (falso).

"""
    valor_verdadero = True
    valor_falso = False
    print(int(valor_verdadero)) # 1
    print(int(valor_falso)) # 0
"""

#La función type()
""" Vimos que que input() devuelve un string, así que si necesitas tratar ese valor
como un número, primero tenés que convertirla al tipo de dato adecuado, ya sea int o float: """

""" edad = input("Introduce tu edad: ")
edad = int(edad)
print("El próximo año tendrás" ,edad + 1, "años.") """

#Operadores aritméticos
"""
    Suma (+): Suma dos valores.
    Resta (-): Resta el segundo valor del primero.
    Multiplicación (*): Multiplica dos valores.
    División (/): Divide el primer valor entre el segundo. -> Esta operación siempre retorna un número flotante (float), incluso si el resultado es un entero.
    División entera (//): Divide el primer valor entre el segundo y redondea -> el resultado hacia abajo para obtener un número entero (int).
    Módulo (%): Retorna o devuelve el sobrante de la división entre el primer y segundo valor.
    Exponenciación (**): Eleva el primer valor a la potencia del segundo.
"""

#Operadores aritméticos 2


#####################################
###        *** CLASE 3 ***        ###
#####################################

# Clase N° 3 | Condicionales I
"""
    ● Operadores lógicos y relacionales.
    ● Control de flujo: estructuras condicionales if y else.
    ● Comentarios en el código. """

# Operadores relacionales
""" Sirven para algo clave: comparar valores. El resultado de esta comparación siempre es un valor booleano, es decir, True (verdadero) o False 
(falso), dependiendo de si la condición que estás evaluando es cierta o no. Son:
    - ==    Igual que
    - !=    No igual que
    - >     Mayor que
    - <     Menor que
    - >=    Mayor o igual que
    - <=    Menor o igual que

Las cadenas de texto se comparan carácter por carácter, de izquierda a derecha, siguiendo un orden basado en su codificación (ASCII o Unicode), este tipo de
comparación se llama orden lexicográfico. Ver valor ASCII en https://elcodigoascii.com.ar/
 """
# Operadores lógicos
"""
Son clave cuando querés trabajar con múltiples condiciones al mismo tiempo. Al final, todo se reduce a si esas afirmaciones son
True (verdaderas) o False (falsas).
    - Operador “and”. Sólo devuelve True si todas las condiciones que estás evaluando son verdaderas
    - Operador “or”. Alcanza con que una sola de las condiciones sea verdadera para que el resultado total sea True. Si todas las condiciones
      son falsas va a devolver False.
    - Operador “not”. Este es el que invierte el valor de verdad de una expresión. Si algo es True, not lo convierte en False, y viceversa.
"""

# Estructuras de control.
"""
La estructura básica de un if es súper sencilla. Fijate en este ejemplo:
"""
""" numero = int(input("Ingrese un numero: "))
resultado = numero % 2

if resultado > 0:
    print("El número es impar.")
else:
    print("El número es par.") """

""" Recordar que el numero ingresado en el input lo toma como una variable del tipo text por lo que tendre q castear a int para hacer
    operaciones aritmeticas. Recordar que el bloque if, el else o elseif con opcionales a la operatividad que quieras dar al programa.
    Recordar que lo que se ejecuta en el bloque if es si la condicion es verdadera, sino salta el bloque y continua. Sus componentes:
        - Condición
        - Dos puntos (:)
        - Bloque de código indentado

    Y esto es solo el principio. Ahora pronto vas a ver cómo podés manejar situaciones que no cumplen ninguna condición con else.
"""

# Condicionales y operadores lógicos, combinación, ejemplo:
""" edad = int(input("Ingrese su edad: "))
es_ciudadano = True
if edad >= 18 and es_ciudadano:
        print("Podés votar.")
else: print("No podés votar.")

# 1. Comentarios simples con # """
# 2. Comentarios multilínea """

""" Buenas prácticas al usar comentarios:
        - Sé claro y preciso
        - Actualizá los comentarios al modificar el código
        - Usá comentarios para documentar decisiones importantes
        - Evitá comentarios redundantes
"""

#####################################
###        *** CLASE 4 ***        ###
#####################################

# Clase N° 3 | Condicionales II

# Estructuras condicionales avanzadas: elif
""" El bloque elif (abreviatura de "else if") nos permite manejar múltiples casos dentro de una misma estructura condicional, evitando
redundancias y haciendo que nuestro código sea más eficiente y legible. 
"""
#Sintaxis
""" edad = 25 
if edad < 13: 
    print("Sos menor a trece años.") 
elif edad < 18: print("Sos un o una adolescente.") 
elif edad < 60: print("Sos una persona adulta.") 
else: print("Sos una persona adulta mayor.") """

#Combinando elif con operadores lógicos
""" Podemos combinar elif con operadores lógicos para evaluar condiciones más complejas. El uso de elif simplifica el manejo de múltiples
escenarios en tus programas, haciéndolos más fáciles de entender y mantener."""

#Estructura condicional avanzada: match
""" La estructura match fue introducida en la versión 3.10 de Python, como una alternativa más clara y poderosa al uso de múltiples bloques
if...elif...else, especialmente cuando queremos comparar un valor específico con varias opciones posibles. Es similar a la estructura switch
de otros lenguajes de programación y se utiliza para simplificar el manejo de casos múltiples. """
    #La sintaxis de match
""" match variable:
    case valor1: 
        # Código si variable coincide con valor1
    case valor2:
        # Código si variable coincide con valor2
    case _:
        # Código si no coincide ningún caso (opcional)
 """

#Ejemplo sintaxis match / Simplifique el codigo de pag. 65, con una versión más limpia y directa.Eliminaste una redundancia 
#lógica: la segunda condición

""" peso = float(input("Ingresá el peso del paquete (en kg): "))
match peso:
    case p if p <= 5:
        print("Paquete pequeño.")
    case p if p <= 20:
        print("Paquete mediano.")
    case p if p > 20:
        print("Paquete grande.")
    case _:
        print("Peso no válido.") """

#Tu versión es más limpia y directa.

# Concatenación de cadenas -> 
""" El operador + para lograrlo de manera sencilla. -> Si necesitás unir una cadena con otro tipo de dato, como un número o un valor booleano,
primero tenés que convertir ese dato en texto usando la función str(). *** Python no permite combinar distintos tipos de datos directamente *** """

#Longitud de una cadena de caracteres y la función len()
"""
La función len() toma como argumento una cadena y devuelve un número entero que representa la cantidad de caracteres en esa cadena.

En Python, muchas de las funcionalidades como `len()` funcionan como **funciones globales**, lo que significa que no están atadas 
directamente como propiedades de las clases (como ocurre en otros lenguajes como Java o C#). Por ejemplo, en Python usamos `len(cadena)` en 
lugar de algo como `cadena.length`.

Esto es una decisión de diseño del lenguaje. Guido van Rossum, el creador de Python, quiso que las funciones más comunes y útiles 
(como `len()`, `max()`, `min()`, etc.) fueran globales para que fueran más consistentes y fáciles de usar en diferentes contextos, no solo 
con cadenas, sino también con otros tipos de datos como listas, tuplas o conjuntos.

### ¿Por qué no es una propiedad como en otros lenguajes?
En Python, una cadena es una instancia de la clase `str`, y aunque podrías pensar que `len()` debería ser un método (como `cadena.len()`), 
esta funcionalidad no fue incluida en la clase `str`. Sin embargo, Python maneja este comportamiento de manera centralizada a través de la 
función global `len()`.

# Rompiendo las cadenas
En Python, el índice de una cadena comienza en cero, podés utilizar la notación con corchetes [] para acceder a un carácter específico. 
También podés usar índices negativos, Python empieza a contar desde el final de la cadena.

Podés extraer una porción de la cadena utilizando *** slicing (rebanado)***. Esto se hace indicando un rango en los corchetes [inicio:fin].
Ej: mensaje= 'Hola'  ->  mensaje[0:2]  # Salida: Ho
Si omitís el inicio o el final del rango, Python asume que querés ir desde el principio o hasta el final de la cadena, respectivamente. 
Ej: mensaje[:2]  ->  te devuelve "Ho"  , y mensaje[1:]  ->  te da "ola"

*** Las cadenas son inmutables, lo que significa que no podés cambiar un carácter directamente asignándole un nuevo valor usando los índices.
Si intentás algo como mensaje[0] = "J", Python va a generar un error.***

# Métodos de cadenas en Python
Las cadenas en Python no solo son una secuencia de caracteres, sino que también son objetos que vienen con una variedad de métodos 
incorporados. Lo interesante de los métodos de cadenas es que no modifican la cadena original, sino que generan una nueva con los 
cambios aplicados.
Ej: 

cadena = "Hola, mundo!"
print(cadena.lower())               # Convierte a minúsculas: "hola, mundo!"
print(cadena.upper())               # Convierte a mayúsculas: "HOLA, MUNDO!"
print(cadena.title())               # Convierte a: "Hola, Mundo!"
print(cadena.strip())               # Elimina los espacios en blanco al principio y al final de la cadena.
print(cadena.replace())             # Reemplaza una subcadena por otra dentro de la cadena. Ej.: print(texto.replace("Mundo", "Python")) 
                                    # Salida: "Hola, Python!"
print(cadena.startswith("Hola"))    # Verifica si empieza con "Hola": True
print(cadena.endswith("!"))         # Verifica si termina con "!": True
print(cadena.find())                # Devuelve la posición, ej: print(texto.find("Mundo")) # Salida: 6
print(cadena.find())                # Devuelve un valor booleano True si todos los valores de la cadena de entrada son dígitos; de lo 
                                      contrario, devuelve False.

"""

#Formateo de cadenas con f-Strings
"""
El formateo de cadenas con f-Strings es una de las maneras más eficientes y legibles de combinar texto con valores variables en Python.
Introducidas en la versión 3.6, las f-Strings permiten integrar directamente expresiones y variables dentro de una cadena, utilizando
llaves {} para delimitar el contenido dinámico. las f-Strings soportan expresiones complejas, lo que las convierte en una herramienta
poderosa para la creación de cadenas dinámicas. Las f-Strings permiten no solo incluir valores dinámicos en cadenas, sino también aplicar
comandos y formatos para presentar la información de manera clara y profesional.
"""

#1. Inclusión de variables
"""
La forma básica de usar f-Strings es incluir variables directamente dentro de las llaves {}.
"""
""" nombre = "María"
edad = 30
print(f"Hola, {nombre}. Tenés {edad} años.") # Salida: Hola, María. Tenés 30 años. """

#2. Expresiones dentro de las llaves
""" Podés incluir cálculos y expresiones directamente dentro de las llaves. """
""" a = 5 
b = 3 
print(f"La suma de {a} y {b} es {a + b}.") # Salida: La suma de 5 y 3 es 8. """

#3. Formateo de números
""" Con las f-Strings, podés aplicar formatos para ajustar cómo se muestran los números.

Decimales: Podés limitar la cantidad de decimales utilizando :.nf, donde n es el número de
decimales deseados.
"""
""" pi = 3.14159 
print(f"El valor de π con 2 decimales es {pi:.2f}.") """

"""
Números grandes: Podés agregar separadores de miles con :,. (dos puntos seguidos del separador, que puede ser un punto o una coma):
"""
""" numero = 1000000 
print(f"El número es {numero:,}.") # Salida: El número es 1,000,000. """

"""
Porcentajes: Usá % para formatear como porcentaje.
"""
""" porcentaje = 0.85 
print(f"El porcentaje es {porcentaje:.0%}.") # Salida: El porcentaje es 85%. """

# 4. Formateo de texto
"""
Podés usar especificadores para ajustar cómo se muestra el texto. Alineación: 
Usá <, > o ^ para alinear texto a la izquierda, derecha o centro, mas la cantidad de digitos que debe alinear
"""
""" texto = "Python" 
print(f"{texto:<100}") # Salida: Python (alineado a la izquierda) 
print(f"{texto:>100}") # Salida: Python (alineado a la derecha) 
print(f"{texto:^100}") # Salida: Python (centrado) """

"""
Relleno: Podés agregar un carácter de relleno antes de los especificadores de alineación.
"""
""" texto = "Python" 
print(f"{texto:*<100}") # Salida: Python (alineado a la izquierda) 
print(f"{texto:*>100}") # Salida: Python (alineado a la derecha) 
print(f"{texto:*^100}") # Salida: Python (centrado) """

# 5. Escapando llaves -> Si necesitás incluir llaves {} como texto y no como parte de una f-String, simplemente duplicalas.




#####################################
###        *** CLASE 5 ***        ###
#####################################

# Clase N° 5 | Bucles While

#Control de flujo: bucles while
"""
Un bucle while permite repetir un bloque de código mientras se cumpla una condición específica. Es importante que dentro del bucle haya algo
que eventualmente haga que la condición sea False, porque si no, el programa entraría en lo que llamamos un "bucle infinito". Un bucle 
infinito sigue ejecutándose sin detenerse y puede hacer que tu programa deje de responder. Un bucle while es ideal cuando no sabés de 
antemano cuántas veces se debe repetir una acción. Ver: # Ejemplo 2 
"""

#Ejemplo
"""
contador = 1

while contador <= 5:
    print(f"Este es el intento número {contador}.")
    contador += 1 # Incrementamos el valor de contador
print("Bucle terminado.")

print("Contador es igual a:",contador) """

# Ejemplo 2 
""" # Inicializamos una variable para controlar el bucle 
numero = 0 
print("Ingresá números positivos para sumarlos. Ingresá 0 para terminar.") 
# Usamos un bucle while que se ejecuta hasta que el usuario ingrese 0 
suma = 0 
while True: 
    # Solicitamos al usuario un número 
    numero = int(input("Ingresá un número: ")) 
    
    # Verificamos si el número es negativo 
    if numero < 0:
        print("El número es negativo, se ignora. Intentá de nuevo.") 
        continue # Saltamos el resto del código en esta iteración 
    
    # Si el número es 0, salimos del bucle 
    if numero == 0: 
        break 
    # Sumamos el número positivo al total 
    suma += numero 

# Mostramos el resultado final 
print(f"La suma de los números positivos es: {suma}")
 """

#Ejemplo 3
""" 
numero = 1
suma = 0
print("Ingresá números positivos para sumarlos. Ingresá un número mayor a 50 para terminar.")

while numero <= 50:  # El bucle se ejecuta mientras número sea menor o igual a 50
    numero = int(input("Ingresá un número: "))
    
    if numero < 0:  # Si el número es negativo
        print("El número es negativo, se ignora. Intentá de nuevo.")
        continue  # Salta la suma y vuelve a pedir otro número
    
    suma += numero  # Si es positivo, lo suma al total

print(f"La suma de los números positivos es: {suma}")

 """

# Contadores en bucles while.
"""
Por lo general, un contador se inicializa antes del bucle, se actualiza en cada iteración (normalmente sumándole 1) y se utiliza como parte
de la condición del bucle o para tomar decisiones dentro de él. Ej: Solicitar un nombre de usuario con un máximo de 3 intentos. En el ejemplo
se utiliza break cuando se intenta hasta 3 veces, podriamos ponerlo como condicion del while y mantendria la misma funcionalidad.

La sentencia continue se utiliza dentro de bucles para omitir el resto del código en la iteración actual y pasar directamente a la siguiente
iteración. A diferencia de break, que termina el bucle por completo, continue sólo salta la ejecución restante en la iteración actual,
permitiendo que el bucle continúe funcionando como está diseñado. Esto es útil cuando querés evitar ciertas condiciones específicas dentro
del bucle, pero sin detener todo el proceso.
"""
# Acumulador
"""
Un acumulador es una variable que se utiliza para almacenar un valor que va aumentando (o disminuyendo) de manera progresiva a lo largo de
las iteraciones de un bucle. Generalmente, se inicializa con un valor base (por ejemplo, 0 para una suma o 1 para una multiplicación), y
luego se le van agregando o combinando valores durante cada iteración del bucle. El propósito de un acumulador es mantener un registro de un
cálculo o un resultado parcial que depende de los datos procesados en el bucle.
"""
#Introducción a las listas como estructuras para almacenar múltiples valores.
"""
Una lista es una estructura de datos en Python que te permite almacenar múltiples valores en un solo lugar. Las listas en Python se definen
utilizando corchetes [], y los elementos se separan por comas. Podés agregar, modificar o eliminar elementos de una lista, lo que las
convierte en una herramienta muy flexible para manejar datos en tus programas, y que pronto aprenderemos a utilizar a fondo. 
"""
# Ejemplo 1:
""" numeros = [10, 20, 30, 40, 50]
nombres = ["Ana", "Luis", "Carlos"]
lista_vacia = [] """

#Acceso a los elementos de una lista utilizando su índice.
"""
Si intentás acceder a un índice que no existe, Python genera un error.
Índices negativos: Python también permite usar índices negativos para acceder a los elementos desde el final hacia el principio.
"""
# Ejemplo 2:
""" frutas = ["manzana", "banana", "cereza"] 
# Accedemos a los elementos por índice 
print(frutas[0]) # Salida: manzana 
print(frutas[1]) # Salida: banana 
print(frutas[2]) # Salida: cereza """





#####################################
###        *** CLASE 6 ***        ###
#####################################

# Clase N° 6 | Bucles For y Range()

# Control de flujo: bucles for
"""
A diferencia del bucle while, que sigue ejecutándose hasta que una condición se vuelva falsa, el bucle for es ideal cuando ya sabés 
exactamente cuántas veces necesitás repetir una acción. El bucle for toma una secuencia (una lista, una cadena de texto, un rango numérico)
y la recorre de principio a fin, ejecutando un bloque de código para cada elemento en la secuencia.
"""
# Ejemplo 1 
""" productos = ["manzanas", "naranjas", "bananas", "peras"] 
for producto in productos: 
    print("Producto disponible:", producto) """

# Bucle for: Iterando a través de cadenas.
""" palabra = "Python" 
for letra in palabra: 
    print("Letra:", letra) """

# Break
"""
El uso de break en un bucle for, tal como ocurre cuando lo usamos con while, permite interrumpir la ejecución del bucle antes de que haya
terminado su recorrido completo.
"""
#Ejemplo 2:
""" # Lista de productos 
productos = ["P001", "P002", "P003", "P004", "P005"] 
# Producto que queremos encontrar 
producto_a_buscar = "P003" 
# Recorremos la lista buscando el producto 
for producto in productos: 
    if producto == producto_a_buscar: 
        print("Producto encontrado:", producto)
        break # Detenemos el bucle al encontrar el producto 
    print("Buscando...") 
print("Fin de la búsqueda.") """

# ¿Qué es range()?
"""
La función range() es muy útil para generar secuencias de números, lo que nos permite controlar cuántas veces queremos que un bucle se repita
tanto como recorrer listas utilizando índices numéricos. Se utiliza principalmente con bucles for para ejecutar un bloque de código un número
determinado de veces
"""
""" #Sintaxis
range(inicio, fin, paso)
 """

#La función range() es útil para controlar cuántas veces se repite un bucle for. Nos permite:
"""
   - Definir un rango de números.
   - Controlar desde dónde comienza y termina la secuencia.
   - Ajustar el paso entre los números de la secuencia.

El uso de range() es fundamental cuando trabajás con iteraciones en Python, especialmente para recorrer listas, repetir tareas un número fijo
de veces o manejar secuencias de números de manera versátil.
"""
# Ejemplo range(inicio, fin, paso)
""" for i in range(2,5,2): 
    print(i)
 """

# Ejemplo 1: Uso básico de range().
""" for i in range(5): 
    print(i) """

# Ejemplo 2: Valor de inicio específico.
""" for i in range(3, 7): 
    print(i) """

#Ejemplo 3: El parámetro paso.
""" for i in range(0, 10, 2): 
    print(i) """

# Ejemplo 4: Secuencias decrecientes
""" for i in range(10, 0, -2): 
    print(i) """

# Ejemplo 5: El uso de range() para recorrer listas
""" frutas = ["manzana", "banana", "naranja"] 

for i in range(len(frutas)): 
    print(f"Fruta {i + 1}: {frutas[i]}") """

# Comparación entre while y for.
"""
Cuando usás un bucle while, generalmente tenés que controlar variables como contadores o índices de forma manual. Esto significa que 
necesitás inicializarlos, actualizarlos en cada iteración y asegurarte de que la condición del bucle sea correcta. Sin embargo, con un bucle
for, podés recorrer directamente los elementos de una lista o una secuencia sin preocuparte por gestionar esas variables, ya que Python 
lo hace automáticamente por vos.
Esta simplicidad no solo reduce posibles errores, sino que también hace que tu código sea más fácil de leer y mantener. Aprender a identificar
cuándo usar for en lugar de while es clave para optimizar tus programas y trabajar de manera más eficiente.
"""


#####################################
###        *** CLASE 7 ***        ###
#####################################