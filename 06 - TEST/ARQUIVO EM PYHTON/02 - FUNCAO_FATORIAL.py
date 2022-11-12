# 2 - Peça ao usuário para entrar com um número e faça uma função que retorne o fatorial dele como resposta. 
#O fatorial de um número é o resultado da multiplicação de todos os números que o antecedem a partir de 1 até o número fornecido.


def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n # fat = fat * n
        n -= 1 # n = n - 1
    return fat

# OU

def f(n):
    fat = 1
    for num in range(n):
        fat = fat * (num+1)
    return fat



# OU

def fat(numero):

    i = 1
    fatorial = 1
    while i < numero:
        i += 1
        fatorial *= i
    else:
        fatorial *= 1
        
    print('O fatorial de {} é {}'.format(numero,fatorial))
