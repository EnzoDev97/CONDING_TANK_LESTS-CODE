#14 - Faça um programa que sorteie 10 números entre 0 e 100 e imprima:

# a. O maior número sorteado
# b. o menor número sorteado
# c. a média dos números sorteados
# d. A soma dos números sorteados

import random

lista = []
media = 0
for i in range(10):
    lista.append(random.randint(0,100))
    media += lista[i]
    
print(f'O maior número sorteado foi: {max(lista)}')
print(f'O menor número sorteado foi: {min(lista)}')
print(f'A media dos números sorteados foi: {media/len(lista)}')
print(f'A soma dos números sorteados foi: {media}')

print(f'Lista final foi: {lista}')