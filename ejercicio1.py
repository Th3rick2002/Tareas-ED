numeros = []

for i in range(0,5):
    numero = float(input(f"Ingrese el {i + 1} numero: "))
    numeros.append(numero)

print(sum(numeros))