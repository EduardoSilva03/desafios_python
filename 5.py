# Tabuada Simples: Crie um programa que solicite um número e imprima a tabuada de multiplicação desse número (de 1 a 10).

num = int(input("Digite um número para ver sua tabuada: "))
print(f"Tabuada do {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")