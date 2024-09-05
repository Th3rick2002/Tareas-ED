numeros = []
contador = 0
print("Ingrese 8 números")

for i in range (0,8):
    numeros.append(int(input(f"Ingrese el {i + 1}° número: ")))

for i in numeros:
    if i > 1:
        contador += 1

print(f"La cantidad de números positivos es: {contador}")