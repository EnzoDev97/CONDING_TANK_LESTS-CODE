import datetime


def parque_diversao(ano,altura):
    data_nascimento = int(input('INFORME O ANO DO SEU NASCIMENTO: '))
    hoje = datetime.date.today()        #print('{:%d/%b/%Y}'.format(hoje))  # fORMATO DO DIA/MES/ANO
    convert = str(hoje)       #CONVERTENDO A DATA EM STRING
    ano = convert.split('-')   #REMOVENDO O CARACTERE '/'
    ano_1 = int(ano[0])      # CONVERTENDO O ANO EM NUMERO
    idade= ano_1 - data_nascimento  # CALCULO PARA DESCOBRIR SUA IDADE
    # RESOLVENDO O PROBLEMA
    
    altura = float(input('INFORME SUA ALTURA: '))

    print('SUA IDADE É : {} ANOS\nSUA ALTURA É {} CM DE ALTURA'.format(idade,altura))
    
    print('\n')

    print('SITUAÇÃO DA ENTRADA DOS PARQUES....','\n')


   #CARROSSEL
    if altura > 1 and idade >=3:
        print('CARROSEL : \033[42m PERMITIDA \033[0m')
    else:
        print('CARROSEL : \033[41m NEGADA \033[0m')

    # PISCINA DE BOLINHAS 
    
    if  1 < altura < 1.3 and 4 <= idade <= 9:
        print('PISCINA DE BOLINHAS : \033[42m PERMITIDA \033[0m')
    else:
        print('PISCINA DE BOLINHAS : \033[41m NEGADA \033[0m')

    # MONTANHA-RUSSA
    
    if  altura >=1:
        print('MONTANHA-RUSSA : \033[42m PERMITIDA \033[0m')
    else:
        print('MONTANHA-RUSSA : \033[41m NEGADA \033[0m')
    

parque_diversao('ano', 'altura')