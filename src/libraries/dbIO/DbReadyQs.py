import sqlite3
from DbQueries import QuerySelector as QC

class DbReadyQs:

    ## Static Variables
    DB_PATH = './src/data/database.db'
    db = sqlite3.connect(DB_PATH)

    def get_board():
        output = {team:{} for team in QC.getTeams()}
        
        for team in output:
            team = output[team]
            team['wins'] = team['defeats'] = team['ties'] = 0

        functions:list(function) = [DbReadyQs.__dict__[func] for func in list(DbReadyQs.__dict__.keys())[5:-3]]
        for func in functions:
            value:dict = func()
            for team in value:
                output[team][func.__name__.rstrip("_for_each_team")] = value[team]
        
        return output

    def format(cursor: object):
        "This function formats the outputs from the database for the GUI"
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
        cursor = DbReadyQs.db.execute("SELECT team_name, count(match.match_id) FROM team \
            JOIN participation ON (team_name=home_team OR team_name=away_team) \
            LEFT JOIN match ON participation.match_id=match.match_id AND home_team_goals=away_team_goals \
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
        points = lambda team: ties[team] if team not in wins else 3*wins[team] + 1*ties[team]
        return DbReadyQs.format([(team,points(team)) for team in wins])


if __name__ == "__main__":
    board = DbReadyQs.get_board()
    for tm in board:
        # Check that all have same length.. Bug in wins/defeats for teams that have 0 of them
        print(tm, len(board[tm]), board[tm])

