# Ejercicio 1: Calificación según puntaje
puntaje = int(input("Ingresa tu puntaje: "))

if 80 <= puntaje <= 100:
    print("Calificación: A")
elif 70 <= puntaje <= 79:
    print("Calificación: B")
elif 60 <= puntaje <= 69:
    print("Calificación: C")
elif 50 <= puntaje <= 59:
    print("Calificación: D")
elif 0 <= puntaje <= 49:
    print("Calificación: F")
else:
    print("Puntaje inválido.")

# Ejercicio 2: Estación del año según el mes
mes = input("Ingresa un mes: ").capitalize()

if mes in ["Septiembre", "Octubre", "Noviembre"]:
    print("La estación es Otoño.")
elif mes in ["Diciembre", "Enero", "Febrero"]:
    print("La estación es Invierno.")
elif mes in ["Marzo", "Abril", "Mayo"]:
    print("La estación es Primavera.")
elif mes in ["Junio", "Julio", "Agosto"]:
    print("La estación es Verano.")
else:
    print("Mes no válido.")

# Ejercicio 3: Verificación y adición de frutas
frutas = ['banana', 'naranja', 'mango', 'limón']
fruta = input("Ingresa una fruta: ").lower()

if fruta in frutas:
    print("Esa fruta ya está en la lista.")
else:
    frutas.append(fruta)
    print("Fruta añadida. Lista actualizada:", frutas)
