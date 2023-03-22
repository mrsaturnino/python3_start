aluno = {'nome': 'Andre', 'idade': 20}

# 'nome': => Key
# 'Andre' => Value

print(aluno['nome'], aluno['idade'])

# Alterando o valor(value) da key
aluno['nome'] = 'Jose'
print(aluno)

# Alterando vários values das keys ao mesmo tempo
aluno.update({'nome': 'Ana', 'idade': 21})

# Capturando valores de uma key
print(aluno.get('nome'))

# Deletando um valor
del aluno['nome']
