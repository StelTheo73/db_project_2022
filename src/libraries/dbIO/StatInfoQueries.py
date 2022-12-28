import sqlite3

class StatInfoQueries(object):
    
    ## Static Variables
    DB_PATH = './src/data/database.db'
    db = sqlite3.connect(DB_PATH)

    @staticmethod
    def get_players_stats():
        goal_dict = StatInfoQueries.get_stat_for_players_by_type("Goal")
        assist_dict = StatInfoQueries.get_stat_for_players_by_type("Assist")
        return goal_dict, assist_dict

    @staticmethod
    def get_players_info():
        players_list = []
        [ players_list.append(cursor) for cursor in (
            StatInfoQueries.db.execute("SELECT team_name, position, surname, name, nationality, player.player_id, player.people_id, tel, birthdate \
                                        FROM player, people \
                                        WHERE player.people_id = people.people_id \
                                        ORDER BY team_name, position, surname, name")
        )]
        players_list_dict = []
        for player in players_list:
            player_dict =  {
                "team_name"   : player[0],
                "position"    : player[1],
                "surname"     : player[2],
                "name"        : player[3],
                "nationality" : player[4],
                "player_id"   : player[5],
                "people_id"   : player[6],
                "telephone"   : player[7],
                "birthdate"   : player[8]
            }
            players_list_dict.append(player_dict)
        return players_list_dict

    @staticmethod
    def get_referees_stats():
        pass

    @staticmethod
    def get_referees_info():
        pass

    @staticmethod
    def get_matches_info():
        pass

    @staticmethod
    def get_stat_for_players_by_type(stat_type):
        players_list = []
        [ players_list.append(cursor) for cursor in (
            StatInfoQueries.db.execute("SELECT player.player_id, count(stat_name) as goals\
                                        FROM player, statistic \
                                        WHERE player.player_id = statistic.player_id AND stat_name = ?\
                                        GROUP BY player.player_id", [stat_type])
        )]
        players_list_dict = []
        for player in players_list:
            player_dict =  {
                "player_id"   : player[0],
                stat_type    : player[1],
            }
            players_list_dict.append(player_dict)
        return players_list_dict

if __name__ == "__main__":
    print(StatInfoQueries.get_players_stats())