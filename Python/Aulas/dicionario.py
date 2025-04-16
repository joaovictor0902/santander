pessoa = {"Nome": "Joao", "Idade": 21, "Cidade": "Paranavai"}
print(pessoa["Nome"])  # Acessa o valor associado à chave "Nome"
print(pessoa["Idade"])  # Acessa o valor associado à chave "Idade"
print(pessoa["Cidade"])  # Acessa o valor associado à chave "Cidade"

#Os dicionários em Python têm vários métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:
#keys(): retorna uma visualização de todas as chaves do dicionário.
#values(): retorna uma visualização de todos os valores do dicionário.
#items(): retorna uma visualização de todos os pares chave-valor do dicionário.
#update(outro_dicionario): atualiza o dicionário com os pares chave-valor de outro dicionário.

print(pessoa.keys())  # Imprime todas as chaves do dicionário
print(pessoa.values())  # Imprime todos os valores do dicionário
print(pessoa.items())  # Imprime todos os pares chave-valor do dicionário

pessoa.update({"Profissao": "T.I"})
print(pessoa)  # Imprime o dicionário atualizado com a nova chave-valor
