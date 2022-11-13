# 05 - Faça um programa, usando loops, que peça para um usuário digitar um número e que 
#só finaliza quando o usuário digitar 0. Ao final imprima a soma de todos os números digitados.

numero = 0 
number = int(input('Digite um número para somar ou 0 para sair: ')) 
numero += number

while number != 0: 
    number = int(input('Digite um número para somar ou 0 para sair: ')) 
    numero += number

print('_'*100) 
print('\n')

print('A soma dos números dados é {}.'.format(numero))