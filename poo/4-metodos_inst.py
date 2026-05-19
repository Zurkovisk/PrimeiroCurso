class Game:
    def __init__(self, name="", year=0, multiplayer=False, note=0):
        self.name = name
        self.year = year
        self.multiplayer = multiplayer
        self.note = note

    def __str__(self):
        return f"Nome: {self.name}, Ano: {self.year}, Multijogador: {self.multiplayer}, Nota: {self.note}"

    def technical_sheet(self):
        print("###Dados so Jogo###")
        print(f"\nNome do Jogo: {self.name}")
        print(f"Ano de Lançamento: {self.year}") 
        print(f"É Multijogador? {'Sim' if self.multiplayer else 'Não'}")
        print(f"Nota: {self.note}")

####Primeiro Jogo###
game1 = Game("The Legend of Zelda: Breath of the Wild", 2017, False, 9.5)
game1.technical_sheet()