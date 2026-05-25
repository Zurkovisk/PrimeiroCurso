class Game:
    name = ""
    year = 0
    multiplayer = False
    note = 0

####Primeiro Jogo###
game1 = Game()
game1.name = "The Legend of Zelda: Breath of the Wild"
game1.year = 2017
game1.multiplayer = False
game1.note = 9.5

print("###Dados do Jogo 1###")
print(f"Nome: {game1.name}")
print(f"Ano: {game1.year}")
print(f"Multijogador: {game1.multiplayer}")
print(f"Nota: {game1.note}")

####Segundo Jogo###
game2 = Game()
game2.name = "Fortnite"
game2.year = 2017
game2.multiplayer = True
game2.note = 8.0

print("###Dados do Jogo 2###")
print(f"Nome: {game2.name}")
print(f"Ano: {game2.year}")
print(f"Multijogador: {game2.multiplayer}")
print(f"Nota: {game2.note}")