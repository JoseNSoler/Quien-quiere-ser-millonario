""" Question object declaration file """
from datetime import datetime
from pymongo import MongoClient


class Question:
    """ Question section """
    def __init__(self, quest, ans, wrong):
        """
        Initialization for class with:
        'quest' = question to be used - <str>
        'ans' = answer for previous 'quest' - <str>
        'wrong' = array with 3 decoy questions - <str>
        """
        self.quest = quest
        self.ans = ans
        self.wrong = wrong


class User:
    """ User declaration """
    def __init__(self, name):

        self.name = name
        self.date = datetime.now()
        self._score = 0

    def save(self, records):
        """" Method for saving user """
        print("Guardando nombre y puntaje del usuario")
        records.insert_one(self.__dict__)

    @property
    def score(self):
        """ Public getter score """
        return self._score

    @score.setter
    def score(self, value):
        """ Public setter score """
        self._score = value
