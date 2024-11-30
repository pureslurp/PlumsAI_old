import requests
from utils import TEAM_DICT
from datetime import datetime
import numpy as np

def convert_date(date_str):
    # Parse the date string into a datetime object
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    
    # Format the datetime object to the desired output
    formatted_date = date_obj.strftime("%B %d, %Y")
    
    return formatted_date

def format_date(str):
    str = str[:10]
    m = str[5:7]
    d = str[-2:]
    y = str[:4]
    date = f"{m}/{d}/{y}"
    return convert_date(date)

API_KEY = '9450ee87d52e4ece9c1784a7768a9bf9'

SEASON = 2024
WEEK = np.arange(1,13,1)

for w in WEEK:
    week_response = requests.get(
        f'https://api.sportsdata.io/v3/nfl/scores/json/ScoresByWeekFinal/{SEASON}/{w}?key={API_KEY}'
    )

    game_list = []

    if week_response.status_code != 200:
        print(f'Failed to get odds: status_code {week_response.status_code}, response body {week_response.text}')

    else:
        week_json = week_response.json()
        for game in week_json:
            spread = game["PointSpread"]
            overunder = game["OverUnder"]
            home_score = game['HomeScore']
            away_score = game["AwayScore"]
            home_team = TEAM_DICT[game['HomeTeam']]
            away_team = TEAM_DICT[game['AwayTeam']]
            total_score = home_score + away_score
            if overunder < total_score:
                ou_result = "over"
            else:
                ou_result = "under"
            if home_score + spread > away_score:
                spread_result = "covered"
            else:
                spread_result = "did not cover"

            info = f"On {format_date(game['Date'])} in Week {w} of the NFL, the {away_team} played at the {home_team}. The final score was {away_team} {away_score} and the {home_team} {home_score}. The over/under was {overunder} and the final score was {total_score}, so the {ou_result} hit. The spread was {home_team} {spread} points, and they {spread_result}."
            game_list.append(info)

    with open(f'characters/ashley_knowledge/NFL/Week{w}.txt', 'w') as f:
        for line in game_list:
            f.write(f'"{line}",\n')