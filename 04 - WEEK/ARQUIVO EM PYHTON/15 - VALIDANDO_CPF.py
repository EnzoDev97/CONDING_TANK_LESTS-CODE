#15 - Super Desafio! Faça um programa para o usuário digitar o CPF e verifica se ele é valido.
# Para isso, primeiramente deve multiplicar cada um dos 9 primeiros números do CPF pelos números de 10 a 2 e somar suas respostas.
# O resultado deve ser multiuplicado por 10 e dividido por 11. 
# O resto dessa divisão deve ser igual ao primeiro dígito do verificador (10º digito).
# Em seguida, o programa deve multiplicar cada um dos 10 primeiros dígitos do CPF pelos números de 11 a 2 e repetir o procedimento anterior

# AGORA IREI RETIRAR OS ESPAÇOS , PONTOS E TRAÇOS DO CPF
cpf = input('Digite Seu Cpf ')
#cpf = cpf.strip()


# ELE VAI RETIRAR OS PONTOS E TRAÇOS [ (O PRIMEIRO É O CARETERE QUE QUERO TIRAR) , (O SEGUNDO É O QUE EU QUERO SUBSTITUIR) ]
cpf= cpf.replace('.','')

cpf.replace('-','')

# Regra que faz a pessoa botar apenas a informação que quero ( neste caso apenas numero e apenas 11 caracteres)
if len(cpf) == 11 and cpf.isnumeric():
    print('O CPF É : {}'.format(cpf))
else:
    print('CPF ESTÁ INCORRETO POIS CONTEM CARACTERES NÃO PERMITIDOS {}'.format(cpf))



#VERIFICANDO SE O CPF É REAL E VALIDO

try:
    #cpf =input()
        
    cpf = cpf.replace('.','').replace('-','' )
    #cpf = cpf.replace('-','' )

    cpf_valido = True

    erro = ''

    if not len(cpf) == 11:
        cpf_valido = False
        erro += 'O cpf não tem 11 caracteres \n'

    digito = 0


    digito = digito + int(cpf[0]) * 10
    digito +=  int(cpf[1]) * 9
    digito +=  int(cpf[2]) * 8
    digito +=  int(cpf[3]) * 7
    digito +=  int(cpf[4]) * 6
    digito +=  int(cpf[5]) * 5
    digito +=  int(cpf[6]) * 4
    digito +=  int(cpf[7]) * 3
    digito +=  int(cpf[8]) * 2

    # calculando o resto da operacao
    digito = (digito * 10) % 11

    # Observação Importante: Se o resto da divisão for igual a 10, nós o consideramos como 0.
    if digito == 10:
        digito = 0
    print('='*100)
    if str(digito) == cpf[-2]:
        print('Primeiro digito bateu')
    else:
        cpf_valido = False
        erro += "O primeiro digito verificador não bateu \n"
    

    print(digito)

    ## segundo digito verificador

    digito = 0
    # shift + alt + seta para baixo = copia a linha atual e cola

    digito = digito + int(cpf[0]) * 11
    digito +=  int(cpf[1]) * 10
    digito +=  int(cpf[2]) * 9
    digito +=  int(cpf[3]) * 8
    digito +=  int(cpf[4]) * 7
    digito +=  int(cpf[5]) * 6
    digito +=  int(cpf[6]) * 5
    digito +=  int(cpf[7]) * 4
    digito +=  int(cpf[8]) * 3
    digito +=  int(cpf[9]) * 2

    # calculando o resto da operacao
    digito = (digito * 10) % 11

    # Observação Importante: Se o resto da divisão for igual a 10, nós o consideramos como 0.
    if digito == 10:
        digito = 0

    

    if str(digito) == cpf[-1]:
        print('Segundo digito bateu')
    else:
        cpf_valido = False
        erro += "O segundo digito verificador não bateu \n"

    print(digito)
    print('='*100)


    print(f'O cpf é {cpf_valido}')
    print(erro)
except Exception as err:
    print(f'Deu um erro no validador: {err}')
    cpf_valido = False