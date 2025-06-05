# Declarar variables
Nombre = "Nery"
Apellido = "Mata"
Nombre_completo = "Nery Antonio Mata Salas"
Pais = "Mexico"
Ciudad = "Ciudad Gotica"
edad = 18
año_d_nacimiento = 2006
estado_civil = "soltero"
casado = False
esta_pendejo = True  

# Mostrar el tipo de cada variable
print(type(Nombre))
print(type(Apellido))
print(type(Nombre_completo))
print(type(Pais))
print(type(Ciudad))
print(type(edad))
print(type(año_d_nacimiento))
print(type(estado_civil))
print(type(casado))
print(type(esta_pendejo))

#Comparacion entre nombre y apellido
len(Nombre)
if len(Nombre)> len(Apellido) :
  print("El nombre es mas largo que el apellido")
elif len(Nombre)< len(Apellido) :
  print('El apellido es mas largo que el nombre')
else:
  print('Me quedo grande muchachos')


#Operaciones y su resultado
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print("Total:", total)
print("Diferencia:", diff)
print("Producto:", product)
print("División:", division)
print("Resto:", remainder)
print("Potencia:", exp)
print("División entera:", floor_division)

# Círculo con radio fijo
radio = 30
pi = 3.141592653589793

area_of_circle = pi * radio ** 2
circum_of_circle = 2 * pi * radio

print("Área del círculo:", area_of_circle)
print("Circunferencia del círculo:", circum_of_circle)

# Calcular área con radio dado por el usuario
radio_usuario = float(input("Ingresa el radio del círculo: "))
area_usuario = pi * radio_usuario ** 2
print("Área del círculo con radio", radio_usuario, "es:", area_usuario)

# Datos del usuario
nombre_usuario = input("¿Cuál es tu primer nombre? ")
apellido_usuario = input("¿Cuál es tu apellido? ")
pais_usuario = input("¿De qué país eres? ")
edad_usuario = int(input("¿Cuántos años tienes? "))

print("Hola,", nombre_usuario, apellido_usuario + ", de", pais_usuario + ", con", edad_usuario, "años.")

help('keywords')
