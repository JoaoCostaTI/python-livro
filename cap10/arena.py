tv = {
    "ligado" : False,
    "canal" : 2
}

tvSala = {
    "ligado" : False,
    "canal" : 2
}

tvQuarto = {
    "ligado" : True,
    "canal" : 4
}

def ligaTv(tv):
    tv['ligado'] = True

def desligaTv(tv):
    tv['ligado'] = False

ligaTv(tvSala)
desligaTv(tvQuarto)

print(tvSala)
print(tvQuarto)