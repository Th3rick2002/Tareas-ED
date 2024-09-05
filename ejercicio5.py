vector = [1,2,3,4,5,6]
inicio = 0
final = len(vector)
vector_invertido = []

for i in range(final,inicio,-1):
    vector_invertido.append(vector[i - 1])

print(vector_invertido)