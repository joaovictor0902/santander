
#Organização do código em módulos
#À medida que nossos programas crescem em tamanho e complexidade, é uma boa prática organizar nosso código em módulos separados segundo sua funcionalidade. Isso nos permite manter um código mais legível, agrupado em módulos e fácil de manter.

#Por exemplo, podemos ter um módulo operacoes.py que contenha funções relacionadas com operações matemáticas, e outro módulo utilidades.py que contenha funções de uso geral.

#operacoes.py
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b