# Crear un diccionario vacío llamado dog
dog = {}

# Agregar nombre, color, raza, patas, edad al diccionario dog
dog['name'] = 'Max'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

print("Diccionario dog:", dog)

# Crear un diccionario llamado student
student = {
    'first_name': 'Nery',
    'last_name': 'Antonio',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'HTML'],
    'country': 'Mexico',
    'city': 'Loreto',
    'address': '123 Calle Falsa'
}

# Obtener la longitud del diccionario student
print("Longitud del diccionario student:", len(student))

# Obtener el valor de skills y verificar el tipo de dato
skills = student['skills']
print("Skills:", skills)
print("Tipo de dato de skills:", type(skills))  # Debería ser list

# Modificar skills agregando una o dos habilidades
student['skills'].append('CSS')
student['skills'].append('JavaScript')
print("Skills actualizadas:", student['skills'])

# Obtener las claves del diccionario como lista
keys_list = list(student.keys())
print("Claves del diccionario student:", keys_list)

# Obtener los valores del diccionario como lista
values_list = list(student.values())
print("Valores del diccionario student:", values_list)

# Convertir el diccionario a una lista de tuplas
items_list = list(student.items())
print("Diccionario como lista de tuplas:", items_list)

# Eliminar un elemento del diccionario (por ejemplo, marital_status)
student.pop('marital_status')
print("Diccionario tras eliminar 'marital_status':", student)

# Eliminar por completo uno de los diccionarios (por ejemplo, dog)
del dog

# Verificar que dog ya no existe (esto daría error si intentas imprimirlo)
# print(dog)  # ← Esto daría error si se descomenta


