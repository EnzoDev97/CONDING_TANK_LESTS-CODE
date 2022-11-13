#04 - Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.

qtd_numeros = int(input('DIGITE QUANTAS TABUADAS É PARA SEREM FEITAS: ')) 
print('_' * 20) 
print('\n')

print('=' * 55) 
print( '|\033[42m{:^53}|\033[0m'.format('TABUADA')) 
print('=' * 55) 
print('\n')



print('=' * 48)
print('|\033[44m{:^10}\033[0m x \033[41m{:^15}\033[0m = \033[43m{:^15}\033[0m|'.format('NÚMERO','MULTIPLICADOR','RESULTADO'))
print('=' * 48)

i = 1
while i < 11:
    print('|{:^10} x {:^15} = {:^15}|'.format( qtd_numeros, i, i*qtd_numeros))
    i += 1
    pass
print('-' * 48) 
print('\n')
