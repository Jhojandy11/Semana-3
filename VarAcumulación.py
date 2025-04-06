#Objetivo : Uso de Variable Aculación Letras (Hcer mientras)
#Nombre ; Michue Izquierdo Jhojandy Azariel 
#Fechas: 05/04/2025

i = 0       # Variable de incremento
varAcumulación = 0  # Variable de acumulación
while( i <= 3):   # mientras (que sean menores a igual a 3)
    monto = int ( input('ingrese un monto ')) #solicitando un monto entero
    varAcumulación = varAcumulación + monto 
    i += 1


print('Acumulado es: ',varAcumulación)  #Estoy imprimiendo el resultado del acumulado