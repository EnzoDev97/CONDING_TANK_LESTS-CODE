#08 - Faça um programa que peça um número para o usuário (string), converta-o para float e depois imprima-o na tela.
#Você consegue fazer a mesma coisa, porém convertendo para int?

a = input('DIGITE UM NÚMERO : ') 
print('-'*40) 
print('\n')

a_int = int(a) 
a_float = float(a)

print('='*40) 
print('\033[42m O NÚMERO {} ESTÁ NO FORMATO STRING\033[0m'.format(a)) 
print('\033[43m O NÚMERO {} ESTÁ NO FORMATO INT\033[0m'.format(a_int)) 
print('\033[44m O NÚMERO {} ESTÁ NO FORMATO FLOAT\033[0m'.format(a_float)) 
print('='*40)