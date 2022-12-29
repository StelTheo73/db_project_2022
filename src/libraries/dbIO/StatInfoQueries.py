import sqlite3
if __name__ == "__main__":
    from DbQueries import QuerySelector
else:
    from libraries.dbIO.DbQueries import QuerySelector

class StatInfoQueries(object):
    
    ## Static Variables
    DB_PATH = './src/data/database.db'
    db = sqlite3.connect(DB_PATH)

    @staticmethod
    def get_players_stats():
        stat_types = QuerySelector.getStatsTypes()
        stat_list_dict = []
        for stat_type in stat_types:
            stat_list_dict.append(StatInfoQueries.get_stat_for_players_by_type(stat_type))
        stat_dict = {}

        stat_type_index = 0
        for stat_list in stat_list_dict:
            stat_type = stat_types[stat_type_index]
            for player_stat in stat_list:
                    player_id = player_stat["player_id"]
                    stat_number = player_stat[stat_type]
                    if player_id not in stat_dict.keys():
                        stat_dict[player_id] = {}
                        stat_dict[player_id]["team_name"] = player_stat["team_name"]
                        stat_dict[player_id]["player_id"] = player_id
                        stat_dict[player_id]["surname"] = player_stat["surname"]
                        stat_dict[player_id]["name"] = player_stat["name"]
                        stat_dict[player_id]["position"] = player_stat["position"]
                    stat_dict[player_id][stat_type] = stat_number
            stat_type_index+=1
            
        return stat_dict

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
        referees_list = []
        [ referees_list.append(cursor) for cursor in (
            StatInfoQueries.db.execute("SELECT type, surname, name, nationality, referee.referee_id, referee.people_id, tel, birthdate \
                                        FROM referee, people \
                                        WHERE referee.people_id = people.people_id \
                                        ORDER BY type, surname, name")
        )]
        referees_list_dict = []
        for referee in referees_list:
            referee_dict =  {
                "type"        : referee[0],
                "surname"     : referee[1],
                "name"        : referee[2],
                "nationality" : referee[3],
                "player_id"   : referee[4],
                "people_id"   : referee[5],
                "telephone"   : referee[6],
                "birthdate"   : referee[7]
            }
            referees_list_dict.append(referee_dict)
        return referees_list_dict

    @staticmethod
    def get_matches_info():
        pass

    @staticmethod
    def get_stat_for_players_by_type(stat_type):
        players_list = []
        [ players_list.append(cursor) for cursor in (
            StatInfoQueries.db.execute("SELECT team_name, surname, name, position, player.player_id, count(stat_name) as goals\
                                        FROM player, people, statistic \
                                        WHERE player.player_id = statistic.player_id AND player.people_id = people.people_id AND stat_name = ?\
                                        GROUP BY player.player_id \
                                        ORDER BY team_name, surname, name, player.player_id", [stat_type])
        )]
        players_list_dict = []
        for player in players_list:
            player_dict =  {
                "team_name"   : player[0],
                "surname"     : player[1],
                "name"        : player[2],
                "position"    : player[3],
                "player_id"   : player[4],
                stat_type     : player[5],
            }
            players_list_dict.append(player_dict)
        return players_list_dict

if __name__ == "__main__":
    print(StatInfoQueries.get_players_stats())