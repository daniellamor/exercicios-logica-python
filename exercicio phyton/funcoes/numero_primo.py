def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Digite um número: "))
print("É primo?" , eh_primo(num))