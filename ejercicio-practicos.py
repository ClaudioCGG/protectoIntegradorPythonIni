#####################################
###        *** CLASE 2 ***        ###
#####################################

#Operadores aritméticos

"""
En nuestro día a día, interactuamos con muchos clientes, y uno de los pasos iniciales es recopilar y organizar su información básica. 
Para eso, necesito que desarrolles un pequeño programa en Python que haga lo siguiente:
    ● Solicite al cliente su nombre, apellido, edad y correo electrónico.
    ● Almacene estos datos en variables.
    ● Los muestre organizados en forma de una tarjeta de presentación en la pantalla.
¡Espero ver el resultado de tu trabajo pronto!
"""
""" nombre = input('Ingrese nombre: ')
apellido = input('Ingrese Apellido: ')
edad = input('Ingrese edad: ')
mail = input('Ingrese correo electronico: ')

print('\nBienvenido ',nombre,apellido,' su edad indicada es:',edad,'años.')
print('Notificaremos al mail:', mail, ' novedades de su interes. Gracias por su registro!', end='\n ') """


#####################################
###        *** CLASE 3 ***        ###
#####################################

"""
Te damos la bienvenida a tu jornada en TechLab. Al llegar, te encontrás con Mariana, la Gerente de Proyectos, quien te felicita por haber
completado tu primera asignación en torno a las variables con éxito, y aprovecha para hacerte algunas sugerencias:
“Para que tu programa sea aún más robusto, me gustaría que trabajemos en validar los datos que ingresan los usuarios:
    - que los campos no queden en blanco
    - agregar una lógica para indicar si un cliente es mayor o menor de edad.”

    Necesito que desarrolles un pequeño programa en Python que haga exactamente lo siguiente:
        ● Solicite al cliente su nombre, apellido, edad y correo electrónico.
        ● Compruebe que el nombre, el apellido y el correo no estén en blanco, y que la edad sea mayor de 18 años.
        ● Muestre los datos por la terminal, en el orden que se ingresaron. Si alguno de los datos ingresados no cumple los requisitos, sólo mostrar el texto “ERROR!”.

Para ello, tendrás que interiorizarte en el concepto de condicionales (estructuras de control de flujo) y los operadores lógicos y
relacionales. ¡Manos a la obra! """

nombre = input('Ingrese nombre: ')
apellido = input('Ingrese Apellido: ')
try:
    edad = int(input('Ingrese edad: '))
except ValueError:
    print("Por favor, ingrese un número válido para la edad.")
    exit()
mail = input('Ingrese correo electrónico: ')

# Validación de entrada con mensajes al usuario
if not nombre.strip():
    print("El campo nombre está vacío. Por favor, ingrese un nombre válido.")
    nombre = input("Reingrese nombre: ").strip()

if not apellido.strip():
    print("El campo apellido está vacío. Por favor, ingrese un apellido válido.")
    apellido = input("Reingrese apellido: ").strip()

if not mail.strip() or "@" not in mail:
    print("El correo electrónico no es válido. Por favor, ingrese un correo válido.")
    mail = input("Reingrese correo electrónico: ").strip()

if edad < 0:
    print("La edad no puede ser negativa. Por favor, ingrese una edad válida.")
    edad = int(input("Reingrese edad: "))

# Mensaje final
print('\nBienvenido', nombre, apellido, 'su edad indicada es:', edad, 'años.')
print('Notificaremos al mail:', mail, 'novedades de su interés. ¡Gracias por su registro!')

#####################################
###        *** CLASE 4 ***        ###
#####################################

"""
En lo que ya se está convirtiendo en una costumbre, ni bien ingresás a la sede de TalentoLab, te encontrás con Mariana. Café en mano, te
felicita por tus avances, y te comenta que:
    - “Nuestro cliente nos pide que el programa formatee correctamente los textos ingresados y
    - que clasifique a las y los clientes por rango etario (niña o niño, adolescente, adulto o adulta) basándose en su edad.”

Claramente, es algo que no podés hacer con tus conocimientos actuales. Afortunadamente, Luis está ahí para ayudarte. Buscan un despacho
libre, y comienzan a ver que necesitás saber para poder resolver este nuevo desafío.


Ejercicio Práctico
Luego de haber pasado el día con Luis y aprendido a utilizar condicionales avanzados y los métodos de las cadenas, estás en condiciones de 
resolver la tarea que te mencionó Mariana y que acaba de formalizar mediante un correo electrónico:

Nuestro cliente nos pide que el programa ahora haga lo siguiente:
    ● Formatee correctamente los textos ingresados en “apellido” y “nombre”, convirtiendo la primera letra de cada palabra a mayúsculas y el 
      resto en minúsculas.
    ● Asegurarse que el correo electrónico no tenga espacios y contenga solo una “@”.
    ● Que clasifi que a sus clientes por rango etario basándose en su edad (“Niño/a” para los y las menores de 15 años, “Adolescente” de 15 
      a 18 y “Adulto/a” para personas mayores de 18 años.)

El programa debe mostrar el apellido, nombre y dirección de correo con el formato pedido, y el texto correspondiente a su rango etario.
¡Estoy segura de que harás un excelente trabajo!

"""
# https://ellibrodepython.com/cadenas-python#m%C3%A9todos-string



#####################################
###        *** CLASE 5 ***        ###
#####################################
"""

Necesitamos un software que ayude a registrar y calcular información financiera básica para nuestros y nuestras clientes. Tu tarea para esta
semana es la siguiente:
    ● Registrar los ingresos mensuales de un cliente durante 6 meses. Usá un bucle while para solicitar el ingreso de cada mes.
    ● Validar que los ingresos sean números positivos. Si se ingresa un valor negativo, mostrá un mensaje indicando que el valor 
      no es válido y volvé a pedir el dato.
    ● Calcular el ingreso total acumulado durante los 6 meses. Mostrá este resultado al final del programa.
"""


#####################################
###        *** CLASE 6 ***        ###
#####################################

"""
Ejercicio Práctico.
lograste entender la sintaxis y utilidad de los bucles for, y lo súper útil que son para recorrer estructuras de datos. Con estas 
herramientas estás listo para resolver el pedido de Mariana:
    ● Crear una lista con los nombres de los clientes y clientas que vamos a procesar. Algunos nombres pueden estar en blanco por lo que 
      debemos poder detectarlo.
    ● Recorrer la lista y mostrar el nombre de cada cliente, junto con su posición en la lista (por ejemplo, Cliente 1, Cliente 2, etc.).
    ● Si encuentras un o una cliente cuyo nombre sea una cadena en blanco, mostrar un mensaje de alerta indicando que ese dato no es válido.
    ● Para los nombres válidos, convertir cada uno a formato adecuado usando .capitalize(), de modo que siempre tengan la primera letra en 
      mayúscula y el resto en minúscula.

"""