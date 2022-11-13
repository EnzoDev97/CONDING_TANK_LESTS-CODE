# 07-  Faça um programa que imprima o maior número de uma lista sem usar a função máx()

lista_1 = [4,5,8,3,6,15,18,23]
count = 0
for i in range(len(lista_1)):
    if lista_1[i] % 2 == 0:
        count += 1

print(f'Há {count} números pares!')


print('-'*100)
#OU


from random import randint

def sorteia(lista):
    print('SORTEANDO 10 NÚMEROS...\n')
    for cont in range(0,10):   # ESCOLHENDO A QUANTIDADE DE NÚMEROS QUE DEVE SER SORTEADO
        lista.append(randint(1,100))  # INFORMANDO  QUAIS NUMEROS  PODEM SER SORTEADO
    print(numeros)
    print('_'*50,'\n')

numeros = list()


sorteia(numeros)

c = 0
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        c += 1

print(f'Há {c} números pares!')