# Verificador de Vogal: Escreva um programa que peça uma letra e verifique se é uma vogal ou consoante.

letra = input("Digite uma letra: ")
if letra != "A" and letra != "a" and letra != "E" and letra != "e" and letra != "I" and letra != "i" and letra != "O" and letra != "o" and letra != "U" and letra != "u":
    print(f"A letra '{letra}' é consoante")
else:
    print(f"A letra '{letra}' é vogal")