#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Curso: Linguagem Python
#Felipe da Rocha Alves

print(".::Indice de Massa Corporea ::.\n")

entrada = input("Digite a massa (kg): ")
massa = float(entrada)

entrada = input("Digite a altura (m): ")
altura = float(entrada)

imc = massa / altura**2

saida = "IMC = {0:7.2f}" 
print(saida.format(imc))
