frutas = {"maca, banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])
 #Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao =  conjunto1 | conjunto2  # União
print(uniao) # Saída: {1, 2, 3, 4, 5}

intersecao = conjunto1 & conjunto2  # Interseção
print(intersecao) # Saída: {3}

diferenca = conjunto1 - conjunto2  # Diferença 
print(diferenca) # Saída: {1, 2}

diferenca_simetrica = conjunto1 ^ conjunto2  # Diferença simétrica
print(diferenca_simetrica) # Saída: {1, 2, 4, 5}

#Os conjuntos em Python têm vários métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:
#add(elemento): adiciona um elemento ao conjunto.
#remove(elemento): remove um elemento do conjunto. Se o elemento não existir, gera um erro.
#discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
#clear(): remove todos os elementos do conjunto.

frutas.add("pera ")
print(frutas) # Saída: {'banana', 'laranja', 'pera ', 'maca, banana'}

frutas.remove("pera ")
print(frutas) # Saída: {'banana', 'laranja', 'maca, banana'}

frutas.discard("uva") # Não gera erro se "uva" não estiver presente
print(frutas) # Saída: {'laranja', 'maca, banana'}

frutas.clear() # Remove todos os elementos do conjunto
print(frutas) # Saída: set()