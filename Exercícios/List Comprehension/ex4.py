termo_atual = [0]

lista = [termo_atual := 2 * termo_atual + 3 if _ > 0 else 0 for _ in range(20)]

print(lista)