
#Depois, podemos importar e utilizar as funções definidas em meu_modulo.py em outro arquivo Python.

import Python.meu_modulo.meu_modulo as meu_modulo
meu_modulo.saudar("Joao")
resultado = meu_modulo.caucular(5, 3)
print(f"A soma =: {resultado}")

#Neste exemplo, importa-se o módulo meu_modulo e utilizam-se as funções saudar() e calcular_soma() definidas nele.
# O resultado será:
# Ola, Joao!
# A soma =: 8