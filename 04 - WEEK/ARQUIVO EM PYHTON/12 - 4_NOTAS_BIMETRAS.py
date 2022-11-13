#12 - Faça um programa que peça as 4 notas bimestrais e mostre a média aritimética delas, usando listas

notas = []
media = 0
for i in range(4):
    notas.append(float(input(f'Digite a Nota Bimestral {i+1}: ')))
    media += notas[i]

print('A média das notas do usuário é {:.2f}'.format(media/len(notas)))