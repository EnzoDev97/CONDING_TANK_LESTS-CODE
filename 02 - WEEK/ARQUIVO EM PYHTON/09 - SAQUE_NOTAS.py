{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "----------------------------------------------------------------------------------------------------\n",
      "\n",
      "\n",
      "********** SEJA MUITO BEM VINDO AO CAIXA ELETRÔNICO **********\n",
      "_______________________________________________________________\n",
      "\n",
      "\n",
      "                         \u001b[46mLOGANDO...\u001b[0m                         \n",
      "\n",
      "\n",
      "É BOM RE RECEBER NOVAMENTE ENZO\n",
      "O VALOR QUE DESEJA SACAR  HOJE É ----> R$ 985.00 REAIS\n",
      "\n",
      "\n",
      "================================================\n",
      "\u001b[42mO caixa eletronico liberará as seguintes notas:\u001b[0m\n",
      "================================================\n",
      "\n",
      "\n",
      "9.00 NOTAS DE R$ 100 reais\n",
      "------------------------------\n",
      "19.00 NOTAS DE R$ 50 reais\n",
      "------------------------------\n",
      "8.00 NOTAS DE R$ 10 reais\n",
      "------------------------------\n",
      "2.00 NOTAS DE R$ 5 reais\n",
      "------------------------------\n",
      "985.00 NOTAS DE R$ 1 reais\n",
      "------------------------------\n"
     ]
    }
   ],
   "source": [
    "#5) Faça um Programa para um caixa eletrônico.\n",
    "#O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas,\n",
    "#considerando o valor mínimo de notas possíveis.\n",
    "#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.\n",
    "\n",
    "nome = input('QUAL É O SEU NOME : ')\n",
    "saque = float(input('INFORME O VALOR QUE DESEJA SACAR: '))\n",
    "print('-'*100)\n",
    "print('\\n')\n",
    "\n",
    "\n",
    "print ('*'*10, 'SEJA MUITO BEM VINDO AO CAIXA ELETRÔNICO','*'*10)\n",
    "print('_'*63)\n",
    "print('\\n')\n",
    "\n",
    "print(' '*24,'\\033[46mLOGANDO...\\033[0m',' '*24 )\n",
    "print('\\n')\n",
    "\n",
    "print ('É BOM TE RECEBER NOVAMENTE {}'.format(nome))\n",
    "print('O VALOR QUE DESEJA SACAR  HOJE É ----> R$ {:.2f} REAIS'.format(saque))\n",
    "print('\\n')\n",
    "\n",
    "nota_de_1 = saque\n",
    "nota_de_5 = saque // 5 % 5\n",
    "nota_de_10 = saque // 10 % 10\n",
    "nota_de_50 = saque // 50 % 50\n",
    "nota_de_100 = saque // 100 % 100\n",
    "\n",
    "print('='*48)\n",
    "print('\\033[42mO caixa eletronico liberará as seguintes notas:\\033[0m')\n",
    "print('='*48)\n",
    "print('\\n')\n",
    "\n",
    "print('{:.2f} NOTAS DE R$ 100 reais'.format(nota_de_100))\n",
    "print('-'*30)\n",
    "print('{:.2f} NOTAS DE R$ 50 reais'.format(nota_de_50))\n",
    "print('-'*30)\n",
    "print('{:.2f} NOTAS DE R$ 10 reais'.format(nota_de_10))\n",
    "print('-'*30)\n",
    "print('{:.2f} NOTAS DE R$ 5 reais'.format(nota_de_5))\n",
    "print('-'*30)\n",
    "print('{:.2f} NOTAS DE R$ 1 reais'.format(nota_de_1))\n",
    "print('-'*30)"
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
   "name": "python",
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
