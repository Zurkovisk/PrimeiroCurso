# classe generalista ou superclasse
class Game:
    total_games = 0

    def __init__(self, name="", year=0, multiplayer=False, note=0):
        self.name = name
        self.year = year
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1
        self.totalEvaluation = 0
        self.evaluators = 0

    def __str__(self):
        return f"Nome: {self.name}, Ano: {self.year}, Multijogador: {self.multiplayer}, Nota: {self.note}"

    def technical_sheet(self):
        print()
        print(f"\nNome do Jogo: {self.name}")
        print(f"Ano de Lançamento: {self.year}")
        print(f"É Multijogador? {'Sim' if self.multiplayer else 'Não'}")
        print(f"Nota: {self.note}")

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(
            f"A média de avaliação do {self.name} é {(self.totalEvaluation / self.evaluators):.2f}"
        )


# ... existing code ...

game1 = Game("The Legend of Zelda: Breath of the Wild", 2017, False, 9.5)
game2 = Game("Super Mario Odyssey", 2017, True, 9.0)

game1.technical_sheet()
game2.technical_sheet()

game1.evaluate(9.2)
game1.evaluate(9.3)

game2.evaluate(8.8)
game2.evaluate(8.9)

game1.average()
game2.average()


# Exibindo o total de jogos criados
print(f"Total de jogos criados: {Game.total_games}")


# classe derivada ou especializada
class SinglePlayerGame(Game):
    def __init__(self, name="", year=0, note=0, storyline=""):
        super().__init__(name, year, False, note)
        self.storyline = storyline

    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.storyline}\n")


mult_game = Game("Fortnite", 2017, True, 8.0)

sing_game = SinglePlayerGame(
    "The Last of Us 2", 2020, 9.5, "Emocionante história de sobrevivência e vingança"
)
sing_game.technical_sheet()
