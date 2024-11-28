# leitura e escrita de arquivos externos

arquivo = open("dados.txt", "r") # faz a abertura em modo de leitura "r".
conteudo = arquivo.read() # aqui ele faz a leitura.
print(conteudo) # depois aqui ele imprime na tela o conteudo que estava no arquivo.
arquivo.close() # Improtante sempre fechar o arquivo para liberar os recursos do sistema.

print("____________________________________________________")

arquivo = open("dados.txt", "w") # faz a abertura de modo de escrita "W".
arquivo.write("Olá, mundo!") # o conteudo a ser escrito.
arquivo.close()

print("____________________________________________________")

with open("dados.txt", "r") as arquivo: # declaração with faz a abertura e o fechamento automatico uma vez que se sai do bloco with.
    conteudo = arquivo.read()
    print(conteudo)