# 05 - Faça um programa que imprima todos os itens de uma lista usando while e compare com o exercício 1.

lista = [55,6987,'ENZO', 22.70]

for i in range(len(lista)):
    print(lista[i])

print('-'*100)
#OU 

lista = [55,6987,'ENZO', 22.70]
count = 0
while count < len(lista):
    print(lista[count])
    count += 1