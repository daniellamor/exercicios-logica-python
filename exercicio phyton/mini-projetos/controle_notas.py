alunos = {}

while True:
    nome = input("Nome do aluno (ou sair): ")
    if nome == "sair":
        break
    nota = float(input("Nota: "))
    alunos[nome] = nota

for aluno, nota in alunos.items():
    status = "Aprovado" if nota >= 6 else "Reprovado"
    print(aluno, "-", status)