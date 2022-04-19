# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ################################## Ejemplos de Programas Sencillos #################################################
# 1. Programa para ver si funciona PYTHON

edad=int(input("Dime tu edad: "))
if edad>=18:
    print("Eres mayor de edad")
print("Programa Terminado")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1. Programa que pregunte al usuario su nombre, y luego lo salude

nombre=str(input("Dime tu nombre: "))
print('Un gusto conocerte',nombre)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2. Calcular el perímetro y área de un rectángulo dada su base y su altura

base=float(input("Dime la base del rectángulo: "))
altura=float(input("Dime la altura del rectángulo: "))
perimetro=(base*2)+(altura*2)
area=(base**altura)
print('El perímetro de su rectágulo es de %d y su area de %d'%(perimetro,area))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3. Hipotenusa de un triángulo, de triángulo rectángulo

from __future__ import division
import math
cateto1=float(input("Dime el cateto 1 del rectángulo: "))
cateto2=float(input("Dime el cateto 2 del rectángulo: "))
hipotenusa=math.sqrt(cateto1**cateto1 + cateto2**cateto2)
print('La hipotenusa de su rectágulo es de %d'%(hipotenusa))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 4. Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

num1=int(input("Dime el número 1: "))
num2=int(input("Dime el número 2: "))
suma=(num1+num2)
resta=(num1-num2)
div=(num1 / num2)
mult=(num1**num2)
print('''~ La suma es de %.2f
~ La resta de %.2f
~ La división es de %.2f
~ La multiplicación es de %.2f'''%(suma,resta,div,mult))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 5. Pasar de grados fahrenheit a celcius

fahren=float(input("Escribe la temperatura en grados fahrenheit: "))
celcius=(fahren-32)*5/9
print('La temperatura es de %d ºC'%(celcius))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 6. Media de 3 números

num1=float(input('Escribe el primer número: '))
num2=float(input('Escribe el segundo número: '))
num3=float(input('Escribe el tercer número: '))
media=(num1+num2+num3)/3
print('La media de los tres números es de %.2f'%(media))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 7. Pasar una cantidad de minutos indeterminada a horas

minutos=int(input('Escribe la cantidad de minutos: '))
ResultHoras=(minutos//60)
ResultMin=(minutos%60)
print('El resultado es de %d horas y %d minutos'%(ResultHoras,ResultMin))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 8. Un vendedor realiza 3 ventas al mes y se lleva un 10% de comisiónes de venta, cuanto gana?

sueldoBase=float(input('Escribe cuál es tu sueldo base: '))
venta1=float(input('Escribe cuanto dinero ganó en la primera venta: '))
venta2=float(input('Escribe cuanto dinero ganó en la segunda venta: '))
venta3=float(input('Escribe cuanto dinero ganó en la tercera venta: '))
ventasTotales=(venta1*0.1)+(venta2*0.1)+(venta3*0.1)
SueldoTotal=sueldoBase+ventasTotales
print('Su sueldo mensual total es de %.2f'%(SueldoTotal))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 9. Tienda hace 15% de descuento sobre compra total a clientes

CompraTotal=float(input('Escribe la compra total en euros: '))
descuento=(CompraTotal*0.15)
precioFinal=(CompraTotal-descuento)
print('El total a pagar con el descueto aplicado es de %.2f €'%(precioFinal))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~