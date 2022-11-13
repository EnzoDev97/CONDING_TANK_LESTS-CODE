# 08 - Agora usando a função max() faça um programa que imprima os três maiores números de uma lista.

lista = [4,5,8,3,48,15,18,23]

for i in range(3):
    print(max(lista))
    lista.remove(max(lista))