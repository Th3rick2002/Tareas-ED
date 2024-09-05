matriz = []

print("Ingrese los números para agregar a la matriz")

for i in range(3):
    filas = []
    for j in range(3):
        filas.append(int(input(f"Ingrese el valor para [{i + 1}][{j + 1}]: ]")))

    matriz.append(filas)

suma = [sum(matriz[i]) for i in range(len(matriz))]
suma_total = sum(suma)
print(suma_total)