def imprimeListas(lista,nivel=0):
    
    for x in lista:
        if isinstance(x, int):
            print(f'{x:{nivel*2}}')
        else:
            imprimeListas(x, nivel + 1)
imprimeListas([1,[2,3,4],[5,6,[7,8,9]],10])