# Cálculo de Média: Faça um programa que peça três notas de um aluno e calcule a média.

num1 = float(input("Primeira nota: "))
num2 = float(input("Segunda nota: "))
num3 = float(input("Terceira nota: "))

soma = num1 + num2 + num3
media = soma / 3

print(f"A sua média é: {media}")