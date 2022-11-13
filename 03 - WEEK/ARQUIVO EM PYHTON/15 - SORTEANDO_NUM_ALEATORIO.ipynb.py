import random as rd

unkown_number = rd.randint(1,1000)

guess_number = int(input('Chute um número entre 1 e 1000: '))
count = 1
while guess_number != unkown_number:
    hint = 'baixo' if unkown_number < guess_number else 'alto'
    guess_number = int(input('|\033[41mRESPOSTA ERRADA\033[0m|----> Digite um valor mais '+hint+': '))
    count += 1

print('|\033[42mRESPOSTA CORRETA\033[0m| - Você acertou o número {}! ----> Foram necessárias {} tentativa(s).'.format(unkown_number,count))