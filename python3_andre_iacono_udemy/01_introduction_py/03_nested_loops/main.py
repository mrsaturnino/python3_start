#nested for loops

#Outer loop
    #Inner loop
    
#Loop 'PAI'
for produto1 in range(1,6): #contar A PARTIR da posição 1 ATÉ a 6
    print('Produto ' + str(produto1))
    
    #Loop 'FILHO'
    for numero2 in range(5):
        print(f'{produto1} Categoria {numero2}')
        
#Aqui, o loop 'PAI' irá executar o loop filho inteiro cada vez que ele for executado.
#Ou seja, a cada vez que o loop 'PAI' executa, ele executa o loop 'FILHO' por inteiro.