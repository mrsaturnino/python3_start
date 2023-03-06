try:
    value = int(input('Digite a sua idade: '))
    print(type(value))
    print(value)

except ValueError:
    print('Este dado não é um número. Digite uma informação válida.')
