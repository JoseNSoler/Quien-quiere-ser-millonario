""" File with utilities for main-game program """
from os import system, name
from .Printer import printPlayers


def selectionMode(mode=0):
    """ Selection game mode with visual help"""

    print(
"""
<< QUIEN QUIERE SER MILLONARIO >>

Porfavor seleccione una opcion:
________________________________
A. Iniciar juego
B. Ver puntajes actuales por otros jugadores
"""
    )
    # If players chooses to check previous scores, "printPlayers()" is called
    # and returns to starting point
    ans = checkAns(2)

    if ans == 0:
        # Option start game, returns name validated
        name = checkAns(3)
        return name
    else:
        printPlayers()
        return selectionMode(1)

def checkAns(mode=0):
    """ 
    Checks if response is a expected answer

    If not, function will continually ask for correct input information
    """
    
    # Checks for only valid input for current question
    if mode == 1:
        while True:
            res = input("Introduzca su respuesta\no escriba \"rendirse\" para retirarse con su puntaje acumulado actual: >")
            try:
                if res not in ["A", "B", "C", "D", "rendirse"]:
                    raise Exception
            except Exception:
                print("=>ERROR: Respuesta debe ser una letra en mayuscula segun opciones")
                continue
            else:
                break
        # On "rendirse" case, the program return -1
        if res == "rendirse": return -1
        # Returns given answer on translated position
        if res == "A": return 0
        if res == "B": return 1
        if res == "C": return 2
        if res == "D": return 3

    # Checker for mode game
    if mode == 2:
        while True:
            res = input(">")
            try:
                if res not in ["A", "B"]:
                    raise Exception
            except Exception:
                print("=>ERROR: Respuesta debe ser una letra en mayuscula segun opciones")
            else:
                break
        if res == "A": return 0
        if res == "B": return 1
    
    # Checker for valid input username
    if mode == 3:
        while True:
            res = input("Porfavor introduzca su nombre:  >")
            try:
                if len(name) > 15 or (name in [None, ""]):
                    raise Exception
            except Exception:
                print("=>ERROR: 15 Caracteres permitidos")
            else:
                break
        return res


def clear():
    # Clear screen/terminal
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
