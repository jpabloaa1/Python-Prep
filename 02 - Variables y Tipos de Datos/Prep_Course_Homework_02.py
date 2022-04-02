# Homework Lección 2
# Juan Pablo Aguayo Adame

#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
num1 = 24
print(num1)

#2) Imprimir el tipo de dato de la constante 8.5
type(8.5)

#3) Imprimir el tipo de dato de la variable creada en el punto 1
type(num1)

#4) Crear una variable que contenga tu nombre
nombre = "Juan Pablo"
print(nombre)

#5) Crear una variable que contenga un número complejo
num1 = 3 + 2j

#6) Mostrar el tipo de dato de la variable crada en el punto 5
type(num1)

#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi = 3.1416

#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
var1 = "True"
var2 = True

#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print("La variable var1 es de tipo ", type(var1))
print("La variable var2 es de tipo ", type(var2))

#10) Asignar a una variable, la suma de un número entero y otro decimal
num2 = 5 + 3.12


#11) Realizar una operación de suma de números complejos
x = 2 + 3j
y = 5 - 4j

print(x + y)

#12) Realizar una operación de suma de un número real y otro complejo
m = 4 + 2j
n = 7

print(m + n)

#13) Realizar una operación de multiplicación
print(4*7)

#14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)

#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
div = 27/4
print(div)

#16) De la división anterior solamente mostrar la parte entera
print(int(div))

#17) De la división de 27 entre 4 mostrar solamente el resto
print(27%4)

#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(6*4+3)

#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
cad1 = "Juan "
cad2 = "Pablo"

print(cad1 + cad2)

#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print(2 == "2")

#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(2 == int("2"))

#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
a = float("3.2")
print(a)

#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
a = 3
a -= 5

print(a)

#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
n = 1 << 5
print(n)

#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
a = 2
b = "2"

#26) Realizar una operación válida entre valores de tipo entero y string
c = a + int(b)