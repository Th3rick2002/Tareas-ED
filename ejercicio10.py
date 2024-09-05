matriz = []

for i in range(3):
    fila = []
    for j in range(3):
        numero = float(input(f"ingrese el {i + 1}° numero"))
        fila.append(numero)
    matriz.append(fila)

diagonal = []
for i in range(3):
    numero = matriz[i][i]
    diagonal.append(numero)

print(f"La diagonal de la matriz es: {diagonal}")