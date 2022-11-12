# 13 - ORGANIZANDO NÚMEROS EM FORMATO DE DATA 
dia = input('QUAL É O DIA ? ')
mes = input('QUAL É O MÊS: ')
ano = input('QUAL O ANO')

print('A DATA É : {}/{}/{}'.format(dia,mes,ano))

# OUTRO MÉTODO 

from datetime import datetime # Incluímos a biblioteca datetime
agora = datetime.now() # Chamamos a função now() da biblioteca datetime

# Separamos cada pedaço que precisamos
ano = agora.year
mes = agora.month
dia = agora.day
hora = agora.hour
minuto = agora.minute
segundo = agora.second

# Imprimimos o resultado 
# (Obs: o sep="" quer dizer que o print não vai inserir um espaço entre cada uma das saídas)
print(dia, "/", mes, "/", ano, " ", hora, ":", minuto, ":", segundo, sep="")

# Outra forma
agora = datetime.now()
formato = "%d/%m/%Y %H:%M:%S" # Definimos um formato 
agora_formatado = datetime.strftime(agora,formato) # Usamos a função strftime(), que formata automaticamente o texto
print(agora_formatado)