#06 - Faça um programa que sorteia um número N e peça para o usuário adivinhar o número sorteado. 
#A cada resposta errada, o seu programa deve imprimir um aviso dizendo que a resposta está errada e pedir novamente uma resposta ao usuário.
#Para a realização desse exercício, utilize alguma função da biblioteca random (e.g. randint()).

import random

sorteado = random.randint(1,10)

numero = int(input('Advinhe o número inteiro escolhido entre 1 e 10: '))

while numero != sorteado:
    numero = int(input('Resposta errada! Tente novamente: '))

print('Parabéns, voce acertou! O número escolhido foi:', sorteado)