 # Nivel 1

# Crear una tupla vacía
tupla_vacia = ()

# Crear una tupla con nombres de hermanas y hermanos (pueden ser imaginarios)
hermanas = ("Luna", "Sofía", "Camila")
hermanos = ("Leo", "Mateo", "Andrés")

# Unir las tuplas de hermanos y hermanas
hermanos_y_hermanas = hermanas + hermanos

# ¿Cuántos hermanos tienes?
cantidad_hermanos = len(hermanos_y_hermanas)
print("Tengo", cantidad_hermanos, "hermanos/as")

# Agregar padre y madre a la tupla
miembros_familia = hermanos_y_hermanas + ("Carlos", "María")  # Papá y mamá

# Nivel 2

# Desempaquetar hermanos y padres
*solo_hermanos, padre, madre = miembros_familia
print("Hermanos:", solo_hermanos)
print("Padre:", padre)
print("Madre:", madre)

# Crear tuplas de frutas, verduras y productos animales
frutas = ("manzana", "plátano", "mango")
verduras = ("zanahoria", "lechuga", "brócoli")
productos_animales = ("leche", "queso", "huevo")

# Unir todas las tuplas en una sola
alimentos_tp = frutas + verduras + productos_animales

# Convertir la tupla en lista
alimentos_lt = list(alimentos_tp)

# Extraer el elemento del medio
indice_medio = len(alimentos_lt) // 2
if len(alimentos_lt) % 2 == 0:
    elementos_medios = alimentos_lt[indice_medio - 1:indice_medio + 1]
else:
    elementos_medios = [alimentos_lt[indice_medio]]
print("Elemento(s) del medio:", elementos_medios)

# Extraer primeros tres y últimos tres elementos
primeros_tres = alimentos_lt[:3]
ultimos_tres = alimentos_lt[-3:]
print("Primeros tres elementos:", primeros_tres)
print("Últimos tres elementos:", ultimos_tres)

# Eliminar la tupla alimentos_tp
del alimentos_tp

# Verificar si un país está en la tupla
paises_nordicos = ('Dinamarca', 'Finlandia', 'Islandia', 'Noruega', 'Suecia')

print("¿Estonia es un país nórdico?", 'Estonia' in paises_nordicos)
print("¿Islandia es un país nórdico?", 'Islandia' in paises_nordicos)
