##Return & Print

def cliente1(nome):
    print(f'Olá {nome}')
# O "print" não gera valor algum, ele apenas imprime.

    
def cliente2(nome):
    return f'Olá {nome}'
# O "return" armazena o valor gerado pela function.

print(cliente1('Andre')) #como o print nao armazena valor algum, apenas exibe, o console exibirá "None".

print(cliente2('Andre')) #Aqui, o return armazenou o valor passado no argumento e na chamada da função esse valor foi exibido.


