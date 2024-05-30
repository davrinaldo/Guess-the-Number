"""
MIT License

Copyright (c) [2024] [David Felipe Rinaldo]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import random


class GuessTheNumber:
    """Classe para o jogo 'Adivinhe o Número'."""

    MESSAGE_DIFFICULTY = """
\033[1;33mEscolha a dificuldade, 1 Fácil, 2 Médio ou 3 difícil!\033[m
Digite 1, 2 ou 3 para continuar:"""

    MESSAGE_DIFFICULTY_ERROR = """
\033[1;31mDigite apenas 1, 2 ou 3 para selecionar uma Dificuldade!\033[m"""

    MESSAGE_NUMBER_ERROR = """
\033[1;31mDIGITE APENAS NÚMEROS ENTRE 1 E"""

    MSG_GUESS = 'Digite seu Palpite: '

    def __init__(self):
        """Inicializa a classe GuessTheNumber."""

        self.max_num = 3
        self.max_num = (self.get_user_number(self.MESSAGE_DIFFICULTY)*20) // 2
        self.secret_number = self.generate_number_secret()
        self.attempts = 0
        self.game_play()

    def get_user_number(self, prompt):
        """Solicita ao usuário um número de acordo com o prompt fornecido."""

        while True:
            try:
                number = int(input(prompt))
                if self.validate_user_number(number):
                    return number
            except ValueError:
                print(self.MESSAGE_NUMBER_ERROR, f'{self.max_num}!\033[m')

    def validate_user_number(self, number):
        """Valida se o número fornecido pelo usuário está dentro dos limites"""

        if 1 <= number <= self.max_num:
            return True
        else:
            print(self.MESSAGE_NUMBER_ERROR, f'{self.max_num}!\033[m')
            return False

    def generate_number_secret(self):
        """Gera um número secreto dentro do intervalo de dificuldade."""
        return random.randint(1, self.max_num)

    def game_play(self):
        """Inicia o jogo 'Adivinhe o Número'."""

        print(f'\n\033[1;35mTENTE UM NÚMERO ENTRE 1 E {self.max_num}\033[m\n')

        while True:
            guess = self.get_user_number(self.MSG_GUESS)
            self.attempts += 1

            if guess == self.secret_number:
                print('Parabéns! Você acertou o número secreto!')
                break
            elif guess < self.secret_number:
                print('\033[1;36mTente um número Maior.\033[m')
            else:
                print('\033[1;36mTente um número Menor.\033[m')

        print(f'Você acertou o número secreto em {self.attempts} tentativas.')
        return self.attempts


game = GuessTheNumber()
