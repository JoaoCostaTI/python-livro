class Televisão:
    def __init__(self, min=2, max=14):
        self.ligada = False
        self.canal = min
        self.cmin = min
        self.cmax = max
        
    def mudaCanalParaBaixo(self):
        if not self.ligada:
            return
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax
        return self.canal

    def mudaCanalParaCima(self):
        if not self.ligada:
            return
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin
        return self.canal

class controleRemoto:
    def __init__(self, televisao, pilha):
        self.televisao = televisao
        self.pilha = pilha
    def liga(self):
        if self.pilha.consuma(1):
            self.televisao.ligada = True
    def desliga(self):
        if self.pilha.consuma(1):
            self.televisao.ligada = False
    def canalMais(self):
        if self.pilha.consuma(1):
            self.televisao.mudaCanalParaCima()
    def canalMenos(self):
        if self.pilha.consuma(1):
            self.televisao.mudaCanalParaCima()

class Pilha:
    def __init__(self, energia = 100):
        self.energia = energia
    def consuma(self, consumo):
        if consumo > self.energia:
            consumo = self.energia
        self.energia -= consumo
        return consumo

tv = Televisão(2, 14)
pilha = Pilha(5)
controle = controleRemoto(tv, pilha)
print(tv.canal)
print(pilha.energia)

controle.canalMais()
controle.canalMais()
controle.canalMais()
controle.canalMais()

print(tv.canal)
print(pilha.energia)
print(tv.canal)

print(pilha.energia)

controle.canalMais()
print(tv.canal)

print(pilha.energia)
controle.canalMais()

print(tv.canal)
