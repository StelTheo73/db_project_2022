## IMPORTANT: Run while in folder 'DB_PROJECT_2022' (for the paths)
## Run pyw .\src\db\DBinit.py to initialise without printing

import sqlite3, os
DB_PATH = './src/data/database.db'
SQL_PATH = './src/data/DBCreationScript.sql'

# DELETE ALL DATABASE for initialization purposes
if os.path.exists(DB_PATH): os.remove(DB_PATH)

# CREATE AND CONNECT DB
db = sqlite3.connect(DB_PATH)

# EXECUTE THE EXTERNAL SQL SCRIPT
with open(SQL_PATH, 'r') as sql_file:
    db.executescript(sql_file.read())
db.commit()


## TODO: GENERATE RANDOM INPUTS

# # TEST OUTPUTS

# print("\nPeople:")
# [print(person) for person in db.execute("SELECT * FROM people")]
# print("\nPlayers:")
# [print(player) for player in db.execute("SELECT * FROM player")]
# print("\nReferees:")
# [print(referee) for referee in db.execute("SELECT * FROM referee")]
# print("\nMatch Controls by refs:")
# [print(control) for control in db.execute("SELECT * FROM gameControl")]
# print("\nPlayers' Statistics:")
# [print(stat) for stat in db.execute("SELECT * FROM statistic")]
# print("\nClubs:")
# [print(club) for club in db.execute("SELECT * FROM club")]
# print("\nMatches:")
# [print(match) for match in db.execute("SELECT * FROM match")]
# print("\nParticipations:")
# [print(participation) for participation in db.execute("SELECT * FROM participation")]

db.close()
