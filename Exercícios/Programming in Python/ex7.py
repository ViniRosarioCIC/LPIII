#7. Faça um Programa que leia três números e mostre o maior e o menor deles.

x = float(input("Digite o primeiro valor"))
y = float(input("Digite o segundo valor"))
z = float(input("Digite o terceiro valor"))

print(f"O maior valor é: {max(x,y,z)}")
print(f"O menor valor é: {min(x,y,z)}")