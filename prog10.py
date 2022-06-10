#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Curso: Linguagem Python
#Felipe da Rocha Alves

# 18.5 Abaixo do peso normal
# 18.5 - 25 Peso normal
# 25 - 30 Excesso de peso
# 30 - 35 Obesidade de grau 1
# 35 - 40 Obesidade de grau 1
#   40    Obesidade de grau 1

print(".::Indice de Massa Corporea ::.\n")

massa = float(input("Digite a massa (kg): "))
altura = float(input("Digite a altura (m): "))

imc = massa / altura**2

print ("IMC = {0:7.2f}".format(imc))

if imc < 18.5:
	print("\nAbaixo do peso normal :-(")
else:
	if imc < 25:
		print("Peso normal :-)")
	else:
		if imc < 30:
			print("Excesso de peso :-(")
		else:
			if imc < 35:
				print("Obesidade de grau 1")
			else:
				if imc < 40:
					print("Obesidade de grau 2")
				else:
					print("Obesidade de grau 3")
print("\nBye :-)")
