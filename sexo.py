#Objetivo :elije tu sex0:
#NOMBRE Y APELLIDO: Jhojandy Azariel Michue Izquierdo 
#FECHA: 06/04/2025


while(True):
    generoIngresado= str ( input("Ingrese un genero (M/F/O): "))
    if (generoIngresado.upper() == 'M' and generoIngresado.upper() == 'F' or generoIngresado.upper() == 'O' ) :
        break
    print('Error ')
    
if (generoIngresado  == 'M' ) :
    print('El genero ingresado es MASCULINO !')
elif ( generoIngresado  == 'F' ) :
    print('El genero ingresadp es Femenino') 
else:
    print('El genero ingresado es OTROS')

