class Animal:
    def __init__(self,nome):
        self.nome=nome
    
    def som(self):
        return "..."
class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome)
        self.cor = cor
    
    def som(self):
        return "miau"

g = Gato("mimi","preto")
print(g.nome, g.cor , g.som())