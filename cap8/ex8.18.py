def imprimeListas(lista,nivel=0, carac = " ", incremento = 2):
    
    for x in lista:
        if isinstance(x, int):
            print(f'{carac * (nivel * incremento)}{x}')
        else:
            imprimeListas(x, nivel +1, carac, incremento)
imprimeListas([1,[2,3,4],[5,6,[7,8,9]],10], carac="*", incremento=4)

