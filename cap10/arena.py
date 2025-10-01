"""
class televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

tvQuarto = televisao()

print(tvQuarto.ligada)

print(tvQuarto.canal)

tvSala = televisao()
tvSala.ligada = True
tvSala.canal = 86
print(tvSala.ligada)
print(tvSala.canal)
"""
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
    def mudaCanalParaBaixo(self):
        self.canal -= 1
    def mudaCanalParaCima(self):
        self.canal += 1
    
tvJoao = Televisao()

print(f'Canal Atual TV João: {tvJoao.canal}')
tvJoao.mudaCanalParaCima()
print(f"Alterando o canal passou para: {tvJoao.canal}")