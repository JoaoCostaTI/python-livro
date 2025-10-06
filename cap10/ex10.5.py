"""
class Televisao():
    def __init__(self, min = 2, max = 14):
        self.ligada = False
        self.canal = min
        self.canalMin = min
        self.canalMax = max
    def mudaCanalParaCima(self):
        if self.canal + 1 <= self.canalMax:
            self.canal += 1 
        else:
            self.canal = self.canalMin
        return self.canal
    def mudaCanalParaBaixo(self):
        if self.canal -1 >= self.canalMin:
            self.canal -= 1
        else:
            self.canal = self.canalMax
        return self.canal

tv1 = Televisao(min=1, max=22)
tv1.mudaCanalParaBaixo()
print(tv1.canal)
tv1.mudaCanalParaCima()
print(tv1.canal)

tv2 = Televisao(min=2, max=64)
tv2.mudaCanalParaBaixo()
print(tv2.canal)
tv2.mudaCanalParaCima()
print(tv2.canal)
"""

class Televisão:
    def __init__(self, min=2, max=14):
        self.ligada = False
        self.canal = min
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax
        return self.canal

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin
        return self.canal


tv = Televisão(min=1, max=22)
tv.muda_canal_para_baixo()
print(tv.canal)
tv.muda_canal_para_cima()
print(tv.canal)

tv2 = Televisão(min=2, max=64)
tv2.muda_canal_para_baixo()
print(tv2.canal)
tv2.muda_canal_para_cima()
print(tv2.canal)

