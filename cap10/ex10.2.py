class Televisão():
    def __init__(self,canalInicial, canalMin, canalMax):
        self.ligada = False
        self.canal = canalInicial
        self.canalMin = canalMin
        self.canalMax = canalMax
    def mudaCanalParaBaixo(self):
        if self.canal - 1 >= self.canalMin:
            self.canal -= 1
    def mudaCanalParaCima(self):
        if self.canal + 1 <= self.canalMax:
            self.canal += 1

tv = Televisão(5, 1, 99)

for x in range(1, 99):
    tv.mudaCanalParaCima()
print(tv.canal)
for x in range(0, 120):
    tv.mudaCanalParaBaixo()
print(tv.canal)