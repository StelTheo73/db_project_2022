import sqlite3

class DbReadyQs:

    ## Static Variables
    DB_PATH = './src/data/database.db'
    db = sqlite3.connect(DB_PATH)

    def format(cursor: object):
        "This function formats the outputs from the database for the GUI"
        return list(cursor)

    def matches_for_each_team():
        cursor = DbReadyQs.db.execute("SELECT team_name, count(match_id) FROM team, participation \
            WHERE team_name=home_team OR team_name=away_team GROUP BY team_name ORDER BY team_name")
        return DbReadyQs.format(cursor)

    def goals_for_each_team():
        "goals that each team scored"
        cursor = DbReadyQs.db.execute("SELECT team_name, sum(goals) FROM \
            (SELECT team_name, sum(home_team_goals) AS goals FROM team, participation, match \
                WHERE team_name=home_team AND participation.match_id=match.match_id GROUP BY team_name \
            UNION SELECT team_name, sum(away_team_goals) AS goals FROM team, participation, match \
                WHERE team_name=away_team AND participation.match_id=match.match_id GROUP BY team_name) \
            GROUP BY team_name")
        return DbReadyQs.format(cursor)

    def conceded_goals_for_each_team():
        "goals that were scored to each team"
        cursor = DbReadyQs.db.execute("SELECT team_name, sum(goals) FROM \
            (SELECT team_name, sum(away_team_goals) AS goals FROM team, participation, match \
                WHERE team_name=home_team AND participation.match_id=match.match_id GROUP BY team_name \
            UNION SELECT team_name, sum(home_team_goals) AS goals FROM team, participation, match \
                WHERE team_name=away_team AND participation.match_id=match.match_id GROUP BY team_name) \
            GROUP BY team_name")
        return DbReadyQs.format(cursor)

    def wins_for_each_team():
        cursor = DbReadyQs.db.execute("SELECT team_name, count(match.match_id) FROM team, participation, match \
            WHERE participation.match_id=match.match_id AND \
            ((team_name=home_team AND home_team_goals>away_team_goals) OR (team_name=away_team AND home_team_goals<away_team_goals)) \
            GROUP BY team_name ORDER BY count(match.match_id) DESC")
        return DbReadyQs.format(cursor)



print(DbReadyQs.goals_for_each_team())
