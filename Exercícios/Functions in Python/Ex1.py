# 1. Crie uma função que recebe uma lista de números e
# a. retorne o maior elemento

def maior_elemento(lista):

    if not lista:
        return None
    
    return max(lista)


aux = maior_elemento([1, 2, 3, 4, 5])
print(aux)


