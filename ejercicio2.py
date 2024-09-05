numeros = []
print("Ingresa 10 números para calcular el promedio")

for i in range(0,10):
    numeros.append(float(input(f"ingrese el {i + 1}° número: ")))

promedio = sum(numeros) / len(numeros)
print(f"El promedio es: {promedio}")