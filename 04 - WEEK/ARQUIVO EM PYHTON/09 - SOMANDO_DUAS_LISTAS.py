# 09  - Faça uma função que recebe duas listas e retorna a soma item a item dessas listas. Exemplo: 
# Se a função receber as listas [1,4,3] e [3,5,1], 
# então a função deve retornar [1+3, 4+5, 3+1] = [4, 9, 4].

def somalista(lista_1, lista_2):
    lista_3 =[]
    for i in range(len(lista_1)):
        lista_3.append(lista_1[i] + lista_2[i])
    print(lista_3)


somalista([2,2,2], [2,2,2])