#Faça um programa para imprimir:

  #  1
  #  1   2
  #  1   2   3
  #  .....
  #  1   2   3   ...  n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def sequencia(n):
    for linha in range(1, n +1):     # aqui criamos a linha da sequencia 1 depois 1+1 depois 2+1 
        for coluna in range(1, linha + 1): # aqui criamos a coluna 
            print(coluna, end =  ' ')
        print('')

sequencia(int(input()))