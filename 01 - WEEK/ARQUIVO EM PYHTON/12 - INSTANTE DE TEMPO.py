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
      "A posição no instante t = 50.0 é -11900.0\n"
     ]
    }
   ],
   "source": [
    "#Desafio 1 - Peça para o usuário digitar uma velocidade inicial (em m/s), uma posição inicial (em m) e um instante de tempo (em s) e imprima a posição de um projétil nesse instante de tempo.\n",
    "\n",
    "#Use a fórmula matemática:\n",
    "\n",
    "#y(t) = y(0) + v(0)*t + (g*(t**2)/2)\n",
    "\n",
    "#Onde, g é a aceleração da gravidade (-10m/s²), y(t) é a posição final, y(0) é a posição inicial, v(0) é a velocidade inicial e t é o instante de tempo.\n",
    "\n",
    "y0 = float(input(\"Digite a posição inicial: \"))\n",
    "v0 = float(input(\"Digite a velocidade inicial: \"))\n",
    "t = float(input(\"Digite um instante no tempo: \"))\n",
    "g = -10\n",
    "\n",
    "y = y0 + v0*t + 0.5*g*t**2\n",
    "\n",
    "print(\"A posição no instante t =\", t, \"é\", y)"
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
