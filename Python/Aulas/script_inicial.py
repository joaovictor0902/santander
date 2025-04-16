frutas = ["pera", "banana", "laranja", "uva", "abacaxi"]
print(frutas[0])  # Acessa o primeiro elemento da lista
print(frutas[1])  # Acessa o segundo elemento da lista
print(frutas[2])  # Acessa o terceiro elemento da lista
print(frutas[3])  # Acessa o quarto elemento da lista
print(frutas[4])  # Acessa o quinto elemento da lista

frutas.append("kiwi")  # Adiciona "kiwi" ao final da lista
print(frutas)  # Imprime a lista atualizada

frutas.insert(2, "manga")  # Insere "manga" na posição 2 (terceiro lugar)
print(frutas)  # Imprime a lista atualizada

frutas.remove("banana")  # Remove "banana" da lista
print(frutas)  # Imprime a lista atualizada

fruta_removida = frutas.pop(2)  # Remove e retorna o elemento na posição 1 (segundo lugar)
print(frutas)  # Imprime a lista atualizada
print(fruta_removida)  # Imprime a fruta removida 

frutas.sort()  # Ordena a lista de frutas em ordem alfabética
print(frutas)  # Imprime a lista ordenada

frutas.reverse()  # Inverte a ordem da lista de frutas
print(frutas)  # Imprime a lista invertida