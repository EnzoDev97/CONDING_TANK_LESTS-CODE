# 16 - Faça um programa que peça os 3 coeficientes (inteiros) de uma equação do segundo grau e imprima as duas soluções.
#Obs: Só pode aparecer número inteiro na resposta final

a = int(input('Digite o coeficiente A '))
b = int(input('Digite o coeficiente B '))
c = int(input('Digite o coeficiente C '))

delta = b**2 - (4*a*c)
x1 = (-b +delta ** 0.5) / (2 * a)
x2 = (-b -delta ** 0.5) / (2 * a)

# if delta ** 0.5 - int(delta**0.5) != 0 --> radicando = delta? Quem vai ser meu x1


if delta > 0:
    print('Há duas raizes, X1 = {:.2f} e X2 = {:.2f}'.format(x1,x2))
elif delta == 0:
    print('As duas raizes são iguais, sendo o valor = {:.2f}'.format(x1))
else: 
    print('Não existem raizes')