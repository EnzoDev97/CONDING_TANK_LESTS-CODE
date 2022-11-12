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
      "VOCÊ RECEBE R$ 2000.00 REAIS POR MÊS\n"
     ]
    }
   ],
   "source": [
    "# 04 - CALCULANDO SEU SÁLARIO A PARTIR DAS HORAS TRABALHADAS\n",
    "\n",
    "s_diario = float(input('QUANTO VOCÊ GANHA POR HORA: '))\n",
    "horas = float(input('QUANTAS HORAS VOCÊ TRABALHA POR MÊS? '))\n",
    "\n",
    "salario = s_diario * horas\n",
    "print('VOCÊ RECEBE R$ {:.2f} REAIS POR MÊS'.format(salario))"
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
