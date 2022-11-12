# 11 - FORMATAÇÃO DE DATAS E HORARIO


import datetime

#TODOS OS DADOS DO DIA 
data = datetime.datetime.now()
print(data)

print('-'*100)

Y = datetime.datetime.now()
H = datetime.datetime.now()

print(Y.year)    # ANO 
print(Y.strftime("%A"))   # DIA DA SEMANA  VERSÃO COMPLETA
print(Y.strftime("%a"))  # VERSAO CURTA
print(Y.strftime("%w"))  # VERSAO EM  NÚMERO

print('-'*100)

print('FORMATO DE MESES')
print(Y.strftime("%d"))  # DIA DO MES 
print(Y.strftime("%b"))   # MES EM FORMATO ABREVIADO
print(Y.strftime("%B"))   # MES EM FORMATO COMPLETO
print(Y.strftime("%m"))   # MES EM FORMATO DE NUMERO


print('-'*100)

print('FORMATO DO ANO')
print(Y.strftime("%Y"))  # FORMATO DE ANO COMPLETO
print(Y.strftime("%y")) # FORMATO DE ANO ABREVIADO
print(Y.strftime("%j"),'DIA DO ANO') # FORMATO DO DIA DO ANO
print(Y.strftime("%U"),'DIA DA SEMANA')
print(Y.strftime("%W"))
print(Y.strftime("%C"),'SÉCULO')  # FORMATO DO SÉCULO
print(Y.strftime("%G"))
print(Y.strftime("%u"))
print(Y.strftime("%V"))

print('-'*100)

print('FORMATO DO HORA')

print(H.strftime('%H'),'HORAS')  # FORMATO DE HORA VERSÃO BR
print(H.strftime('%I'),'HORAS - EUA') # FORMATO DE HORA VERSÃO EUA
print(H.strftime('%p'),'TURNO') # FORMATO DO TURNO EUA
print(H.strftime('%M'),'MINUTOS') # FORMATO DE MINUTOS
print(H.strftime('%S'),'SEGUNDOS') # FORMATO DE SEGUNDOS
print(H.strftime('%f'),'MILISEGUNDOS') # FORMATO DE MICROSEGUNDOS
print(H.strftime('%z'),'FUSO HORARIO') # FORMATO DE FUSO HORARIO
print(H.strftime('%Z'),'FUSO HORARIO') # FORMATO DE FUSO HORARIO

print('-'*100)

print('FORMATO DAS DATAS')
print(Y.strftime('%x'),'DATA') # FORMATO DE DATA
print(Y.strftime('%X'),'HORARIO') # FORMATO DO HORARIO
