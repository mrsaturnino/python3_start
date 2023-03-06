try:
    value = int(input('Digite a sua idade: '))
    print(type(value))
    print(value)

except ValueError:
    print('Este dado não é um número. Digite uma informação válida.')
 

#o finally sempre será executado independente de ocorrer um erro ou não. 
finally:
    print('O usuário digitou uma informação.')   

#o else será executado se o try for verdadeiro.
#else:
#    print('O usuário digitou a idade corretamente.')