#Objetivo : Uso de Do-While (mientras)
#Nombre ; Michue Izquierdo Jhojandy Azariel 
#Fechas: 05/04/2025


while (True):
    Numero = int(input ('Usuario ingresar un número enter positivo' ))
    if ( Numero > 0 and Numero < 19)  or (Numero > 29 and Numero < 61):
        break 
    print('ERROR DE USUARIO ........ Ingrese un número > 0 !!! ')

print ('Por fin saliste del bucle care loca!')