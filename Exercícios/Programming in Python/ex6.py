# 6. Faça um Programa que leia três números e mostre o maior deles.

x = float(input("Digite um valor: "))
y = float(input("Digite um valor: "))
z = float(input("Digite um valor: "))

if x >= y and x >= z:
    print(f"O maior valor é {x}")
elif y >= x and y >= z :
    print(f"O maior valor é {y}")
else:
    print(f"O maior valor é: {z}")
