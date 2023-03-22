# Ao rodar loops em uma lista, devemos lembrar que os espaços são alocados na memória. Quanto maior a lista, maior o espaço alocado.
# Uma forma mais rápida para lists, dictionaries e etc.
# Menos memória alocada, valores em bytes.

# importando a lib que possui a função "getsizeof", que ajudará a visualizar o consumo de memória do programa
from sys import getsizeof


# Percorrendo um loop numa lista de forma normal.

numerosLista = [x * 10 for x in range(10)]
print(type(numerosLista))  # exibindo o tipo, que é uma lista

print(numerosLista)  # exibindo a lista

print(getsizeof(numerosLista))
# Ao ser exibido, o getsizeof vai nos mostrar que a "numerosLista" é mais pesada a cada vez que aumentamos o "range()".


print('===========================')


# Percorrendo um loop em uma lista utilizando o generator expressions
# para utilizar o Generator Expressions, basta aplicar dessa forma, com parênteses.
numeros = (x * 10 for x in range(10))

print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))
# No caso do Generator Expressions, não perdemos performance ao estar claro que o tamanho não é alterado da mesma maneira que na "numerosLista".
