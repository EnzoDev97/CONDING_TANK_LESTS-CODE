# 10  - Faça uma função que receba duas listas e retorne o produto item a item dessas listas. 
# Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve retornar [1x3, 4x5, 3x1] = [3, 20, 3].
def multiplicaListas(lista_1, lista_2):
    lista_3 =[]
    for i in range(len(lista_1)):
        lista_3.append(lista_1[i] * lista_2[i])
    print(lista_3)


multiplicaListas([3,3,3], [3,5,6])