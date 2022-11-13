#  04 - Faça um script que reproduza o padrão usando "" a seguir de acordo com o número de linhas desejadas pelo usuário. Dica: print(5 '@')

number = None 

while type(number) != int: 
    number = int(input('Digite um número inteiro: '))

i = 0 
while i < number: 
    print('*'*(i+1)) 
    i += 1