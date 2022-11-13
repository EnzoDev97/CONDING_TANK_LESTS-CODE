# 11 - Faça um programa que pede para o usuário digitar 5 números e, ao final, imprime uma lista com os 5 números digitados pelo usuário (sem converter para int ou float)

lista = []

for i in range(5):
    lista.append(input('Digite um número: '))

print(lista)
print('-'*100)
# CONVERTENDO PARA FLOAT

for i in range(len(lista)):
    lista[i] = float(lista[i])
    
print(lista)
