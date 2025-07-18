# 1. Suma del 0 al 100
suma_total = sum(range(101))
print("Suma total de 0 a 100:", suma_total)

# 2. Suma de pares e impares
suma_pares = sum(i for i in range(0, 101, 2))
suma_impares = sum(i for i in range(1, 101, 2))
print("Suma de pares:", suma_pares)
print("Suma de impares:", suma_impares)
