numeros = []
mayor = 0
print("Ingrese 7 números para calcular el mayor de ellos")

for i in range (0,7):
    numeros.append(int(input(f"Ingrese el {i + 1}° número: ")))

for i in numeros:
    if i > mayor:
        mayor = i

print(f"El mayor es: {mayor}")