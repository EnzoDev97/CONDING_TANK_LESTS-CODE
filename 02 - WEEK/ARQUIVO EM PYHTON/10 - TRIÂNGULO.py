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
      "________________________________________\n",
      "\n",
      "\n",
      "Os lados formam um triângulo equilátero\n"
     ]
    }
   ],
   "source": [
    "#6) Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.\n",
    "\n",
    "#Dicas:\n",
    "\n",
    "#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;\n",
    "#Triângulo Equilátero: três lados iguais;\n",
    "#Triângulo Isósceles: quaisquer dois lados iguais;\n",
    "#Triângulo Escaleno: três lados diferentes;\n",
    "\n",
    "ladoA = float(input(\"Digite o tamanho do lado A: \"))\n",
    "ladoB = float(input(\"Digite o tamanho do lado B: \"))\n",
    "ladoC = float(input(\"Digite o tamanho do lado C: \"))\n",
    "print('_' *40)\n",
    "print('\\n')\n",
    "\n",
    "if not(ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA):\n",
    "  print(\"Os lados informados não formam um triangulo.\")\n",
    "else:\n",
    "  if ladoA == ladoB == ladoC:\n",
    "    print(\"Os lados formam um triângulo equilátero\")\n",
    "  elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:\n",
    "    print(\"Os lados formam um triângulo isósceles\")\n",
    "  else:\n",
    "    print(\"Os lados formam um triângulo escaleno\")\n"
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
