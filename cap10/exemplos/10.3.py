class Televisao():
    def __init__(self, canalMin, canalMax):
        self.ligada = False
        self.canal = 2
        self.canalMin = canalMin
        self.canalMax = canalMax
    def mudaCanalParaBaixo(self):
        if self.canal - 1 >= self.canalMin:
            self.canal -= 1
    def mudaCanalParaCima(self):
        if self.canal + 1 <= self.canalMax:
            self.canal += 1

tv = Televisao(1,99)
for x in range(0,120):
    tv.mudaCanalParaCima()
print(tv.canal) 

for x in range(0,120):
    tv.mudaCanalParaBaixo()
print(tv.canal)