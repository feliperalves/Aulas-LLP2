#! /usr/bin/env python
# -*- coding: utf-8 -*-

print(".:: No bar :-) ::.")

resposta = "sim"

while resposta in "sim":
        resposta = input("Mais uma cerveja? [sim/nao]: ")
        resposta = resposta.lower()
        if resposta in "sim":
            print("Bebendooo..")

print("Casaaaaa")

