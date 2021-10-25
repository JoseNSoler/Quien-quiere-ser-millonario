""" Custom printer for game execution """
import random
from pymongo import MongoClient
import json

# Connection to MongoDB with previous players score
url = "mongodb+srv://public:test@database.j4esf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)

# Database name = "players_db" and records name = "players_records"
db = client.get_database('players_db')
records = db.players_records

def printPlayers():
    # Print previous users scores
    print("JUGADORES PREVIOS:\n")

    for user in list(records.find()):
        print(">NOMBRE: {}, SCORE: {} \n____________________________\n\n"
        .format(
            user['name'],
            user['_score']
        ))

def printWin(user):
    # Formated win print with current user information
    print(
"""
_________________________________________________________
|                                                       |
|   FELICIDADES!!, HA GANADO EL JUEGO                   |
|                                                       |
|   NOMBRE: {}
|   PUNTAJE FINAL: ${}
|                                                       |
|_______________________________________________________|
""".format(getattr(user, "name"), getattr(user, "score"))
    )
    user.save(records)
    exit()


def printEnd(user):
    # Formated surrender print with current end information
    print(
"""
-- FIN DEL JUEGO --

_______________________
Nombre: {}
Puntaje: {}
""".format(getattr(user, "name"), getattr(user, "score"))
    )
    user.save(records)
    exit()

def printFormat(classQuest, user, level):
    # Formated print with current obj question
    ans = [
        getattr(classQuest, "ans"),
        getattr(classQuest, "wrong")[0],
        getattr(classQuest, "wrong")[1],
        getattr(classQuest, "wrong")[2]
    ]

    ans = [value for value in random.sample(ans,len(ans))]

    print(
        """

NIVEL ACTUAL= -{}-  PUNTAJE ACTUAL= -${}-

_______________________________________________________...
|
| {}
|______________________________________________________...


|A. {}                               
|_______________________________________|

|B. {}
|_______________________________________|

|C. {}
|_______________________________________|

|D. {}
|_______________________________________|


        """.format(
            level,
            getattr(user, "score"),
            getattr(classQuest, "quest"),
            ans[0],
            ans[1],
            ans[2],
            ans[3])
    )

    return ans
