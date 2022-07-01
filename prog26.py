#! /usr/bin/env python
# -*- coding: utf-8 -*-
print(".:: Dicionario ::.")

dic = {"amarela":234, "verde":7,
        "azul":145, "vermelha":87}

for ch, valor in dic.items():
    print("Chave: {0:10s} Valor: {1:3d}".format(ch,valor))

print("Ufa!!!")
