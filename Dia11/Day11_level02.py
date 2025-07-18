# 1. Contar pares e impares
def evens_and_odds(n):
    evens = sum(1 for i in range(n+1) if i % 2 == 0)
    odds = sum(1 for i in range(n+1) if i % 2 != 0)
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."

# 2. Factorial
def factorial(n):
    if n < 0:
        return "No existe factorial para números negativos."
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# 3. Verificar si una variable está vacía
def is_empty(var):
    if var:
        return False
    return True

# 4. Media de una lista
def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else 0

# 5. Mediana de una lista
def calculate_median(lst):
    n = len(lst)
    if n == 0:
        return None
    sorted_lst = sorted(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid-1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

# 6. Moda de una lista
def calculate_mode(lst):
    from collections import Counter
    if not lst:
        return None
    c = Counter(lst)
    mode_freq = max(c.values())
    modes = [k for k, v in c.items() if v == mode_freq]
    return modes

# 7. Rango de una lista
def calculate_range(lst):
    if not lst:
        return 0
    return max(lst) - min(lst)

# 8. Varianza de una lista
def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst) if lst else 0

# 9. Desviación estándar
def calculate_std(lst):
    import math
    return math.sqrt(calculate_variance(lst))

# Ejemplos:
print(evens_and_odds(100))
print(factorial(5))        # 120
print(is_empty([]))        # True
print(calculate_mean([1,2,3]))  # 2.0
print(calculate_median([1,3,2])) # 2
print(calculate_mode([1,1,2,3,3,3])) # [3]
print(calculate_range([1,10])) # 9
print(calculate_variance([1,2,3]))  # 0.666...
print(calculate_std([1,2,3]))       # 0.816...
