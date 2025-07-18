# 1. For loop del 0 al 10
print("Del 0 al 10 (for loop):")
for i in range(11):
    print(i, end=' ')

# 2. While loop del 0 al 10
print("\n\nDel 0 al 10 (while loop):")
i = 0
while i <= 10:
    print(i, end=' ')
    i += 1

# 3. For loop del 10 al 0
print("\n\nDel 10 al 0 (for loop):")
for i in range(10, -1, -1):
    print(i, end=' ')

# 4. While loop del 10 al 0
print("\n\nDel 10 al 0 (while loop):")
i = 10
while i >= 0:
    print(i, end=' ')
    i -= 1

# 5. Triángulo con "#"
print("\n\nTriángulo:")
for i in range(1, 8):
    print("#" * i)

# 6. Patrón cuadrado de "#"
print("\nCuadro de #:")
for _ in range(8):
    print("# " * 8)

# 7. Tabla de cuadrados
print("\nTabla de cuadrados:")
for i in range(11):
    print(f"{i} x {i} = {i*i}")

# 8. Imprimir tecnologías
print("\nLibrerías populares:")
techs = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in techs:
    print(tech)

# 9. Números pares del 0 al 100
print("\nNúmeros pares del 0 al 100:")
for i in range(0, 101, 2):
    print(i, end=' ')

# 10. Números impares del 0 al 100
print("\n\nNúmeros impares del 0 al 100:")
for i in range(1, 101, 2):
    print(i, end=' ')
