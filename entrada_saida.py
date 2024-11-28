# entrada e saída de dados

nome = input("Insira seu nome: ") # input() sempre retorna uma cadeia de texto.
idade = input("Insira sua idade: ")


print("Olá, " + nome + "!")
print("Você tem " + idade + " anos.")


print("_______________________________________")

Idade = int(input("Insira sua idade: "))

if Idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
    
    
print("_______________________________________")

nome = "Juan"
idade = 25


print(f"Olá, meu nome é {nome} e tenho {idade} anos.")