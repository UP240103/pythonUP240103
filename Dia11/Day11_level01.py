# 1. Función que suma dos números
def add_two_numbers(a, b):
    return a + b

# 2. Área de un círculo
def area_of_circle(r):
    pi = 3.1416
    return pi * r * r

# 3. Suma arbitraria de números, validando que sean números
def add_all_nums(*args):
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
            return "Error: todos los argumentos deben ser números."
        total += num
    return total

# 4. Convertir Celsius a Fahrenheit
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# 5. Función para obtener la estación según el mes
def check_season(month):
    month = month.lower()
    autumn = ['september', 'october', 'november']
    winter = ['december', 'january', 'february']
    spring = ['march', 'april', 'may']
    summer = ['june', 'july', 'august']
    if month in autumn:
        return "Autumn"
    elif month in winter:
        return "Winter"
    elif month in spring:
        return "Spring"
    elif month in summer:
        return "Summer"
    else:
        return "Mes inválido"

# 6. Calcular pendiente (slope) entre dos puntos
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Pendiente indefinida (división por cero)."
    return (y2 - y1) / (x2 - x1)

# 7. Resolver ecuación cuadrática ax² + bx + c = 0
def solve_quadratic_eqn(a, b, c):
    import math
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Raíces complejas."
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    return root1, root2

# 8. Imprimir elementos de una lista
def print_list(lst):
    for item in lst:
        print(item)

# 9. Invertir una lista usando bucle
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

# 10. Capitalizar los items de una lista
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

# 11. Agregar un item a la lista
def add_item(lst, item):
    lst.append(item)
    return lst

# 12. Remover un item de la lista
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# 13. Suma de números hasta n
def sum_of_numbers(n):
    return sum(range(n+1))

# 14. Suma de números impares hasta n
def sum_of_odds(n):
    return sum(i for i in range(n+1) if i % 2 != 0)

# 15. Suma de números pares hasta n
def sum_of_even(n):
    return sum(i for i in range(n+1) if i % 2 == 0)

# Ejemplos de uso:
print(add_two_numbers(3, 5))          # 8
print(area_of_circle(3))               # 28.2744 aprox
print(add_all_nums(1, 2, 3, 4))       # 10
print(convert_celsius_to_fahrenheit(0))  # 32.0
print(check_season("October"))         # Autumn
print(calculate_slope(1, 2, 3, 6))     # 2.0
print(solve_quadratic_eqn(1, -3, 2))   # (2.0, 1.0)
print_list(["Python", "Java", "C++"])
print(reverse_list([1, 2, 3]))          # [3, 2, 1]
print(capitalize_list_items(["manzana", "pera"])) # ['Manzana', 'Pera']
print(add_item([1,2,3], 4))             # [1,2,3,4]
print(remove_item([1,2,3], 2))          # [1,3]
print(sum_of_numbers(5))                 # 15
print(sum_of_odds(10))                   # 25
print(sum_of_even(10))                   # 30
