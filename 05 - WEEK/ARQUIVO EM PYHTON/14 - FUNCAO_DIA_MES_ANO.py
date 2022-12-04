{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Trinta de novembro de 1997\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'30/11/1997'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "\n",
    "\n",
    "def data_conversao (data):\n",
    "    meses = [\n",
    "\"janeiro\",\n",
    "\"fevereiro\",\n",
    "\"março\",\n",
    "\"abril\",\n",
    "\"maio\",\n",
    "\"junho\",\n",
    "\"julho\",\n",
    "\"agosto\",\n",
    "\"setembro\",\n",
    "\"outubro\",\n",
    "\"novembro\",\n",
    "\"dezembro\"]\n",
    "    \n",
    "    dia = [\n",
    "\"Um\", \n",
    "\"Dois\", \n",
    "\"Três\", \n",
    "\"Quatro\", \n",
    "\"Cinco\", \n",
    "\"Seis\", \n",
    "\"Sete\", \n",
    "\"Oito\", \n",
    "\"Nove\", \n",
    "\"Dez\", \n",
    "\"Onze\", \n",
    "\"Doze\", \n",
    "\"Treze\", \n",
    "\"Catorzer\", \n",
    "\"Quinze\", \n",
    "\"Dezesseis\", \n",
    "\"Dezessete\", \n",
    "\"Dezoito\", \n",
    "\"Dezenove\", \n",
    "\"Vinte\", \n",
    "\"Vinte e Um\", \n",
    "\"Vinte e Dois\", \n",
    "\"Vinte e Três\", \n",
    "\"Vinte e Quatro\", \n",
    "\"Vinte e Cinco\", \n",
    "\"Vinte e Seis\", \n",
    "\"Vinte e Sete\", \n",
    "\"Vinte e Oito\", \n",
    "\"Vinte e Nove\", \n",
    "\"Trinta\", \n",
    "\"Trinta e Um\"]\n",
    "    \n",
    "    #data = input(\"informe a data (dd/mm/aaaa): \")\n",
    "    print(dia[(int(data.split(\"/\")[0])-1)],\n",
    "       \"de\",\n",
    "       meses[(int(data.split(\"/\")[1])-1)],\n",
    "       \"de\",\n",
    "       data.split(\"/\")[2])\n",
    "    return data\n",
    "    \n",
    "data_conversao (data = input(\"informe a data (dd/mm/aaaa): \"))"
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
