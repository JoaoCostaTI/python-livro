from functools import total_ordering

@total_ordering

class TipoTelefone:
    def __init__(self, tipo):
        self.tipo = tipo
    def __str__(self):
        return f"({self.tipo})"
    def __eq__(self, outro_valor):
        if outro_valor is None:
            return False
        return self.tipo == outro_valor.tipo
    def __lt__(self, outro_valor):
        return self.tipo < outro_valor.tipo
    
