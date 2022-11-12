# 01 - Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.



def inverso (n):
    inverte=str(n)   # CONVERTENDO NÚMERO EM STRING 
    print('_'*50,'\n')
    print('O  NÚMERO INVETIDO FICA ------> ', inverte[::-1]) #  FORMATO DE INVERSO DE UMA STRING


inverso(int(input()))