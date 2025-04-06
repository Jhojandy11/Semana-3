#Objetivo: Realizar un programa que te solicite solo el ingreso de un númeno mayor a 10 y menor a 50
#   Y  QUE TE IMPRIMA SI ES UN NUMERO PAR O IMPAR, utiliza mod.
#NOMBRE Y APELLIDO: Jhojandy Azariel Michue Izquierdo 
#FECHA: 06/04/2025


#===========
# Ingresa u número mayor a 10 y menor a 50:
#
#El número es par 
#
#=========

while (True): 
    numeroIngresado = int (input('ingrese un número mayor a 10 y menor a 50: '))
    if (numeroIngresado > 9 and numeroIngresado < 51) :
        break
    print('ERROR DE USUARIO ..... INGRESE UN NÚMERO MAYO A 10 Y MENOR A 50')

if(numeroIngresado % 2 == 0 ) :     
    print('El número ingresado es par')
else: 
    print('El número ingresado es impar')
           
