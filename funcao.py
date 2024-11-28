def calcular_media(*numeros): # funções que aceite um numero variável de argumento, ultiliza * antes do nome de parâmetro.
    suma = sum(numeros)
    quantidade = len(numeros)
    media = suma / quantidade
    return media

print("media: ", calcular_media(10, 20, 30, 40))

def somar_3(x):
    return x + 3

somar = lambda x: x + 7

print("somar 3 a um numero", somar(2))


def funcao():
    variavel_local = 10
    print(variavel_local)  # Acessível dentro da função


variavel_global = 20


def funcao2():
    print(variavel_global)  # Acessível de qualquer lugar


funcao()  # Imprime 10
funcao2()  # Imprime 20
print(variavel_global)  # Imprime 20
print(variavel_local)  # Gera um erro, a variável não está definida neste escopo.

