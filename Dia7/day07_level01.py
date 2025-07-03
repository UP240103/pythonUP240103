# Nivel 1

# Conjuntos dados
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Longitud del conjunto it_companies
print("Longitud de it_companies:", len(it_companies))

# Agregar 'Twitter'
it_companies.add('Twitter')
print("Después de agregar Twitter:", it_companies)

# Insertar múltiples compañías
it_companies.update(['Tesla', 'Samsung', 'Intel'])
print("Después de agregar varias compañías:", it_companies)

# Eliminar una compañía (por ejemplo 'IBM')
it_companies.remove('IBM')  # Si no existe, da error
print("Después de eliminar IBM:", it_companies)

# Diferencia entre remove y discard:
# remove lanza error si el elemento no existe.
# discard NO lanza error si el elemento no existe.
it_companies.discard('Netflix')  # No pasa nada si no existe

# Nivel 2


# Unión de A y B
union_ab = A.union(B)
print("Unión de A y B:", union_ab)

# Intersección de A y B
interseccion = A.intersection(B)
print("Intersección de A y B:", interseccion)

# ¿A es subconjunto de B?
print("¿A es subconjunto de B?", A.issubset(B))

# ¿A y B son disjuntos?
print("¿A y B son disjuntos?", A.isdisjoint(B))

# Unión A con B y B con A (mismo resultado)
print("A unido con B:", A.union(B))
print("B unido con A:", B.union(A))

# Diferencia simétrica (elementos que están en A o en B, pero no en ambos)
symmetric_diff = A.symmetric_difference(B)
print("Diferencia simétrica entre A y B:", symmetric_diff)

# Eliminar los conjuntos completamente
del A
del B


# Nivel 3


# Convertir 'age' a conjunto
age_set = set(age)
print("Lista age:", age)
print("Set age_set:", age_set)
print("¿Cuál es más grande? Lista:", len(age), "vs Set:", len(age_set))

# Diferencias entre tipos de datos
# String: cadena de texto (ej: "Hola")
# List: lista ordenada y modificable (ej: [1, 2, 3])
# Tuple: lista ordenada e inmutable (ej: (1, 2, 3))
# Set: colección no ordenada y sin elementos duplicados (ej: {1, 2, 3})

# Frase dada
frase = "I am a teacher and I love to inspire and teach people"

# Contar palabras únicas
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
print("Número de palabras únicas:", len(palabras_unicas))
