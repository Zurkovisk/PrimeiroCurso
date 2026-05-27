class Game:
    def __init__(self, name="", year=0, multiplayer=False, note=0):
        self.name = name
        self.year = year
        self.multiplayer = multiplayer
        self.note = note

    def __str__(self):
        return f"Nome: {self.name}, Ano: {self.year}, Multijogador: {self.multiplayer}, Nota: {self.note}"

####Primeiro Jogo###
game1 = Game("The Legend of Zelda: Breath of the Wild", 2017, False, 9.5)
print("###Dados do Jogo 1###")
print(f"\nNome do Jogo: {game1.name}\nAno de Lançamento: {game1.year}\nÉ Multijogador? {'Sim' if game1.multiplayer else 'Não'}\nNota: {game1.note}")
