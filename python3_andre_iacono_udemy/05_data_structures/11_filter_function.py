# Da mesma forma que a função map, é muito utilizado com arrays, lists, tuples e dictionaries
# Aplica uma  função a um Iterable, filtrando os 'items'.

valores = [10, 11, 45, 54, 90]

def remover20(x):
    return x > 20

print(list(filter(remover20, valores))) # retorna os valores que atendem à condição

print(list(filter(lambda x: x > 20, valores)))