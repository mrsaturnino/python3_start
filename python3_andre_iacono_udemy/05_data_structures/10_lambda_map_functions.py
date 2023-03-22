# a função map é muito utilizada com listas

listaNum = [1, 2, 3, 4, 5, 6]

#def multiNum(x):
    #return x * 2

# O Iterable "x", vai garantir que cada item da lista seja mapeado à função e seja aplicado a operação matemática que está no retorno.

# Abaixo, um exemplo utilizando a map function com Lambda, reduzindo no fim a operação à uma linha de código.
listaMap = map(lambda x: x * 2, listaNum)

print(list(listaMap))

print(list(map(lambda x: x * 2, listaNum)))