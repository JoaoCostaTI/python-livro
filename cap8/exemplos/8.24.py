import types

def dizOTipo(a):
    if isinstance(a,str):
        return "String"
    elif isinstance(a, list):
        return "Lista"
    elif isinstance(a, dict):
        return "Dicionario"
    elif isinstance(a, int):
        return "Inteiro"
    elif isinstance(a, float):
        return 'Numero decimal'
    elif isinstance(a, types.FunctionType):
        return "Função"
    elif isinstance(a, types.BuiltinFunctionType):
        return "Função Interna"
    else:
        return str(type(a))

print(dizOTipo(10))
print(dizOTipo(10.5))
print(dizOTipo("Alo"))
print(dizOTipo([1,2,3]))
print(dizOTipo({"a":2,"b":50}))
print(dizOTipo(print))
print(dizOTipo(None))
