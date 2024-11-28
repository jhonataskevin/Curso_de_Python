try:
    # Código que pode gerar uma exceção
    arquivo = open("arquivo.txt", "r") 
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção


print("_________________________________________")

def funcao():
    # Código que pode gerar uma exceção personalizada
    if condicao:
        raise Exception("Descrição do erro")

try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")

'''
 - define-se uma função chamada funcao(). Dentro da função, verifica-se uma condição e,
 se for satisfeita, gera-se uma exceção utilizando a declaração raise.
 Em vez de criar uma classe personalizada, utiliza-se diretamente a classe base Exception para gerar a exceção.

 - considerando os possiveis erros que podem ocorrer no codigo e utilizando o tratamento de exceções 
   adequado para lidar com eles de maneira apropriada.
   Isso tornará o programa mais robusto e confiável.

'''