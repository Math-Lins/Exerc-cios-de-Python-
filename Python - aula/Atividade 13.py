class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} foi comer...")

    def emitir_som(self):
        print(f"O {self.nome} emitiu som...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def emitir_som(self):
        print(f"O {self.nome} foi miando...")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def emitir_som(self):
        print(f"O {self.nome} foi latindo...")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)



g1 = Gato("Garfield", "Rajado")
g1.emitir_som()
g1.comer()
c1 = Cachorro("Thor", "Caramelo")
c1.emitir_som()
c1.comer()
v1 = Vaca("Joyce", "Preta e branca")
v1.comer()
v1.emitir_som()