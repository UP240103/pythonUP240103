# Declaración de variables
edad = 25  # variable entera
altura = 1.75  # variable de tipo float
numero_complejo = 3 + 4j  # variable con número complejo

# Área de un triángulo
base = float(input("Introduce la base del triángulo: "))  # Ejemplo: 20
altura_triangulo = float(input("Introduce la altura del triángulo: "))  # Ejemplo: 10
area_triangulo = 0.5 * base * altura_triangulo
print("El área del triángulo es", area_triangulo)

# Perímetro de un triángulo
a = float(input("Introduce el lado a: "))  # Ejemplo: 5
b = float(input("Introduce el lado b: "))  # Ejemplo: 4
c = float(input("Introduce el lado c: "))  # Ejemplo: 3
perimetro = a + b + c
print("El perímetro del triángulo es", perimetro)

# Área y perímetro de un rectángulo
largo = float(input("Introduce el largo del rectángulo: "))
ancho = float(input("Introduce el ancho del rectángulo: "))
area_rectangulo = largo * ancho
perimetro_rectangulo = 2 * (largo + ancho)
print("Área del rectángulo:", area_rectangulo)
print("Perímetro del rectángulo:", perimetro_rectangulo)

# Área y circunferencia de un círculo
radio = float(input("Introduce el radio del círculo: "))
pi = 3.14
area_circulo = pi * radio * radio
circunferencia = 2 * pi * radio
print("Área del círculo:", area_circulo)
print("Circunferencia del círculo:", circunferencia)

# y = 2x - 2
# Pendiente (m), intersección en y (b), intersección en x (cuando y=0)
pendiente = 2
interseccion_y = -2
interseccion_x = interseccion_y / -pendiente
print("Pendiente:", pendiente)
print("Intersección en y:", interseccion_y)
print("Intersección en x:", interseccion_x)

# Distancia y pendiente entre dos puntos
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente_puntos = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Pendiente entre los puntos:", pendiente_puntos)
print("Distancia euclidiana:", distancia)

# Comparar pendientes
print("¿Las pendientes son iguales?", pendiente == pendiente_puntos)

# y = x^2 + 6x + 9. ¿Para qué x, y = 0?
# Factorizando: (x + 3)^2 = 0 => x = -3
for x in range(-10, 11):
    y = x**2 + 6*x + 9
    print(f"x={x}, y={y}")

# Comparación de longitud de palabras
palabra1 = 'python'
palabra2 = 'dragon'
print("Longitud 'python':", len(palabra1))
print("Longitud 'dragon':", len(palabra2))
print("¿Longitudes son iguales?", len(palabra1) == len(palabra2))

# Verificar si 'on' está en ambas palabras
print("'on' en 'python' y 'dragon':", 'on' in palabra1 and 'on' in palabra2)

# Verificar si hay 'jargon' en la oración
oracion = "Espero que este curso no esté lleno de jerga."
print("¿'jargon' está en la oración?", 'jargon' in oracion.lower())

# Negación
print("No hay 'on' en ambas:", not ('on' in palabra1 and 'on' in palabra2))

# Convertir longitud de 'python'
longitud_python = len('python')
print("Convertido a float:", float(longitud_python))
print("Convertido a string:", str(longitud_python))

# Verificar si un número es par
numero = int(input("Introduce un número para verificar si es par: "))
print("¿Es par?", numero % 2 == 0)

# División de piso
print("¿7 // 3 == int(2.7)?", 7 // 3 == int(2.7))

# Comparación de tipos
print("¿Tipo de '10' es igual al de 10?", type('10') == type(10))

# int('9.8') falla, así que:
try:
    print(int('9.8') == 10)
except ValueError:
    print("No se puede convertir '9.8' a int directamente.")

# Cálculo de pago semanal
horas = float(input("Introduce las horas trabajadas: "))  # Ej: 40
tarifa = float(input("Introduce la tarifa por hora: "))  # Ej: 28
ganancia = horas * tarifa
print("Tu ganancia semanal es", ganancia)

# Cálculo de segundos vividos
anios = int(input("Introduce los años que has vivido: "))  # Ej: 100
segundos_vividos = anios * 365 * 24 * 60 * 60
print("Has vivido aproximadamente", segundos_vividos, "segundos.")

# Imprimir tabla
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
