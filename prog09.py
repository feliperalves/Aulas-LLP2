#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Curso: Linguagem Python
#Felipe da Rocha Alves

print(".::Indice de Massa Corporea ::.\n")

massa = float(input("Digite a massa (kg): "))
altura = float(input("Digite a altura (m): "))

imc = massa / altura**2

print ("IMC = {0:7.2f}".format(imc))
