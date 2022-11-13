# 07 - Faça um programa que peça para o usuário digitar a idade, o salário e o sexo de uma pessoa até que as entradas digitadas sejam válidas.

#a. Idade: entre 0 e 150;

#b. Salário: maior que 0;

#c. Sexo: M, F ou Outro.




age = int(input('INFORME SUA IDADE: '))
while not(0<=age<=150): 
    print('Entrada de idade inválida. Por favor, digite um idade entre 0 e 150 anos.') 
    age = int(input('Digite a sua idade mais uma vez: '))

print('_'*100) 
print('\n')

salary = int(input('DIGITE SEU SALÁRIO: ')) 
while salary<=0: 
    print(f'Entrada de salário inválida. Por favor, digite valor maior que 0.') 
    salary = int(input('Digite o seu salário mais uma vez: '))

print('_'*100) 
print('\n')

sex = input('QUAL É O SEU GÊNERO ? (F/M/Outro) ') 
while sex not in ['M', 'F', 'Outro']:
    print(f'Entrada de sexo inválida. Por favor, digite valor maior que 0.')
    sex = input('Informe o seu sexo (F/M/Outro) mais uma vez: ')