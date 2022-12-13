# no of matches for each team
SELECT team_name, count(match_id) FROM team, participation WHERE team_name = home_team OR team_name = away_team GROUP BY team_name ORDER BY team_name



# no of goals for each team
no_of_home_goals =
SELECT team_name, sum(home_team_goals) FROM team, participation, match WHERE team_name = home_team AND participation.match_id = match.match_id GROUP BY team_name ORDER BY team_name

no_of_away_goals =
SELECT team_name, sum(away_team_goals) FROM team, participation, match WHERE team_name = away_team AND participation.match_id = match.match_id GROUP BY team_name ORDER BY team_name

no_of_total_goals = no_of_home_goals + no_of_away_goals



# no of conceded goals for each team
conceded_away = 
SELECT team_name, sum(home_team_goals) FROM team, participation, match WHERE team_name = away_team AND participation.match_id = match.match_id GROUP BY team_name ORDER BY team_name

conceded_home = 
SELECT team_name, sum(away_team_goals) FROM team, participation, match WHERE team_name = home_team AND participation.match_id = match.match_id GROUP BY team_name ORDER BY team_name

no_of_conceded_goals = conceded_home + conceded_away

