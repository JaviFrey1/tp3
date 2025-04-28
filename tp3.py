# TP3: Estructuras condicionales


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
