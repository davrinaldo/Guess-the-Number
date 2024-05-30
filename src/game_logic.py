import random


class GuessTheNumber:
    """Classe para o jogo 'Adivinhe o Número'."""

    MESSAGE_DIFFICULTY = """
Escolha a dificuldade, 1 Fácil, 2 Médio ou 3 difícil!
Digite 1, 2 ou 3 para continuar:"""

    MESSAGE_DIFFICULTY_ERROR = """
\033[1;31mDigite apenas 1, 2 ou 3 para selecionar uma Dificuldade!\033[m"""

    MESSAGE_NUMBER_ERROR = """
\033[1;31mDIGITE APENAS NÚMEROS!\033[m"""

    def __init__(self):
        self.max_num = 3
        self.max_num = self.get_user_number(self.MESSAGE_DIFFICULTY)
        self.secret_number = self.generate_number_secret()
        self.attempts = 0

    def get_user_number(self, prompt):
        while True:
            try:
                number = int(input(prompt))
                if self.validate_user_number(number):
                    return number
            except ValueError:
                print(self.MESSAGE_NUMBER_ERROR)

    def validate_user_number(self, number):
        if 1 <= number <= self.max_num:
            return True
        else:
            print(self.MESSAGE_DIFFICULTY_ERROR)
            return False

    def generate_number_secret(self):
        return random.randint(1, self.max_num)


game = GuessTheNumber()
