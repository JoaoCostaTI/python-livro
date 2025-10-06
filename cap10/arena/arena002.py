class Televisão:
    def __init__(self, min=2, max=14):
        self.ligada = False
        self.canal = min
        self.cmin = min
        self.cmax = max

    def mudaCanalParaBaixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax
        return self.canal

    def mudaCanalParaCima(self):
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

tvJoao = Televisão()

tvJoaoDict = vars(tvJoao)
print()
print(f"Dicionário Completo = {tvJoaoDict}")
print()
print('AGORA COMEÇAMOS COM O CONTROLE REMOTO')
print()


