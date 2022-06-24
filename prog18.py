#! /usr/bin/env python
# -*- coding: utf-8 -*-

print(".:: No bar :-) ::.")

resposta = "sim"

while True:
        resposta = input("Mais uma cerveja? [sim/nao]: ")
        resposta = resposta.lower()
        if resposta in ["sim", "mais" , "mais uma", "beleza", "ok"]:
            print("Bebendooo..")
        else:
            break

print("Casaaaaa")

