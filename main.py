""" Main point execution "Quien quiere ser millonario" """
import json
import random
import re
import simplejson
import time

from src.objs import Question, User
from src.utilities import clear, checkAns, selectionMode
from src.Printer import printFormat, printEnd, printWin
from types import SimpleNamespace


def game(data, level, user):
    """ Game execution """
    clear()
    if level <= 5:
        questLevel = [x.get("resultados") for x in data if x.get("nivel") == level]

        # Always obtain a random question, and the already used ones, will not appear again in the execution
        for x in random.sample(data[level - 1]["resultados"], len(data[level - 1]["resultados"])):

            # Create current quest as an object
            currQuest = Question(x.get("quest"), x.get("ans"), x.get("wrong"))

            # Formated print for visual help
            ans = printFormat(currQuest, user, level)

            # Check given answer with position of answer
            res = checkAns(1)

            # On -1 in "res", user has given up
            if res == -1:
                print("RETIRADA VOLUNTARIA DEL JUGADOR")
                printEnd(user)

            # Compares given answer with real answer on class CurrentQuestion
            if (str(ans[res]) == str(getattr(currQuest, "ans"))):
                # Increments actual score on user object and global level
                setattr(user, "score", (getattr(user, "score")) + (175 * level))

                level += 1
                # If the answer is correct, we use recursion to repeat again same steps with a new level
                game(data, level, user)
            else:
                # Invalid answer, end of the game
                clear()
                print("RESPUESTA INCORRECTA")
                printEnd(user)
    else:
        # When level is 5, the user has winned the current game
        clear()
        printWin(user)

def main():
    while 1:
        clear()
        """
        Check for user desired mode:
        A. Enter username and start game on level 1- "name"
        B. Print current players on MongoDB
        """
        name = selectionMode()
        level = 1
        user1 = User(name)

        with open('data.json', 'r', encoding='utf-8') as fileJson:
            # json.dump(quest1.__dict__, fileJson, indent=4)
            data = json.load(fileJson)

            game(data, level, user1)

        exit()

if __name__ == "__main__":
    main()