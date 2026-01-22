soma = 0

while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    soma += num

print("Soma total:", soma)