# Contagem Regressiva: Escreva um programa que peça um número inteiro positivo e realize uma contagem regressiva a partir desse número até zero.

print("Digite um número inteiro positivo para iniciar a contagem regressiva: ")
num = int(input("Número: "))
if num < 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    print("Contagem regressiva:")
    for i in range(num, -1, -1):
        print(i)