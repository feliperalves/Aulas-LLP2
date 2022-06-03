#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Curso: Linguagem Python
#Felipe da Rocha Alves

nome = input("Digite seu nome: ")
nome = nome.title()
nome = nome.replace("Da", "da")
nome = nome.replace("De", "de")

frase = "Oi {fulano}. Tudo bem?"
print(frase.format(fulano=nome))

print("Comigo tudo bem!")
print("Vamos brincar?")
print("Vamos correr?")
print(";-D")
