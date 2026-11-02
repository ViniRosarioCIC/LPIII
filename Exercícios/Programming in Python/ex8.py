# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Digite o preco do primeiro produto"))
produto2 = float(input("Digite o preco do segundo produto"))
produto3 = float(input("Digite o preco do terceiro produto"))

print(f"O melhor preco é o produto de valor RS{min(produto1, produto2, produto3)}")