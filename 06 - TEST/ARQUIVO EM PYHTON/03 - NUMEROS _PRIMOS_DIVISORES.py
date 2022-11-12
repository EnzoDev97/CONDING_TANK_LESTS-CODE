#03 - Dado um número fornecido pelo usuário, faça um programa que teste se é número primo e imprima na tela. 
# Além disso, exiba uma lista de divisores do número testado. Um número primo é divisível somente por 1 e por ele mesmo. Seu programa deve ser funcional para qualquer número até o 100.


numero = int(input("Digite o numero DE 0 Á 100 : "))
divisor = 2
print('_'*50)
print('\n')

while divisor < numero:
  if numero % divisor == 0:
    print('O NÚMERO NÃO É PRIMO')
    break
  divisor += 1
else:
  print('O NÚMERO É PRIMO')

print('-'*50)
print('\n')

print ('O NÚMERO {} POSSUI OS SEGUINTES DIVISORES.......'.format(numero))

print('='*50)
for  i in range(1, numero + 1):
    if numero % i == 0:
        print('{:^50}'.format(i))
print('='*50)