# o try executará um bloco de código, em seguida, caso haja algum erro de execução o except será acionado de acordo com a classe do erro colocada nele.
try:
    letras = ['a', 'b', 'c']
    print(letras[3])
    
except IndexError:
    print('O index nao existe.')