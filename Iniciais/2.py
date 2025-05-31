# 2. Número Par ou Ímpar: Crie um programa que peça um número e diga se ele é par ou ímpar.

print("Digite um número para verificar se é par ou ímpar: ")
num = int(input("Número: "))
if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")