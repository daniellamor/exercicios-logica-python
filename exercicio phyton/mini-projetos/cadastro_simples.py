with open("cadastro.txt", "a") as arquivo:
    nome = input("Nome: ")
    idade = input("Idade: ")
    arquivo.write(f"{nome} - {idade}\n")