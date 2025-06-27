# Concatenaciones
concatenated1 = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
print(concatenated1)  # Thirty Days Of Python

concatenated2 = ' '.join(['Coding', 'For', 'All'])
print(concatenated2)  # Coding For All

# Declarar variable company
company = "Coding For All"
print(company)

# Longitud del string
print(len(company))

# Mayúsculas y minúsculas
print(company.upper())
print(company.lower())

# Métodos de formato
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cortar el primer elemento (word)
print(company[7:])  # For All

# Comprobar si contiene "Coding"
print(company.index("Coding"))  # Devuelve el índice
print(company.find("Coding"))   # Devuelve el índice también

# Reemplazar palabras
print(company.replace("Coding", "Python"))  # Python For All
print("Python for Everyone".replace("Everyone", "All"))  # Python for All

# Split usando espacio
print(company.split())  # ['Coding', 'For', 'All']

# Split usando coma
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(', '))

# Índices específicos
print(company[0])  # C
print(company[-1])  # l
print(company[10])  # A

# Acrónimos
phrase1 = "Python For Everyone"
phrase2 = "Coding For All"
acronym1 = ''.join([word[0] for word in phrase1.split()])
acronym2 = ''.join([word[0] for word in phrase2.split()])
print(acronym1)  # PFE
print(acronym2)  # CFA

# Posiciones de caracteres
print(phrase2.index('C'))  # 0
print(phrase2.index('F'))  # 7
print("Coding For All People".rfind('l'))  # 17

# Encontrar "because"
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))     # 31
print(sentence.rindex('because'))   # 47

# Slice de "because because because"
start = sentence.find('because')
end = sentence.rindex('because') + len('because')
print(sentence[start:end])  # because because because

# Start/End con substrings
print(company.startswith("Coding"))  # True
print(company.endswith("coding"))    # False

# Strip
print('   Coding For All      '.strip())  # 'Coding For All'

# isidentifier
print('30DaysOfPython'.isidentifier())  # False
print('thirty_days_of_python'.isidentifier())  # True

# Unir lista con hash y espacio
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))  # Django # Flask # Bottle # Pyramid # Falcon

# Secuencia de nueva línea
print("I am enjoying this challenge.\nI just wonder what is next.")

# Secuencia de tabulación
print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")

# Formato de string: área de círculo
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius, area))

# Operaciones usando formato de string
a, b = 8, 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
