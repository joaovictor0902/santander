#Além de utilizar os módulos padrão do Python, também podemos criar nossos próprios módulos para organizar e reutilizar nosso código.

 #Criar e utilizar módulos personalizados
#Para criar um módulo personalizado, simplesmente criamos um novo arquivo Python com o nome desejado e definimos as funções, classes e variáveis que queremos incluir no módulo. Por exemplo, criamos um arquivo (no mesmo diretório onde estamos executando Python) chamado meu_modulo.py com o seguinte conteúdo:

#meu_modulo.py
def saudar(nome):
    print(f"Ola, {nome}!")

def caucular(a, b):
    return a + b