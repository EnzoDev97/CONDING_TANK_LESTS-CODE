# 04 - Faça um programa com duas funções: uma chamada "calculaImposto". A função possui dois parâmetros formais: 
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto e irá retornar a taxa de imposto. 
# E uma função “alteraValor” que recebe o valor de custo e a taxa de imposto para incluir o imposto sobre vendas e retorna esse novo valor.

# FUNÇÃO ONDE SELECIONA A OPERAÇÃO MAT E REALIZA O CALCULO

#def calculo_imposto():
 #   taxa = float(input('INFORME O VALOR DA TAXA: '))
  #  custo = float(input('INFORME O VALOR DO CUSTO: '))
  #  imposto = ((taxa/100)*custo)

  #  print('O VALOR DO PRODUTO É R$ {:.2f} REAIS A TAXA DE IMPOSTO QUE É  DE {:.2f} % TAXA DE IMPOSTO É R$ {:.2f} REAIS\n '.format(custo, taxa, imposto))

   # calculo = imposto + custo

   # print('O VALOR DO PRODUTO COM O IMPOSTO FICA R$ {:.2f} REAIS  '.format(calculo))

    


def altera_valor():
    custo =  float(input('INFORME O VALOR DO CUSTO: '))
    return custo

def calculo_imposto():
    taxa = float(input('INFORME O VALOR DA TAXA: '))
    custo = altera_valor()
    imposto = ((taxa/100)*custo)
    calculo = imposto + custo
    print('O VALOR DO PRODUTO É R$ {:.2f} REAIS A TAXA DE IMPOSTO É DE {:.2f} % TAXA DE IMPOSTO É R$ {:.2f} REAIS\n '.format(custo, taxa, imposto))
    print('O VALOR DO PRODUTO COM O IMPOSTO FICA R$ {:.2f} REAIS  '.format(calculo))

calculo_imposto()