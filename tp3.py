# TP3: Estructuras condicionales

import random
from statistics import mode, median, mean

# Ej 1
edad = int(input("Ingresa tu edad: "))
if edad > 18:
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")

# Ej 2

nota = int(input("Ingresa tu nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# Ej 3

numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# Ej 4

edad = int(input("Ingresa tu edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")



# Ej 5

contrasena = input("Ingrese su contraseña (entre 8 y 14 caracteres): ")

if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")




# Ej 6

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]


moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)


print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")


if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
else:
    print("Sin sesgo")


# Ej 7

frase = input("Ingrese una frase o palabra: ")

# Verificamos si la última letra es una vocal
if frase: 
  if frase[-1].lower() in "aeiou":
      print(frase + "!")
  else:
      print(frase)



# Ej 8

nombre = input("Ingrese su nombre: ")
opcion = int(input("Elija una opción: 1. Mayúsculas 2. Minúsculas 3. Primera letra mayúscula: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")


# Ej 9

magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")









# Ej 10

hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").strip().upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes (1-31): "))

# Determinamos la estación del año en base al hemisferio y la fecha
if hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (mes >= 1 and mes <= 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes >= 4 and mes <= 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes >= 7 and mes <= 9 and dia <= 20):
        print("Verano")
    else:
        print("Otoño")
elif hemisferio == 'S':
    if (mes == 12 and dia >= 21) or (mes >= 1 and mes <= 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (mes >= 4 and mes <= 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes >= 7 and mes <= 9 and dia <= 20):
        print("Invierno")
    else:
        print("Primavera")
else:
    print("Hemisferio no válido. Por favor, ingrese 'N' para el hemisferio norte o 'S' para el hemisferio sur.")
