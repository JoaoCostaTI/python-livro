def soma(a,b):
    return a + b
def sub(a,b):
    return a - b
def imprime(a,b, foper):
    print(foper(a,b))

imprime(4,5, soma)
imprime(9,6, sub)