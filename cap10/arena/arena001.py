class Televisao():
    def __init__(self):
        self.ligado = False
        self.canal = 2
        self.tamanho = 43
        self.marca = "Xiaomi"
    def descrever(self):
        for atributos in vars(self).items():
            print(atributos)

tvSala = Televisao()
tvQuarto = Televisao()

tvQuarto.ligado = True
tvQuarto.canal = 21
tvQuarto.tamanho = 50
tvQuarto.marca = 'Sony'

tvQuarto.descrever()


