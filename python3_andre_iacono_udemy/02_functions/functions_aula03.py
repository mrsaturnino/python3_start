# Adicionando vários Argumentos ao chamar uma function. (xargs)

# A ideia é conseguir flexibilidade dentro de uma função, podendo, na chamada da função, definir vários argumentos e vários parâmetros com o operador "*" na definição dos parâmetros da function.

def soma(*numeros): #xargs permite que ao chamar uma função, vários valores pode 
    
    result = 0 #valor inicial do loop
    for num in numeros: 
        result += num
    return result
    
x = soma(2,3,4,5,6) #passando vários argumentos de acordo com o parâmetro números, que se trata de um xargs.

print(x)


def concessionaria(**carro): # adicionando mais um asterisco, indicamos à function que iremos colocar mais parâmetros.
    return carro

print(concessionaria(fabricante='Honda', cor='Cinza', motor=2.0))