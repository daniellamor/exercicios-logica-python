numeros = []

for _ in range(10):
    numeros.append(int(input("Digite um número: ")))

print("Maior:", max(numeros))
print("Menor:", min(numeros))
print("Média:", sum(numeros) / len(numeros))