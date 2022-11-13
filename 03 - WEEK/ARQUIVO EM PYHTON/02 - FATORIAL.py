#02 - Peça ao usuário para digitar um número e imprima o fatorial de n.

numero = int(input('Digite um número: '))
fatorial = 1
contador = 1

while contador <= numero:
    fatorial = fatorial*contador # multiplicação o fatorial pelo contador atual
    contador = contador+1

print('O fatorial é: ', fatorial)