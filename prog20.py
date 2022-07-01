#! /usr/bin/env python
# -*- coding: utf-8 -*-

print("...:: Aviario S.T ::...")
galinheiro_G1 = [3.200, 2.980, 3.100 , 2.800, 3.450,
3.210, 2.970, 3.050]

soma = 0.0
for massa in galinheiro_G1:
    soma += massa
media = soma / len(galinheiro_G1)

maior = galinheiro_G1[0]
for massa in galinheiro_G1:
    if massa > maior:
        maior = massa

menor = galinheiro_G1[0]
for massa in galinheiro_G1:
    if massa < menor:
        menor = massa

print("\nMédia:  {0:.3f} kg".format(media))
print("Máxima: {0:.3f} kg".format(maior))
print("Mínima: {0:.3f} kg".format(menor))
