# Diccionario de la persona
persona = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finlandia',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Verificar si tiene la clave 'skills' y mostrar la habilidad del medio
if 'skills' in persona:
    habilidades = persona['skills']
    habilidad_medio = habilidades[len(habilidades)//2]
    print("Habilidad del medio:", habilidad_medio)

# Verificar si tiene habilidad en Python
if 'skills' in persona:
    tiene_python = 'Python' in persona['skills']
    print("¿Tiene habilidad en Python?", tiene_python)

# Determinar tipo de desarrollador
if 'skills' in persona:
    skills_set = set(persona['skills'])

    if skills_set == {'JavaScript', 'React'}:
        print("Es un desarrollador Front End.")
    elif {'Node', 'MongoDB', 'Python'}.issubset(skills_set):
        print("Es un desarrollador Back End.")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print("Es un desarrollador Full Stack.")
    else:
        print("Título desconocido.")

# Información si está casado y vive en Finlandia
if persona['is_marred'] and persona['country'] == 'Finlandia':
    print(f"{persona['first_name']} {persona['last_name']} vive en Finlandia. Está casado.")
