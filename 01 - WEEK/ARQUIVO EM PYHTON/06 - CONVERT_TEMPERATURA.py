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
      " A TEMPERATURA EM FAHRENHEIT É : 100.00° GRAUS  ---------------  CONVERTENDO PARA CELSIUS FICARÁ 37.78° GRAUS \n"
     ]
    }
   ],
   "source": [
    "# 04 Crie um programa que receba a temperatura em CELSIUS e converta para FAHRENHEIT (pesquise no google a fórmula)\n",
    "\n",
    "f = float(input('INFORME UMA TEMPERATURA EM FARENHEIT: '))\n",
    "c = 5*(f - 32)/9\n",
    "print(' A TEMPERATURA EM FAHRENHEIT É : {:.2f}° GRAUS  ---------------  CONVERTENDO PARA CELSIUS FICARÁ {:.2f}° GRAUS '.format(f, c))"
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
    "hash": "84119b4a23c727451d2f5b202898a53a27583c1b582daf411d2362849740e029"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
