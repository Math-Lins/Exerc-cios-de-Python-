class Pessoa:
    def __init__(self, nome,peso, idade, comendo=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo

    def BotarComer(self, comida):
        self.comida = comida
        if self.comendo == False:
            self.comendo = True
            print(f'{self.nome} está comendo {self.comida}')
        else:
            print(f'{self.nome} já está comendo')
    def PararComer(self):
        if self.comendo == True:
            self.comendo = False
            print(f'{self.nome} pare de comer')
        else:
            print(f'{self.nome} não está comendo')
    def falar(self):
        self.falando = False
        if self.falando == False:
            if self.comendo == True:
                print(f'{self.nome} está comendo, não pode falar')
            else:
                 print(f'{self.nome} pode falar')
                 self.falando = True
        else:
            print(f'{self.nome} está falando')




p1 = Pessoa("Matheus",100,25)
p2 = Pessoa("Aline",50,24)


p1.BotarComer("Hambúrguer")
p1.PararComer()
p1.falar()
p2.BotarComer("Sushi")
p2.PararComer()
p2.falar()

# print(vars(p1))
# print(vars(p2))

