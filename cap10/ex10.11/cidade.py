class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao
        self.estado = None
    
    def __str__(self):
        return f"Cidade(Nome = {self.nome}, Popilação = {self.populacao}, Estado = {self.estado})"