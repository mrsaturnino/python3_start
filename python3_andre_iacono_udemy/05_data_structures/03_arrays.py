#Para utilizar arrays no python, basta importar o módulo "array".

from array import array

#para criar arrays, faz-se necessário de criarmos uma Lista e então convertê-la em Array.

lista_numeros = [1, 2, 3, 4, 5]
lista_letras = ['a', 'b', 'c', 'd']

#convertendo em arrays:

lista_numeros = ('i', [1, 2, 3, 4, 5])
lista_letras = ('u', lista_letras)

print(lista_numeros)
print(type(lista_numeros))

print(lista_letras)
print(type(lista_letras))