# 01 - Faça um programa que peça ao usuário um número e imprima todos os números de um até o número dado.

numero = int(input('Digite um número: ')) # entrada do usuário e limite da contagem
contador = 1   # variável de contagem

while contador <= numero: # laço de repetição

    print(contador) # exibição da variável na tela

    contador = contador + 1 # incremento