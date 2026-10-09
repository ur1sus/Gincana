'''
5 - Faça uma matriz de numeros inteiros aleatória 3x3 e exiba. Depois some todos 
os seus valores e mostre para o usuário.
Exemplo:
Sáida
Matriz
10 7 6 
4  2 1 
10 8 1 
A Soma dos valores da matriz é = 49
'''
import random 

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(3):
    for j in range(3):
        matriz[i][j] = random.randint(1, 10)
print("Matriz")
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print()
soma_total = 0
for i in range(3):
    for j in range(3):
        soma_total += matriz[i][j]
print(f"A Soma dos valores da matriz é = {soma_total}")
