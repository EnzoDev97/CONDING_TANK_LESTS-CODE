# 03 - Peça ao usuário para digitar um número N e some todos os números de 1 a N utilizando o laço de repetição while.


#03 ) Peça ao usuário para digitar um número N e some todos os números de 1 a N utilizando o laço de repetição while.

number = int(input('Digite um número inteiro : '))

while number <= 0:
     number = int(input('Digite um número inteiro maior que zero: '))

i = 1
adicao = i
while i < number:
    i += 1
    adicao+= i
print(f'A soma de 1 a {number} é {adicao}.')