# 11 - Faça um programa que peça um valor monetário e aumente-o em 15%. Seu programa deve imprimir a mensagem “O novo valor é [valor]”.

valor_monetario = float(input('DIGITE O VALOR MONETÁRIO: ')) 
print('-'*60) 
print('\n')

juros = valor_monetario * 0.15 
valor_novo = valor_monetario + juros

print('O com aumento é R$ {:.2f} reais'.format(valor_novo))

# Faça um programa que peça um valor monetário e diminua-o em 15%

valor = float(input("Qual o valor? "))
print("O valor diminuido é R$",valor*0.85, 'reais')