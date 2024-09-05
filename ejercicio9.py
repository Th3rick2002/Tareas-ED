matriz1 = []
matriz2 = []

print("Ingresa los datos")
print("Datos para la primera matriz")

for i in range(2):
    fila = []
    for j in range(2):
        mumero = int(input(f"Ingrese el dato [{i+1}][{j+1}]: "))
        fila.append(mumero)
    matriz1.append(fila)

print("Datos para la segunda matriz")

for i in range(2):
    fila = []
    for j in range(2):
        numero = int(input(f"Ingrese el dato [{i+1}][{j+1}]: "))
        fila.append(numero)
    matriz2.append(fila)

print("Multiplicacion de las matrices")
resultado = []

for i in range(2):
    fila = []
    for j in range(2):
        suma = 0
        for k in range(2)   :
            suma += matriz1[i][k] * matriz2[k][j]
        fila.append(suma)
    resultado.append(fila)

print("El resultado de la multiplicación es:")
for fila in resultado:
    print(fila)