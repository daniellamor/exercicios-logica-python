import random

numero = random.randint(1, 10)
tentativas = 0

while True:
    palpite = int(input("Digite um número de 1 a 10: "))
    tentativas += 1

    if palpite == numero:
        print(f"Acertou em {tentativas} tentativas!")
        break
    else:
        print("Tente novamente")