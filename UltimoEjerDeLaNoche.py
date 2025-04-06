#Objetivo : Uso de todo lo aprendido:
# 1. Validar el ingreso de un número de 2 a 4 ( enteros )

#Nombre ; Michue Izquierdo Jhojandy Azariel 
#Fechas: 05/04/2025


while (True):
      Número = int(input("Ingrese un número entero entre 2 y 4: "))
      if ((Número  >= 2 and Número <= 4)):
        break 
      print("Número inválido. Intente nuevamente.")
      
 #Objetivo : Uso de todo lo aprendido:
# 2. Validar el ingreso con la opción A


while (True):
    Letra = str ( input("Ingrese la opción 'A': "))
    if Letra.upper () == 'A':
      break
    print("Opción inválida. Intente nuevamente.")

# 3. con el número ingresado en el punto 1, realizar las interacciones en el while
      
i= 0   #Variable de incremento
VarAcumulación = 1  #variable de acumulación
while ( i <= Número ) :  # mientras ( sean menores igual a 3)
  monto = int ( input('ingrese un monto : ')) # ingresando un monto entero
  VarAcumulación = VarAcumulación * monto # acumulando los monto en la variable VarAcumulación
  i += 1

# 4. imprime la multiplicasión acumulada

print ('Acumulado es : ',VarAcumulación)

