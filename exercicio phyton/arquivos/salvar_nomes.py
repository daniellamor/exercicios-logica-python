with open("nomes.txt", "a") as arquivo:
    nome = input("Digite um nome: ")
    arquivo.write(nome + "\n")