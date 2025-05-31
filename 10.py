# Calculadora de Fatorial: Escreva um programa que peça um número inteiro não negativo e calcule o seu fatorial. (Ex: 5! = 5 * 4 * 3 * 2 * 1 = 120).

num = int(input("Digite um número inteiro: "))

if num < 0:
    print("Número inválido")
else:
    fatorial = 1
    for i in range (1, num + 1):
        fatorial *= i
    print(f"O fatorial de {num} é {fatorial}")