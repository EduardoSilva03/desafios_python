# Contador de Caracteres: Faça um programa que peça uma string e conte quantos caracteres ela possui (sem contar espaços em branco no início ou fim).

frase = input("Escreva uma frase: ")
frase = frase.replace(" ", "")
frase = len(frase)

print(frase)