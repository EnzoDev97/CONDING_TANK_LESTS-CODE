tipo_de_combustivel=input('INFORME O TIPO DO SEU COMBUSTIVEL (A/G): ')

while tipo_de_combustivel.lower() != 'a' and tipo_de_combustivel.lower() != 'g':
    print('\033[41mCOMBUSTIVEL INVALIDO!\033[0m')
    print('-'*60)
    tipo_de_combustivel=input('INFORME O TIPO DO SEU COMBUSTIVEL (A/G): ')
   
print('_'*60)
print('\n')
print('\033[42mO COMBUSTIVEL ESCOLHIDO FOI:\033[0m {}'.format(tipo_de_combustivel.upper()))