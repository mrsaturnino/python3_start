#Functions

def say_hello():
    print("hello!")
    
say_hello()

#função de soma

def somar_dois_numeros():
    num1 = 20
    num2 = 34
    resultado = num1 + num2
    print(resultado)
    
somar_dois_numeros()

def pessoa(nome, idade):
    print(f'Seu nome é {nome} e possui {str(idade)} anos.')

pessoa("Andre", 20)

def produto(nome, quantidade):
    print(f'O nome do produto é {nome} e tem {str(quantidade)} unidades.')