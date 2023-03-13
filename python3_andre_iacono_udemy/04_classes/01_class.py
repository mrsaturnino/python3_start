# criando uma classe

class Usuario:

    # criando um construtor para a classe
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    # criando uma função para exibir os dados passados aos atributos do objeto criado
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome


# criando um objeto a partir da classe 'Usuario'
usuario1 = Usuario('Andre', 'Saturnino')

print(usuario1.nome_completo())
# ou
print(Usuario.nome_completo(usuario1))
