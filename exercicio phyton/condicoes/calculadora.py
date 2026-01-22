print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = int(input("Escolha a operação: "))
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if op == 1:
    print(a + b)
elif op == 2:
    print(a - b)
elif op == 3:
    print(a * b)
elif op == 4:
    print(a / b if b != 0 else "Erro")
else:
    print("Opção inválida")