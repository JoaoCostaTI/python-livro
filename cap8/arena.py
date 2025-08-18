def map_1(funcao, valores):
    retorno = []
    for v in valores:
        retorno.append(funcao(v))
    return retorno
print(map_1(lambda x: x/2, [1,2,3]))

print(list(map(lambda x: x/2, [1,2,3,4,5])))

def map_2(funcao, *valores):
    retorno = []
    for v in zip(*valores):
        retorno.append(funcao(*v))

    return retorno

print(map_2(lambda a,b: (a,b), [1,2,3], [4,5,6]))