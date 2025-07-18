# 1. Verificar si un número es primo
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 2. Verificar si todos los items en lista son únicos
def all_unique(lst):
    return len(lst) == len(set(lst))

# 3. Verificar si todos los items son del mismo tipo
def all_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(isinstance(x, first_type) for x in lst)

# 4. Validar si variable es válida en Python (simplificado)
def is_valid_variable(var):
    import keyword
    if not var.isidentifier() or keyword.iskeyword(var):
        return False
    return True

# 5. Importamos datos simulados (simula archivo countries_data.py)
countries_data = [
    {'name': 'China', 'population': 1439323776, 'languages': ['Chinese']},
    {'name': 'India', 'population': 1380004385, 'languages': ['Hindi', 'English']},
    {'name': 'USA', 'population': 331002651, 'languages': ['English']},
    {'name': 'Indonesia', 'population': 273523615, 'languages': ['Indonesian']},
    {'name': 'Pakistan', 'population': 220892340, 'languages': ['Urdu', 'English']},
    {'name': 'Brazil', 'population': 212559417, 'languages': ['Portuguese']},
    {'name': 'Nigeria', 'population': 206139589, 'languages': ['English']},
    {'name': 'Bangladesh', 'population': 164689383, 'languages': ['Bengali']},
    {'name': 'Russia', 'population': 145934462, 'languages': ['Russian']},
    {'name': 'Mexico', 'population': 128932753, 'languages': ['Spanish']},
   
]

# 6. Top 10 idiomas más hablados (descendente)
def most_spoken_languages(data, top=10):
    lang_count = {}
    for country in data:
        for lang in country['languages']:
            lang_count[lang] = lang_count.get(lang, 0) + 1
    sorted_lang = sorted(lang_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_lang[:top]

# 7. Top 10 países más poblados (descendente)
def most_populated_countries(data, top=10):
    sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:top]

# Ejemplos:
print(is_prime(17))               # True
print(all_unique([1,2,3,3]))     # False
print(all_same_type([1,2,3]))    # True
print(is_valid_variable('var_1'))  # True
print(is_valid_variable('1var'))    # False

print(most_spoken_languages(countries_data))
print(most_populated_countries(countries_data))
print("¿El número 17 es primo?")
print(f"Respuesta: {'Sí' if is_prime(17) else 'No'}\n")

print("¿Todos los elementos son únicos en la lista [1, 2, 3, 3]?")
print(f"Respuesta: {'Sí' if all_unique([1, 2, 3, 3]) else 'No'}\n")

print("¿Todos los elementos son del mismo tipo en la lista [1, 2, 3]?")
print(f"Respuesta: {'Sí' if all_same_type([1, 2, 3]) else 'No'}\n")

print("¿'var_1' es un nombre válido de variable en Python?")
print(f"Respuesta: {'Sí' if is_valid_variable('var_1') else 'No'}\n")

print("¿'1var' es un nombre válido de variable en Python?")
print(f"Respuesta: {'Sí' if is_valid_variable('1var') else 'No'}\n")

print("Las 10 lenguas más habladas según los datos:")
for lang, count in most_spoken_languages(countries_data):
    print(f"- {lang}: en {count} países")

print("\nLos 10 países más poblados según los datos:")
for c in most_populated_countries(countries_data):
    print(f"- {c['name']} con {c['population']:,} habitantes")