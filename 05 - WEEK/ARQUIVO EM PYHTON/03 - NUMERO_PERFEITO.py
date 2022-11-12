# 03 - Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito quando ele é igual a soma dos seus divisores excetuando ele próprio. 
#(Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar um valor booleano.

def main():
    print("Determina se um número n é perfeito\n")

    # leia o valor de n
    n = int(input("Digite o valor de n: "))

    soma = 0
  
    for divisor in range(1,n):
        if n % divisor == 0:
            soma += divisor # soma = soma + divisor

    if n == soma:
        print("O numero %d é perfeito" %(n))
    else: 
        print("O numero %d nao é perfeito\n" %(n))
  
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

main()