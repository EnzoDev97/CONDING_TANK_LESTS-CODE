{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--------------------------------------------------\n",
      "\n",
      "\n",
      "========================================\n",
      "|  IDADE   |    SALÁRIO    |   GÊNERO   |\n",
      "========================================\n",
      "|    20    |R$  200000.0   |     M      |\n"
     ]
    }
   ],
   "source": [
    "idade = int(input('INFORME SUA IDADE: ')) \n",
    "salario = float(input('INFORME SEU SALÁRIO: ')) \n",
    "sexo = input('INFORME SEU GÊNERO: (F/M/O): ') \n",
    "print('-'*50) \n",
    "print('\\n')\n",
    "\n",
    "print('='*40) \n",
    "print('|{:^10}|{:^15}|{:^12}|'.format('IDADE', 'SALÁRIO','GÊNERO')) \n",
    "print('='*40)\n",
    "\n",
    "if idade and salario and sexo: \n",
    "    if idade < 0 and idade > 150: \n",
    "        print('A IDADE INSERIDA É INVÁLIDA') \n",
    "    if salario <0: \n",
    "        print('O SALÁRIO INFORMADO É INVÁLIDO') \n",
    "    if sexo !='F' and sexo !='M' and sexo != 'O': \n",
    "        print('O GÊNERO INFORMADO É INVÁLIDA') \n",
    "    else: \n",
    "        print('|{:^10}|R${:^13}|{:^12}|'.format(idade,salario,sexo)) \n",
    "else: \n",
    "    print('UM DOS CAMPOS NÃO FOI PREENCHIDO')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.12 ('base')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "e8755eff31258cf3f68aa399e6f759d79082959dfad6f58a9830d0e0b06355a5"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
