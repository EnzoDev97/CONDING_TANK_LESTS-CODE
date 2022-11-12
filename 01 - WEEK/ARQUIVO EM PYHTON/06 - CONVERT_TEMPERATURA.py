# 04 Crie um programa que receba a temperatura em CELSIUS e converta para FAHRENHEIT (pesquise no google a fórmula)

f = float(input('INFORME UMA TEMPERATURA EM FARENHEIT: '))
c = 5*(f - 32)/9
print(' A TEMPERATURA EM FAHRENHEIT É : {:.2f}° GRAUS  ---------------  CONVERTENDO PARA CELSIUS FICARÁ {:.2f}° GRAUS '.format(f, c))