# 03 -  Faça um script que informe o fatorial de um número:

numero = int(input('Digite um número inteiro maior ou igual a zero: ')) 
print('_'*50) 
print('\n')

while numero < 0: 
    numero = int(input('Digite um número inteiro maior ou igual a zero: ')) 

i = 1 
fatorial = 1 

while i < numero:
     i += 1 
     fatorial *= i 
else: 
        fatorial *= 1

print('O fatorial de {} é {}'.format(numero,fatorial))