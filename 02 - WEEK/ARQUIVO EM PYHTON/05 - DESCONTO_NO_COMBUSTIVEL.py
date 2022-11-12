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
      "____________________________________________________________\n",
      "================================================================================================\n",
      "|\u001b[46m CLIENTE  \u001b[0m|\u001b[41mTIPO DE COMBUSTÍVEL\u001b[0m|\u001b[42m  QTD LITROS   \u001b[0m|\u001b[43m  PREÇO TOTAL  \u001b[0m|\u001b[44m   DESCONTO    \u001b[0m|\u001b[45m VALOR Á PAGAR \u001b[0m|\n",
      "================================================================================================\n",
      "|   ENZO   |     GASOLINA      |      50       | R$   125.0    | R$    7.5     | R$   117.5    |\n"
     ]
    }
   ],
   "source": [
    "nome = input('INFORME SEU NOME: ')\n",
    "combustivel = input('INFORME O TIPO DE COMBUSTÍVEL (A/G): ')\n",
    "litros = int(input('INFORME QUANTOS LITROS VOCÊ QUER: '))\n",
    "preco_gasolina = 2.50\n",
    "preco_alcool = 1.90\n",
    "valor_gasolina = litros * preco_gasolina\n",
    "valor_alcool = litros * preco_alcool\n",
    "print('_'*60)\n",
    "\n",
    "print('='*96)\n",
    "print('|\\033[46m{:^10}\\033[0m|\\033[41m{:^15}\\033[0m|\\033[42m{:^15}\\033[0m|\\033[43m{:^15}\\033[0m|\\033[44m{:^15}\\033[0m|\\033[45m{:^15}\\033[0m|'.format('CLIENTE','TIPO DE COMBUSTÍVEL','QTD LITROS','PREÇO TOTAL','DESCONTO','VALOR Á PAGAR'))\n",
    "print('='*96)\n",
    "\n",
    "if nome and combustivel and litros:\n",
    "    if combustivel.upper() == 'G' and litros < 20:\n",
    "        desconto = valor_gasolina * 0.04\n",
    "        valor_pago  = valor_gasolina - desconto\n",
    "        print('|{:^10}|{:^19}|{:^15}| R${:^12}| R${:^12}| R${:^12}|'.format(nome, 'GASOLINA', litros, valor_gasolina,desconto,valor_pago))\n",
    "    elif combustivel.upper() == 'G' and litros >= 20:\n",
    "        desconto = valor_gasolina * 0.06\n",
    "        valor_pago  = valor_gasolina - desconto\n",
    "        print('|{:^10}|{:^19}|{:^15}| R${:^12}| R${:^12}| R${:^12}|'.format(nome, 'GASOLINA', litros, valor_gasolina,desconto,valor_pago))\n",
    "    elif combustivel.upper() == 'A' and litros < 20:\n",
    "        desconto = valor_alcool * 0.03\n",
    "        valor_pago  = valor_alcool  - desconto\n",
    "        print('|{:^10}|{:^19}|{:^15}| R${:^12}| R${:^12}| R${:^12'.format(nome, 'ALCOOL', litros, valor_alcool,desconto,valor_pago))\n",
    "    elif combustivel.upper() == 'A' and litros >= 20:\n",
    "        desconto = valor_alcool * 0.05\n",
    "        valor_pago  = valor_alcool - desconto\n",
    "        print('|{:^10}|{:^19}|{:^15}| R${:^12}| R${:^12}| R${:^12}|'.format(nome, 'ALCOOL', litros, valor_alcool,desconto,valor_pago))\n",
    "    else:\n",
    "        print('DIGITE AS INFORMAÇÕES CORRETAMENTE')\n",
    "else:\n",
    "    print('PREENCHA TODOS OS CAMPOS')"
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
