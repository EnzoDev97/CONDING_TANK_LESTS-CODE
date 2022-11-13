# 13 - Crie uma lista de 10 números e imprima:
     # a. Uma lista com 4 primeiros números;
     # b. Uma lista com os 5 últimos números; 
     # c. Uma lista contendo apenas elementos das posições pares
     # d. Uma lista contendo apenas os elementos nas posições ímpares
     # e. Uma lista inversa da lista sorteada (sort)
     # f. Uma lista inversa dos primeiros 5 números
     # g. Uma lista inversa dos últimos 5 números**





lista = [4,5,8,3,6,15,18,23,7,38]

# a.
listaA = []

for i in range(4):
    listaA.append(lista[i])

print(f'A lista com os primeiros 4 números é: {listaA}')

# b.
listaB = []

for i in range(5, 10):
    listaB.append(lista[i])

print(f'A lista com os últimos 5 números é: {listaB}')

# c. e d.
listaC = []
listaD = []

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        listaC.append(lista[i])
    else:
        listaD.append(lista[i])

print(f'A lista com elementos pares é: {listaC}')
print(f'A lista com elementos ímpares é: {listaD}')

# e.
listaE = []

for i in range(len(lista)):
    listaE.append(lista[i])
    
listaE.sort(reverse=True)

print(f'A lista sorteada é: {listaE}')

# f.
listaF = []

for i in range(5):
    listaF.append(lista[i])
    
listaF.reverse()
    
print(f'A Lista inversa dos primeiros 5 números é: {listaF}')

# g.
listaG = []
for i in range(5,10):
    listaG.append(lista[i])
    
listaG.reverse()
    
print(f'A Lista inversa dos últimos 5 números é: {listaG}')