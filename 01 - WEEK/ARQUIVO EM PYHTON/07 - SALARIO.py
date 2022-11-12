# 04 - CALCULANDO SEU SÁLARIO A PARTIR DAS HORAS TRABALHADAS

s_diario = float(input('QUANTO VOCÊ GANHA POR HORA: '))
horas = float(input('QUANTAS HORAS VOCÊ TRABALHA POR MÊS? '))

salario = s_diario * horas
print('VOCÊ RECEBE R$ {:.2f} REAIS POR MÊS'.format(salario))