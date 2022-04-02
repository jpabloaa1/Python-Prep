## Homework Lección 3: Flujos de Control
# Juan Pablo Aguayo Adame

#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
from operator import truediv


num = -0

if(num < 0):
    print("El numero es negativo")
elif(num > 0):
    print("El numero es positivo")
else:
    print("El numero es cero")
    
#2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
a = "Sol"
b= 5
if(type(a) == type(b)):
    print("Las variables son del mismo tipo")
else:
    print("Las variables no son del mismo tipo")


#3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for i in range(1,21):
    if (i%2 == 0):
        print("El numero " + str(i) + " es par")
    else:
        print("El numero " + str(i) + " es impar")

#4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for i in range(0,5):
    a = i**3
    print(a)

#5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
a = 6
for i in range(0,a):
    print(i)

#6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
a = 6
b = a
c = 1
if (a > 0):
    while(b > 0):
        c = c * (b)
        b -= 1
    print(c)
else:
    print("El numero es negativo")

#7) Crear un ciclo for dentro de un ciclo while
n = 5
while(n > 0):
    b = 6 - n
    for i in range(1,6):
        print("Este es el ciclo ", str(i), " del for y el ciclo ", str(b), " del while" )
    n -= 1

#8) Crear un ciclo while dentro de un ciclo for
for i in range(1,6):
    n = 5
    while(n > 0):
        b = 6- n
        print("Este es elc ciclo ", str(b), "del while y el ciclo ", str(i), " del for")
        n -= 1
    
#9) Imprimir los números primos existentes entre 0 y 30
min = 1
max = 30
for n in range(min, (max + 1)):
    primo = True
    j = 2
    while(j < n):
        if (n % j == 0):
            primo = False
            break
        j += 1
    if (primo):
        print('El número', n, 'es primo')
        
#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

#11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

#12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

#13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

#14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

#15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
