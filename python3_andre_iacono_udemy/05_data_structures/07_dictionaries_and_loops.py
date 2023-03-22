aluno = {'nome': 'Jose', 'idade': 23, 'nota_final': 'SS', 'aprovacao': True}

for keys, values in aluno.items():
    print(keys, values)
    print()


# Organizando e visualizando dicionários

aluno2 = {
          'nome': 'Andre',
          'idade': 21, 
          'nota_final': 'SSS', 
          'aprovacao': True,
          'Materias': ['Fisica', 'Matematica', 'Ingles', 'History']
}

print(aluno2.items()) # Imprime todas as keys e values do dicionario
print(aluno2.keys()) # Imprime apenas as keys
print(aluno2.values()) # Imprime apenas os values