def data_conversao (data):
    meses = [
"janeiro",
"fevereiro",
"março",
"abril",
"maio",
"junho",
"julho",
"agosto",
"setembro",
"outubro",
"novembro",
"dezembro"]
    
    dia = [
"Um", 
"Dois", 
"Três", 
"Quatro", 
"Cinco", 
"Seis", 
"Sete", 
"Oito", 
"Nove", 
"Dez", 
"Onze", 
"Doze", 
"Treze", 
"Catorzer", 
"Quinze", 
"Dezesseis", 
"Dezessete", 
"Dezoito", 
"Dezenove", 
"Vinte", 
"Vinte e Um", 
"Vinte e Dois", 
"Vinte e Três", 
"Vinte e Quatro", 
"Vinte e Cinco", 
"Vinte e Seis", 
"Vinte e Sete", 
"Vinte e Oito", 
"Vinte e Nove", 
"Trinta", 
"Trinta e Um"]
    
    #data = input("informe a data (dd/mm/aaaa): ")
    print(dia[(int(data.split("/")[0])-1)],
       "de",
       meses[(int(data.split("/")[1])-1)],
       "de",
       data.split("/")[2])
    return data
    
data_conversao (data = input("informe a data (dd/mm/aaaa): "))