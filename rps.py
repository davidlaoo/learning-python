"""
// Rock Paper Scissors CLI game made in Python //
author: davidlao (n3x4z @ GitHub)

objective: Practice learning Python
"""

# imports
import random
from enum import Enum

# Player enum
class Player(Enum):
    CPU = 0
    HUMAN = 1
    TIE = 2

class Choice(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

def generate_rps() -> dict:
    cpu_choice: int = random.randint(0,2)
    human_choice: int = random.randint(0,2)

    choices: dict = {"cpu": Choice(cpu_choice), "human": Choice(human_choice)}
    return choices

def play_rps() -> dict:
    game: dict = generate_rps()
    winner: Player = Player.TIE

    if game["cpu"] == Choice.ROCK and game["human"] == Choice.SCISSORS:
        winner = Player.CPU
    elif game["cpu"] == Choice.ROCK and game["human"] == Choice.PAPER:
        winner = Player.HUMAN
    elif game["cpu"] == Choice.PAPER and game["human"] == Choice.SCISSORS:
        winner = Player.HUMAN
    elif game["cpu"] == Choice.PAPER and game["human"] == Choice.ROCK:
        winner = Player.CPU
    elif game["cpu"] == Choice.SCISSORS and game["human"] == Choice.ROCK:
        winner = Player.HUMAN
    elif game["cpu"] == Choice.SCISSORS and game["human"] == Choice.PAPER:
        winner = Player.CPU

    return {"winner": winner, "game": game}

def main():
    winner, game = play_rps().values()
    print(winner, "has won in", game)

main()