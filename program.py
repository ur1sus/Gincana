import random
lista = [random.randint(1, 100) for _ in range(15)]
lista_pares = [num for num in lista if num % 2 == 0]
quantidade_pares = len(lista_pares)
print(f"Lista = {lista}")
print(f"Quantidade de pares = {quantidade_pares}")
print(f"Lista de pares = {lista_pares}")
