#! /usr/bin/env python
# -*- coding: utf-8 -*-

print("...:: Número de vogais  ::...\n")

frase = input ("Digite uma frase: ")
frase = frase.lower()

num_vogais = 0
for letra in frase:
    if letra in "aeiou":
        num_vogais += 1

print("A frase tem {n} vogais.". format(n=num_vogais))
