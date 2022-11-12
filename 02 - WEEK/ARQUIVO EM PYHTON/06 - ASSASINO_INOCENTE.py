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
      "\n",
      "\n",
      "\u001b[42mA pessoa é cumplice!\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "#2) Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:\n",
    "\n",
    "#- \"Telefonou para a vítima?\"\n",
    "#- \"Esteve no local do crime?\"\n",
    "#- \"Mora perto da vítima?\"\n",
    "#- \"Devia para a vítima?\"\n",
    "#- \"Já trabalhou com a vítima?\"\n",
    "\n",
    "#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. \n",
    "#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como \"Suspeita\", \n",
    "#entre 3 e 4 como \"Cúmplice\" e 5 como \"Assassino\". Caso contrário, ele será classificado como \"Inocente\".\n",
    "\n",
    "respostas_positivas = 0\n",
    "\n",
    "resposta = input(\"Telefonou para a vítima? (S/N) \")\n",
    "if resposta.upper() == 'S': respostas_positivas += 1\n",
    "\n",
    "resposta = input(\"Esteve no local do crime? (S/N) \")\n",
    "if resposta.upper() == 'S': respostas_positivas += 1\n",
    "\n",
    "resposta = input(\"Mora perto da vítima? (S/N) \")\n",
    "if resposta.upper() == 'S': respostas_positivas += 1\n",
    "\n",
    "resposta = input(\"Devia para a vítima? (S/N) \")\n",
    "if resposta.upper() == 'S': respostas_positivas += 1\n",
    "\n",
    "resposta = input(\"Já trabalhou com a vítima? (S/N) \")\n",
    "if resposta.upper() == 'S': respostas_positivas += 1\n",
    "\n",
    "print('_'*60)\n",
    "print(\"\\n\")\n",
    "\n",
    "if respostas_positivas == 5:\n",
    "    print('\\033[41mA pessoa é o assassino!\\033[0m')\n",
    "elif respostas_positivas == 3 or respostas_positivas == 4:\n",
    "    print('\\033[42mA pessoa é cumplice!\\033[0m')\n",
    "elif respostas_positivas == 2:\n",
    "  print(\"\\033[46mA pessoa é suspeita!\\033[0m\")\n",
    "else:\n",
    "  print(\"\\033[42mA pessoa é inocente!\\033[0m\")\n"
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
