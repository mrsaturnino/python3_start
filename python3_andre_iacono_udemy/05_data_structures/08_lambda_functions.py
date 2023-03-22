# Uma função lambda não precisa ter um nome. pode estar dentro de uma outra função ou variável e por isso costumam ser PEQUENAS.
# Pode ter vários argumentos, mas somente 1 expressão.

def somar(x):
    return x + 10

somar(5)

somarAo10 = lambda v, w, x, y, z: v + w + x + y + z + 10
print(somarAo10(2, 5, 6, 7, 9))

# lambda x: x + 10