matriz = []

for i in range(2):
    filas = []
    for j in range(3):
        filas.append(int(input(f"Ingrese el valor [{i + 1}][{j + 1}]: ")))

    matriz.append(filas)

for fila in matriz:
    print(fila)

traspuesta = [[matriz[j][i] for j in range(2)] for i in range(3)]

for fila in traspuesta:
    print(fila) 