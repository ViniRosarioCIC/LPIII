# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

x = float(input("Digite o primeiro numero:"))
y = float(input("Digite o segundo numero: "))
z = float(input("Digite o terceiro numero: "))

lista = sorted((x,y,z), reverse=True)

print(f"Ordem decrescente: {lista}")

