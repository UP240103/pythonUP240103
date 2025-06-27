# Lista vacía
lista_vacía = []

# Lista con más de 5 elementos
artículos = ['ratón', 'teclado', 'monitor', 'USB', 'HDMI', 'laptop']

# Longitud de la lista
print("Longitud:", len(artículos))

# Primer, medio y último elemento
print("Primer elemento:", artículos[0])
print("Elemento del medio:", artículos[len(artículos)//2])
print("Último elemento:", artículos[-1])

# Tipos de datos mixtos
tipos_de_datos_mixtos = ['Juan', 22, 1.75, 'Soltero', 'Calle Principal 123']
print("Datos mixtos:", tipos_de_datos_mixtos)

# Lista de empresas de TI
empresas_ti = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("Empresas de TI:", empresas_ti)
print("Número de empresas:", len(empresas_ti))
print("Primera empresa:", empresas_ti[0])
print("Empresa del medio:", empresas_ti[len(empresas_ti)//2])
print("Última empresa:", empresas_ti[-1])

# Modificar una empresa
empresas_ti[1] = 'Alphabet'
print("Lista modificada:", empresas_ti)

# Agregar una nueva empresa
empresas_ti.append('Tesla')
print("Después de agregar:", empresas_ti)

# Insertar en el medio
empresas_ti.insert(len(empresas_ti)//2, 'Intel')
print("Después de insertar:", empresas_ti)

# Cambiar una empresa a mayúsculas (excluyendo IBM)
for i in range(len(empresas_ti)):
    if empresas_ti[i] != 'IBM':
        empresas_ti[i] = empresas_ti[i].upper()
        break
print("Después de poner una empresa en mayúsculas:", empresas_ti)

# Unir con '#;  '
print("Unido con '#;  ':", '#;  '.join(empresas_ti))

# Verificar si existe una empresa
print("¿Existe 'AMAZON'?:", 'AMAZON' in empresas_ti)

# Ordenar lista
empresas_ti.sort()
print("Ordenado:", empresas_ti)

# Invertir lista
empresas_ti.reverse()
print("Invertido:", empresas_ti)

# Primeras 3 empresas
print("Primeras 3:", empresas_ti[:3])

# Últimas 3 empresas
print("Últimas 3:", empresas_ti[-3:])

# Empresa(s) del medio
mid = len(empresas_ti) // 2
print("Medio:", empresas_ti[mid-1:mid+1] if len(empresas_ti) % 2 == 0 else [empresas_ti[mid]])

# Eliminar primera empresa
empresas_ti.pop(0)
print("Después de eliminar la primera:", empresas_ti)

# Eliminar del medio
mid = len(empresas_ti) // 2
empresas_ti.pop(mid)
print("Después de eliminar la del medio:", empresas_ti)

# Eliminar la última
empresas_ti.pop()
print("Después de eliminar la última:", empresas_ti)

# Eliminar todo
empresas_ti.clear()
print("Después de limpiar todo:", empresas_ti)

# Destruir lista
del empresas_ti
print("empresas_ti destruida.")

# Unir listas
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end

# Insertar Python y SQL después de Redux
index_redux = full_stack.index('Redux')
full_stack.insert(index_redux + 1, 'Python')
full_stack.insert(index_redux + 2, 'SQL')
print("Full stack:", full_stack)

# --- Nivel 2 ---

edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
edades.sort()
print("Edades ordenadas:", edades)

# Mínimo y máximo
edad_mínima = min(edades)
edad_máxima = max(edades)
print("Edad mínima:", edad_mínima)
print("Edad máxima:", edad_máxima)

# Agregar nuevamente mínimo y máximo
edades.append(edad_mínima)
edades.append(edad_máxima)
print("Edades con mínimo y máximo añadidos:", edades)

# Mediana
edades.sort()
n = len(edades)
mediana = (edades[n//2] + edades[n//2 - 1]) / 2 if n % 2 == 0 else edades[n//2]
print("Mediana:", mediana)

# Promedio
promedio = sum(edades) / len(edades)
print("Promedio:", promedio)

# Rango
print("Rango:", max(edades) - min(edades))

# Comparar abs(min - promedio) vs abs(max - promedio)
print("abs(min - promedio):", abs(edad_mínima - promedio))
print("abs(max - promedio):", abs(edad_máxima - promedio))

# Lista de países
paises = ['China', 'Rusia', 'EE.UU.', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']

# País(es) del medio
índice_medio = len(paises) // 2
if len(paises) % 2 == 0:
    print("Países del medio:", paises[índice_medio - 1: índice_medio + 1])
else:
    print("País del medio:", paises[índice_medio])

# Dividir en dos listas
primera_mitad = paises[: (len(paises) + 1) // 2]
segunda_mitad = paises[(len(paises) + 1) // 2:]
print("Primera mitad:", primera_mitad)
print("Segunda mitad:", segunda_mitad)

# Desempaquetar los primeros 3 y el resto como escandinavos
primer_pais, segundo_pais, tercer_pais, *escandinavos = paises
print("Primeros 3 países:", primer_pais, segundo_pais, tercer_pais)
print("Países escandinavos:", escandinavos)
