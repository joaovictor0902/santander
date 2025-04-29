#Definição e chamada de funções
#Para definir uma função em Python, utilizamos a palavra-chave def seguida do nome da função e parênteses. Opcionalmente, podemos especificar parâmetros dentro dos parênteses. O bloco de código da função é indentado após os dois pontos.

#Para chamar uma função, simplesmente escrevemos o nome da função seguido de parênteses:
def saudacao():
    print('Ola, seja bem-vindo!')
saudacao()

#Parâmetros e argumentos
#As funções podem aceitar parâmetros, que são valores que são passados para a função quando ela é chamada. Os parâmetros são especificados dentro dos parênteses na definição da função.
def saudacao(nome):
    print(f'Ola, {nome}! Seja bem-vindo!')
#Ao chamar a função, fornecemos os argumentos correspondentes aos parâmetros:
saudacao('Maria')
saudacao('Joao')

#Valores de retorno
#As funções podem retornar valores usando a palavra-chave return. O valor de retorno pode ser usado pelo código que chama a função.
def soma(a, b):
    return a + b
resultado = soma(4, 3)
print(resultado)

#Funções anônimas (lambda) 
#Python permite criar funções anônimas ou funções lambda, que são funções sem nome definidas em uma única linha. São comumente usadas para funções pequenas e concisas
qudrado = lambda x: x ** 2
print(qudrado(5))  # Imprime 25

#Escopo das variáveis (local vs. global)
#As variáveis definidas dentro de uma função têm um escopo local, o que significa que só são acessíveis dentro da função. Por outro lado, as variáveis definidas fora de qualquer função têm um escopo global e podem ser acessadas de qualquer parte do programa.

def funcao():
    variavel_local = 10
    print(variavel_local)  # Acessa a variável local dentro da função
    
variavel_global = 20  # Define uma variável global

def funcao2():
    print(variavel_global)
funcao()  # Chama a função interna
funcao2()  # Chama a função interna
print(variavel_global)  # Acessa a variável global fora da função
    #print(variavel_local)  # Acessa a variável local fora da função (causará erro) 

    #Funções definidas pelo usuário
def calcular_media(*numeros):
        soma = sum(numeros)
        quantidadde = len(numeros)
        media = soma / quantidadde
        return media
print(calcular_media(10, 20, 30, 40,))

def soma_3(x):
        return x + 3
soma = lambda x: x + 3
print("Somar e a um numero:", soma(5))  # Imprime 8

#Documentação de funções (docstrings)
#É uma boa prática documentar nossas funções utilizando docstrings. Os docstrings são cadeias de texto que descrevem o propósito, os parâmetros e o valor de retorno de uma função. São colocados imediatamente após a definição da função e são encerrados entre aspas duplas triplas.

def area_retangulo(base, altura):
     """
     calcular a área de um retângulo.

     args:
        base(float): A base do retângulo.
        altura(float): A altura do retângulo.

    retuns:
        float: A área do retângulo.
    """
     return base * altura

#Funções com número variável de argumentos
def soma_variavel(*numeros):
     total = 0
     for numero in numeros:
          total += numero
          return total
    
print(soma_variavel(1, 2, 3,))
print(soma_variavel(4, 5, 6,))

#As funções são uma ferramenta fundamental na programação e nos permitem estruturar e modularizar nosso código. Com a capacidade de definir funções personalizadas, podemos encapsular tarefas específicas e reutilizá-las em diferentes partes do nosso programa.
#Além das funções definidas pelo usuário, Python também fornece uma ampla gama de funções incorporadas que podemos utilizar diretamente, como print(), len(), range(), entre outras.