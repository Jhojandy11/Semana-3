#Ud. va ingresar una cantidad de notas (INTERACCIONES)
#2 Debera validar el ingreso de la cantida (DO-WHILE)
#3 validar el ingreso de cada nta (0-20)
#4 Deberá utilizar variables de incremento y acumulación
#5 Deberá acumular las notas y promediariarlas 
#5 Resultado:
#6 Ud. ingreso n notas 
#       La nsuma de las notas es : m
#        El promedio de las notas es: p 

#===============================================================
# Ingrese una cantidad de notas (INTERACIONES): 3

# Ingrese nota 1: 15
# Ingrese nota 2: 16
# Ingrese nota 3: 17

#========RESULTADO=========
#Ud. ingreso: 3 notas 
#La suma de las notas es: 48 
#El promedio de las notas es : 16.00


cantidad_notas = int(input("Ingrese una cantidad de notas (INTERACCIONES): ")) # Se corrige el nombre de la variable a 'cantidad_notas'

while cantidad_notas <= 0:
  print("La cantidad de notas debe ser mayor a cero.")
  cantidad_notas = int(input("Ingrese una cantidad de notas (INTERACCIONES): "))

SumaDeNotas  = 0
for i in range(cantidad_notas):
  nota = int(input(f"Ingrese nota {i + 1}: "))
  while nota < 0 or nota > 20:
    print("Nota inválida. Ingrese una nota entre 0 y 20.")
    nota = int(input(f"Ingrese nota {i + 1}: "))
  SumaDeNotas += nota

promedio_notas = SumaDeNotas / cantidad_notas

print("========RESULTADO=========")
print(f"Ud. ingreso: {cantidad_notas} notas")
print(f"La suma de las notas es: {SumaDeNotas }")
print(f"El promedio de las notas es : {promedio_notas:.2f}")
    


