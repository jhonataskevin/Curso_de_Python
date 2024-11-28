print("Lista (manipulação)")

frutas = ["maçã", "banana", "laranja"]

frutas.append("pera") # adiciona um elemento ao final da lista.
print(frutas) # Imprime ["maçã", "banana", "laranja", "pera"]

frutas.insert(1, "uva") # insere um elemento numa posição específica da lista.
print(frutas) # Imprime ["maçã", "uva", "banana", "laranja", "pera"]

frutas.remove("banana") # remove a primeira ocorrência da lista.
print(frutas) # Imprime ["maçã", "uva", "laranja", "pera"]

fruta_removida = frutas.pop(2)
print(frutas) # Imprime ["maçã", "uva", "pera"]
print(fruta_removida) # Imprime "laranja"

frutas.sort() # ordena os elementos da lista em ordem acendente.
print(frutas) # Imprime ["maçã", "pera", "uva"]

frutas.reverse()
print(frutas) # Imprime ["maçã", "pera", "maçã"]



print("___________________________________________________")

print("Lista de compreensão")


numero = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in numero if x % 2 == 0]
print(quadrados) # Imprime [4, 16]

print ("___________________________________________________")

print ("Tupla é uma estrutura de dados imutável")


minha_tupla = (1, 2, 3, 2, 4, 2)


print (minha_tupla.index(2))   # Saída: 1

print (minha_tupla.index(2, 2))   #Saída: 3

print (minha_tupla.index(2, 2, 4))   #Saída: 3


print("_____________________________________________")

print(" Dicionário é uma estrutura de dados mutável e não ordenada.")



pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}


print(pessoa.keys())    # Imprime dict_keys(["nome", "idade", "cidade"]) - retorna uma visualização de todas as chaves.
print(pessoa.values())  # Imprime dict_values(["João", 25, "Madri"]) - retorna uma visualização de todos os valores.
print(pessoa.items())   # Imprime dict_items([("nome", "João"), ("idade", 25), ("cidade", "Madri")]) - retorna todos os pares chave-valor.


pessoa.update({"profissao": "Engenheiro"}) # ele atualiza o dicionario com os pares chave-valor.
print(pessoa)  # Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}

print("______________________________________________")

print("Conjunto (set) mutável e não ordenada que permite armazenar uma coleção de elementos.")

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


uniao = conjunto1 | conjunto2 # união
print(uniao)  # Imprime {1, 2, 3, 4, 5}


intersecao = conjunto1 & conjunto2 # interseção
print(intersecao)  # Imprime {3}


diferenca = conjunto1 - conjunto2 # diferença
print(diferenca)  # Imprime {1, 2}


diferenca_simetrica = conjunto1 ^ conjunto2 # diferença simétrica
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}

print("___________________________________________________")

print("Métedos de conjunto")

frutas = {"maçã", "banana", "laranja"}


frutas.add("pera") # adiciona.
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}


frutas.remove("banana") # remove um elemento do conjunto. Se o elemento não existir, gera um erro.
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.discard("uva") # remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.clear() # remove todos os elemetos.
print(frutas)  # Imprime set()

