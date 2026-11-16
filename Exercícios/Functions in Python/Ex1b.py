def soma_elementos(lista):
    if not lista:
        return None
    return sum(lista)

resultado = soma_elementos([1,2,3,4,5])

print(resultado)