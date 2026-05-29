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
        print(f"Nome do Jogo: {self.name}")
        print(f"Ano de Lançamento: {self.year}")
        print(f"É Multijogador? {'Sim' if self.multiplayer else 'Não'}")
        print(f"Nota: {self.note}\n")


class GameStudio:
    def __init__(self, name=""):
        self.name = name
        self.game = []

    def add_game(self, game):  # FIXED: removed (game) from parameters
        self.game.append(game)

    def evaluate_studio_quality(self):
        total_notes = sum(game.note for game in self.game)
        num_games = len(self.game)
        if num_games == 0:
            print(
                f"O estúdio {self.name} ainda não lançou nenhum jogo"
            )  # FIXED: typo and capitalization
        else:
            average_note = total_notes / num_games
            print(
                f"A avaliação média dos jogos do estúdio {self.name}: {average_note:.2f}"
            )


game1 = Game("The Legend of Zelda", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)
game3 = Game("The Last of Us II", 2020, False, 9.0)  # FIXED: added missing comma

studio = GameStudio("Awesome Games")
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)

studio.evaluate_studio_quality()
