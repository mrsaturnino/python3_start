# Mais simples de escrever loops e outras coisas dentro de uma lista ou para ela
# var = [expressão for iten in itens]


frutas = ['abacaxi', 'melancia', 'ameixa', 'limao']

# Forma convencional:

#Criando uma lista vazia de 'frutas'
frutasList = []

#Para cada item em "frutas[]" que possua a letra 'n' e 'm', adicione em "frutasList[]"
for item in frutas:
    if 'n' and 'm' in item:
        frutasList.append(item)


# Com o List Comprehension


frutasList_v2 = [item for item in frutas if 'a' in item]

print(frutasList)
print()
print(frutasList_v2)