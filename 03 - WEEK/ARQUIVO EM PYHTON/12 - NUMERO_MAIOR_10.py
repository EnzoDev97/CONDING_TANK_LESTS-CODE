numero = 0
while numero <=10:
    numero=int(input('DIGITE UM NÚMERO MAIOR QUE 10: '))
print('\n')
print('-'*40)    

print('\033[42mO NÚMERO DIGITADO FOI : {}\033[5m'.format(numero))