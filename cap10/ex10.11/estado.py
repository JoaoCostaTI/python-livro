
class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []
    
    def adicionaCidade(self, cidade):
        self.cidades.append(cidade)

    def calcula_populacao(self):
        return sum(cidade.populacao for cidade in self.cidades)

    def resumo(self):
        print('-' * 15)
        print(f"Estado: {self.nome}\nSigla: {self.sigla}\nCidades:")
        somaPop = 0
        for c in self.cidades:
            print(f" - {c.nome}")
            somaPop += c.populacao
        print(f"População Total: {somaPop} pessoas")

#Estado 
minas = Estado('Minas Gerais', 'MG')
sp = Estado('São Paulo', 'SP')
rio = Estado('Rio de Janeiro', 'RJ')

#Cidades
bh = Cidade('Belo Horizonte', 1500)
curvelo = Cidade('Curvelo', 3000)

taboao = Cidade('Taboão da Serra', 5000)
diadema = Cidade('Diadema', 6558)

arraial = Cidade('Arraial do Cabo', 3000)
barra = Cidade('Barra de Piraí', 2500)


#Adicionando as cidades no estado
minas.adicionaCidade(bh)
minas.adicionaCidade(curvelo)

sp.adicionaCidade(taboao)
sp.adicionaCidade(diadema)

rio.adicionaCidade(arraial)
rio.adicionaCidade(barra)

minas.resumo()
sp.resumo()
rio.resumo()

