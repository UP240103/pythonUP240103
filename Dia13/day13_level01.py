# 1. Filtrar solo negativos y ceros usando list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [n for n in numbers if n <= 0]
print("1. Negativos y ceros:", filtered)

# 2. Aplanar lista de listas de listas a lista unidimensional
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print("2. Lista aplanada:", flattened)

# 3. Crear lista de tuplas con potencias según patrón dado
tuples_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("3. Lista de tuplas:")
for tup in tuples_list:
    print(tup)

# 4. Transformar lista de países a lista con mayúsculas y abreviaturas
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
transformed_countries = [[
    country.upper(),
    country[:3].upper(),
    city.upper()
] for [[country, city]] in countries]
print("4. Países transformados:", transformed_countries)

# 5. Cambiar lista de países a lista de diccionarios
dict_countries = [{'country': country.upper(), 'city': city.upper()} for [[country, city]] in countries]
print("5. Lista de diccionarios:", dict_countries)

# 6. Concatenar nombres en lista de strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for [[first, last]] in names]
print("6. Nombres concatenados:", full_names)

# 7. Lambda para calcular pendiente e intercepto de línea
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else None
intercept = lambda x, y, m: y - m * x

print("7. Pendiente de (1,2) a (3,6):", slope(1, 2, 3, 6))
print("   Intercepto con punto (1,2) y pendiente 2:", intercept(1, 2, 2))
