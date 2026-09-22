##Objetivo: Criar uma lista com os 20 primeiros termos da sequência de Fibonacci utilizando a estrutura de List Comprehension.

##Definição fornecida: A sequência de Fibonacci é descrita como uma sequência de números inteiros que inicia com 1 e 1, onde cada número subsequente é a soma dos dois anteriores (Exemplo: 1, 1, 2, 3, 5, 8, 13, 21...).


a = 0
b = 1

lista_fibonacci = [(a :=b, b:= a+b)[0] for _ in range(20)]

print(lista_fibonacci)