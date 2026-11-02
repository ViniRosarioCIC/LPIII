# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ").strip().upper()

if letra in "AEIOU":
    print("A letra é uma vogal")
else:
    print("A letra é uma consoante")