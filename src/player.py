# src/player.py
class Player:
    """Classe que representa um jogador no jogo 'Adivinhe o Número'."""

    def __init__(self):
        """Inicializa um novo jogador com nome e uma contagem de tentativas."""
        self.name = self.input_name()
        self.attempts = 0

    def input_name(self):
        return input('Digite seu nome: ')

    def increment_attempts(self):
        """Incrementa a contagem de tentativas do jogador."""
        self.attempts += 1
