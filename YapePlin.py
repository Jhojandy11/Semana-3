#1-UD. va a yapear o plinear montos. Las unicas opciones son 'Y' y 'P'. 
#3. deerá utilizar variables de incremento y acumulación
#si utilizo la forma de pago Yape tendrá una comisión de 0.12
#si utilizo la forma de pago Plin tendrá una comisión de 0.13
#6 El descuento será afectado al total acumulado con descuento

#=======
#Ingrese una opción de pago (Y/P): P
#
#INgrese la cantidad de depositos: 3
#
#Ingrese monto 1: 10
#Ingrese monto 2: 20
#Ingrese monto 3: 30
#
#===== Reporte =====
#El monto acumulado es :60
#El monto acumulado con descuento es : 56
#=====

while(True) :
    Opcióningresado= str(input ('Usuario ingresar una opción de pago (Y/P) :  ' )).upper ()
    if (Opcióningresado == 'Y' or Opcióningresado == 'P') :
        break
    print("\tERROR DE USUARIO .... INGRESE UNA OPCIÓN (Y/P)")
 
 #2-UD. Debera validar el ingreso de los montos (mayor a 0.00) a ingresar (interacciones)
while(True) :
    numeroIngresado = float(input('INGRESE UN NÚMERO MAYOR A S/. 0: ')) 
    if(numeroIngresado > 0.00 ):
        break
    print("\tERROR DE USUARIO .... INGRESE UN NÚMERO MAYOR A  S/. 0 :" )

#REPETITIVA

i=0
montoacumulado = 0
while(i < numeroIngresado) :
    i += 1  # SE INCREMENTA EN UNO
    monto = float(input (f'\tIngrese un monto {i} : '))
    montoacumulado = montoacumulado + monto
    if (Opcióningresado == 'Y') :   ##YAPE
        montoDcto = montoacumulado * 0.12 
    else:
        montoDcto = montoacumulado * 0.13
 
print ('=====REPORTE====')
print(montoacumulado)
print(montoDcto)
print(montoacumulado-montoDcto)
print('=========')