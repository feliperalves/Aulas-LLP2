#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Estrutura de controle condicional composta múltipla'''
'''
Exemplo:

x = int(input("Idade:"))
a = x + 3
if a > 5:
    print("maior")
elif a < 21:
    print("menor")
elif a % 2 == 0:
    print("divisivel")
'''

print(".::Indice de Massa Corporea ::.\n")

massa = float(input("Digite a massa (kg): "))
altura = float(input("Digite a altura (m): "))

imc = massa / altura**2

print ("IMC = {0:7.2f}".format(imc))

if imc < 18.5:
    print("\nAbaixo do peso normal :-(")
elif imc < 25:
    print("Peso normal :-)")
elif imc < 30:
    print("Excesso de peso :-(")
elif imc < 35:
    print("Obesidade de grau 1")
elif imc < 35:
    print("Obesidade de grau 1")
elif imc < 40:
    print("Obesidade de grau 2")
else:
    print("Obesidade de grau 3")

print("\nBye :-)")
