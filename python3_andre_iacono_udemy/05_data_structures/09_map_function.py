# a função map é muito utilizada com listas

listaNum = [1, 2, 3, 4, 5, 6]

def multiNum(x):
    return x * 2

listaMap = map(multiNum, listaNum) # O Iterable "x", vai garantir que cada item da lista seja mapeado à função e seja aplicado a operação matemática que está no retorno.

print(list(listaMap)) # Importante converter o resultado em uma lista, já que após a função ".map", este resultado se torna um objeto.