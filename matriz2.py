'''
3 - Faça uma matriz 5x5 com números aleatórios no intervalo entre 
1 e 10 e exiba a matriz. Em seguida, calcule e exiba a soma da diagonal que 
começa na posição [0][0].
Saída:
Matriz:
9 1 5 1 1 
8 6 8 4 7 
9 6 3 8 4 
3 9 9 7 3 
4 8 3 9 8 
Soma da diagonal: 33
'''
import random
matriz = []
for i in range(5):
  linha = []
  for j in range(5):
    numero = random.randint(1,10)
    linha.append(numero)
    matriz.append(linha)

print("Matriz:")
for i in range(5):
  for j in range(5):
    print(matriz[i][j], end=" ")
  print ()
  soma_diagonal = 0
  for i in range(5):
    soma_diagonal += matriz [i][i]
  print()
  print("Soma da diagonal:", soma_diagonal)
