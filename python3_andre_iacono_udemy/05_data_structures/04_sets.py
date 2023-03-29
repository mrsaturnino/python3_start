# Sets são similares às listas. Porém, não utilizam index e evitam itens duplicados.

#criando um set
setEx = {1, 4, 5, 6}

print(setEx)
print(type(setEx))

#criando listas
list1 = [10, 20, 40]
list2 = [15, 31, 50]

#transformando listas em sets
set1 = set(list1)
set2 = set(list2)

#printando os dois sets juntos
print(set1 | set2)
print(type(set1 | set2))


#(num1 | num2) => uniao
#(num1 - num2) => diferença
#(num1 ^ num2) => diferenca simetrica (tira os duplicados)
#(num1 & num2) => união (printa todos os duplicados)