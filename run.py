# run.py
from src.game_logic import GuessTheNumber
from src.player import Player

if __name__ == "__main__":
    print('\n\033[1;34mGUESS THE NUMBER!\033[m\n')
    player = Player()
    game = GuessTheNumber(player)
