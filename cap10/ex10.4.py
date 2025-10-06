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
    def mudaCanalParaBaixo(self):
        if self.canal -1 >= self.canalMin:
            self.canal -= 1
        else:
            self.canal = self.canalMax

tv = Televisao()
tv.mudaCanalParaBaixo()
print(tv.canal)
tv.mudaCanalParaCima()
print(tv.canal)



