#Em Python, um módulo é um arquivo que contém definições de funções, classes e variáveis que podem ser utilizadas em outros programas. A importação de módulos nos permite acessar a funcionalidade definida em outros arquivos e reutilizar código de maneira eficiente. Além disso, podemos criar nossos próprios módulos para organizar e modularizar nosso código.

 #Tenha em mente

#Python vem com uma ampla biblioteca padrão de módulos que fornecem funcionalidades adicionais. Esses módulos estão disponíveis sem a necessidade de instalá-los separadamente.

#Importar módulos
#Para utilizar um módulo em nosso programa, devemos importá-lo utilizando a declaração import. Podemos importar um módulo completo ou funções específicas de um módulo.

import math  # Importa o módulo math completo

resultado = math.sqrt(25)
print(resultado)  # Saída: 5.0
#Neste exemplo, importa-se o módulo math utilizando a declaração import. Em seguida, utiliza-se a função sqrt() do módulo math para calcular a raiz quadrada de 25.

#ambém podemos importar funções específicas de um módulo utilizando a sintaxe from módulo import função.

from math import sqrt # Importa apenas a função sqrt do módulo math
resultado = sqrt(25)
print(resultado)  # Saída: 5.0
#Neste caso, importa-se apenas a função sqrt() do módulo math, o que nos permite utilizá-la diretamente sem ter que precedê-la com o nome do módulo.

#Funções e classes de módulos padrão
#A biblioteca padrao do Python oferece uma ampla gama de módulos com funções e classes úteis. Alguns exemplos incluem:

#math = Fornece funções matemáticas, como sqrt() (raiz quadrada), sin() (seno), cos() (cosseno), entre outras.

#random = Oferece funções para gerar números aleatórios, como random() (número aleatório entre 0 e 1), randint() (número inteiro aleatório em um intervalo), entre outras.

#datetime = Permite trabalhar com datas e horas, como datetime.now() (data e hora atual), datetime.date() (data), datetime.time() (hora), entre outras.

import random  # Importa o módulo random completo
import datetime  # Importa o módulo datetime completo

numero_aleatorio = random.randint(1, 10)  # Gera um número inteiro aleatório entre 1 e 10
print(numero_aleatorio)  # Saída: Número aleatório entre 1 e 10

data_atual = datetime.datetime.now()  # Obtém a data e hora atual
print(data_atual)  # Saída: Data e hora atual no formato YYYY-MM-DD HH:MM:SS.ssssss

#Estes são apenas alguns exemplos dos muitos módulos disponíveis na biblioteca padrão de Python. Você pode consultar a documentação oficial de Python para obter mais informações sobre os módulos e suas funcionalidades.
