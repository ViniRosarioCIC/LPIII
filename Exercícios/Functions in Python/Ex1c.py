def primeiro_elemento(lista):
    if not lista:
        return None
    primeiro = lista[0]
    return lista.count(primeiro)

resultado = primeiro_elemento([1,2,11,1,1,2,3])

print (resultado)