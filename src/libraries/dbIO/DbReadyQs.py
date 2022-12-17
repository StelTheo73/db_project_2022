import sqlite3

class DbReadyQs:

    ## Static Variables
    DB_PATH = './src/data/database.db'
    db = sqlite3.connect(DB_PATH)

    def format(cursor: object):
        "This function formats the outputs from the database for the GUI"
        # return {entry[0]:entry[1] for entry in cursor}
        return dict(cursor)

    def matches_for_each_team():
        cursor = DbReadyQs.db.execute("SELECT team_name, count(match_id) FROM team, participation \
            WHERE team_name=home_team OR team_name=away_team GROUP BY team_name ORDER BY team_name")
        return DbReadyQs.format(cursor)

    def scored_goals_for_each_team():
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

    def ties_for_each_team():
        cursor = DbReadyQs.db.execute("SELECT team_name, count(match.match_id) FROM team, participation, match \
            WHERE participation.match_id=match.match_id AND \
            (team_name=home_team AND home_team_goals=away_team_goals) \
            GROUP BY team_name ORDER BY count(match.match_id) DESC")
        return DbReadyQs.format(cursor)

    def defeats_for_each_team():
        cursor = DbReadyQs.db.execute("SELECT team_name, count(match.match_id) FROM team, participation, match \
            WHERE participation.match_id=match.match_id AND \
            ((team_name=home_team AND home_team_goals<away_team_goals) OR (team_name=away_team AND home_team_goals>away_team_goals)) \
            GROUP BY team_name ORDER BY count(match.match_id) DESC")
        return DbReadyQs.format(cursor)
    
    def points_for_each_team():
        wins, ties = DbReadyQs.wins_for_each_team(), DbReadyQs.ties_for_each_team()
        points = lambda team: 3*wins[team] + 1*ties[team]
        return {team:points(team) for team in ties}
        



for func in list(DbReadyQs.__dict__.keys())[4:-3]:
    print("Function:",func, "\nOutput:", DbReadyQs.__dict__[func](), "\n")
