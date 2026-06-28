"""
Rock Paper Scissors CLI game made in Python

author: davidlao (n3x4z @ GitHub)

objective: Practice learning Python
"""
import random
from enum import Enum


class Player(Enum):
    """Identifies between ``CPU``, ``HUMAN`` and ``TIE`` winning states"""
    CPU = 0
    HUMAN = 1
    TIE = 2


class Choice(Enum):
    """Identifies between ``ROCK``, ``PAPER`` and ``SCISSORS`` choices for a participant"""
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


def play_rps(human_choice: Choice) -> dict:
    """
    Generates a game play state of Rock, Paper, Scissors in ``dict`` data
    :param human_choice: A human input :class:`Choice` to append to the computer calculation
    :return: A :class:`dict` in the format {"winner": ..., "game": ...} with a winner :class:`Player` and game state :class:`dict` respectively.``
    """

    # generates a CPU move
    cpu_choice = Choice( random.randint(0, 2) )

    # forms a final game Choice state
    game: dict = {"cpu": cpu_choice, "human": human_choice}

    # tie by default, given no conditions are met
    winner: Player = Player.TIE

    # evaluate generated game state
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

    # return the final game state
    return {"winner": winner, "game": game}


def main():
    # initial banner and instructions
    print("## ROCK, PAPER, SCISSORS ##")
    print("Choose a number from the choices")
    print("Rock (0), Paper (1), Scissors (2)")

    try:
        # request user input
        raw_choice = int(input("> "))

        try:
            # cast into Choice to verify it is a valid play
            choice = Choice(raw_choice)

            # play, then unpack the game's resulting state
            # since the return type is of dict, we unwrap its .values()
            # correspondingly named
            winner, game = play_rps(choice).values()

            # show the winner @ stdout
            if winner == Player.TIE:
                print("TIE! Both players chose the same.")
            elif winner == Player.CPU:
                print("The computer wins... Better luck next time.")
            elif winner == Player.HUMAN:
                print("You win! Congratulations.")

            # show the game state @ stdout
            print("The game was: ", game, end = "\n\n")

            # start again
            main()

        # it's not a valid play (Choice)
        except ValueError:
            print("[ERR]: Your number is not in range. Try again.")
            main()

    # it's not an integer (int). invalid data
    except ValueError:
        print("[ERR]: You must input a number from (0, 1, 2)")

        # Restart the program
        main()

# start the program
main()
