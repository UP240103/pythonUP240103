# Ejercicio 1: Edad para conducir
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Tienes edad suficiente para aprender a conducir.")
else:
    print(f"Necesitas esperar {18 - edad} años más para aprender a conducir.")

# Ejercicio 2: Comparación de edades
mi_edad = 25
tu_edad = int(input("Ingresa tu edad: "))
diferencia = abs(tu_edad - mi_edad)

if tu_edad > mi_edad:
    print(f"Eres {diferencia} {'año' if diferencia == 1 else 'años'} mayor que yo.")
elif tu_edad < mi_edad:
    print(f"Soy {diferencia} {'año' if diferencia == 1 else 'años'} mayor que tú.")
else:
    print("Tenemos la misma edad.")

# Ejercicio 3: Comparación de dos números
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")
