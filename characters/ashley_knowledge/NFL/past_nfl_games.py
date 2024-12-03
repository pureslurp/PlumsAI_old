import pandas as pd
import urllib.request
from datetime import datetime
import requests
import os



API_KEY = '6a5d3c6ab9dc96538e9b9b9def1ab880'

SPORT = 'americanfootball_nfl' # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports

REGIONS = 'us' # uk | us | eu | au. Multiple can be specified if comma delimited

MARKETS = 'spreads,totals' # h2h | spreads | totals. Multiple can be specified if comma delimited

ODDS_FORMAT = 'decimal' # decimal | american

DATE_FORMAT = 'iso' # iso | unix

BOOKMAKER = "draftkings"

url = 'https://www.pro-football-reference.com/years/2024/games.htm'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

class Team:
    def __init__(self, past_scores: pd.Series, past_odds: pd.DataFrame, home:bool = True):
        self.name = past_odds['home_team'] if home else past_odds['away_team']
        self.past_scores = past_scores
        self.game = past_odds
        self.date = past_scores['Date']
        self.week = past_scores['Week']

    @property
    def winner(self):
        # try:
        if self.name == self.past_scores['Winner/tie']:
            return True
        else:
            return False
        # except:
        #     return ValueError("unable to extract winner, game likely hasn't happened yet")

    @property
    def score(self):
        try:
            if self.winner:
                return int(self.past_scores['PtsW'])
            else:
                return int(self.past_scores['PtsL'])
        except:
            return ValueError("unable to extract score, game likely hasn't happened yet")



    @property
    def spread(self):
        for odds in self.game["bookmakers"][0]['markets']:
            if odds['key'] == 'spreads':
                if self.name == odds['outcomes'][0]['name']:
                    return float(odds['outcomes'][0]['point'])
                else:
                    return float(odds['outcomes'][1]['point'])

    @property
    def get_ou(self):
        for odds in self.game["bookmakers"][0]['markets']:
            if odds['key'] == 'totals':
                return odds['outcomes'][0]['point']

class Matchup:
    def __init__(self, home_team: Team, away_team: Team):
        self.home_team = home_team
        self.away_team = away_team
        self.covered = self.covering_team
        self.total = home_team.score + away_team.score
        self.ou = home_team.get_ou

    @property
    def covering_team(self):
        if self.home_team.score + self.home_team.spread < self.away_team.score:
            return self.away_team
        else:
            return self.home_team

    def did_cover(self, team):
        if team == self.covering_team:
            return "covered"
        else:
            return "did not cover"

    @property
    def winner(self):
        if self.home_team.winner:
            return self.home_team
        else:
            return self.away_team

    @property
    def loser(self):
        if self.away_team.winner:
            return self.home_team
        else:
            return self.away_team

    @property
    def underdog(self):
        if self.home_team.spread < 0:
            return self.away_team
        else:
            return self.home_team

    @property
    def favorite(self):
        if self.home_team.spread > 0:
            return self.away_team
        else:
            return self.home_team

    @property
    def over_result(self):
        if self.total > self.ou:
            return f"over hit because the teams scored more than {self.total}"
        else:
            return f"under hit because the teams scored less than {self.total}"

    @property
    def score_difference(self):
        return abs(self.home_team.score - self.away_team.score)

    def cover_reason(self, team):
        if team == self.underdog:
            if self.did_cover(team) == 'covered':
                if self.underdog == self.winner:
                    return "won the game outright"
                else:
                    return f"lost by less than {self.underdog.spread}"
            else:
                return f"lost by more than {self.underdog.spread}"
        else:
            if self.did_cover(team) == 'covered':
                return f"won by more than {self.underdog.spread}"
            else:
                if team == self.winner:
                    return f"only won by {self.score_difference}"
                else:
                    return "lost"


    @property
    def info(self):
        return f"On {format_date(self.home_team.date)}, in Week {self.home_team.week} of the 2024 NFL season, the {self.away_team.name} played at the {self.home_team.name}. The {self.winner.name} beat the {self.loser.name} {self.winner.score} to {self.loser.score}. The over/under was {self.ou} and the total score was {self.total}, so the {self.over_result}. The spread of the game was {self.home_team.name} {self.home_team.spread}, which means the {self.underdog.name} were underdogs by {self.underdog.spread} points and the {self.favorite.name} were favorites by {self.underdog.spread} points. The {self.underdog.name} as underdogs {self.did_cover(self.underdog)} the {self.underdog.spread} point spread because they {self.cover_reason(self.underdog)}. The {self.favorite.name} as favorites {self.did_cover(self.favorite)} the {self.underdog.spread} point spread because they {self.cover_reason(self.favorite)}."

def convert_date(date_str):
    # Parse the date string into a datetime object
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")

    # Format the datetime object to the desired output
    formatted_date = date_obj.strftime("%B %d, %Y")

    return formatted_date

def format_date(str):
    m = str[5:7]
    d = str[-2:]
    y = str[:4]
    date = f"{m}/{d}/{y}"
    return convert_date(date)

def past_date(date_string):
    # Parse the input date string
    try:
        input_date = datetime.strptime(date_string, "%m/%d/%Y")
    except ValueError:
        return "Invalid date format. Please use MM/DD/YYYY."

    # Get today's date
    today = datetime.now()

    # Compare dates
    if input_date > today:
        return False
    elif input_date < today:
        return True
    else:
        return True

def fix_date(str):
    return str[:-5]

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')
    df = pd.read_html(html)

table = df[0]
table = table.rename(columns={table.columns[5]: "loc"})
odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/historical/sports/{SPORT}/odds',
            params={
                'api_key': API_KEY,
                'regions': REGIONS,
                'markets': MARKETS,
                'oddsFormat': ODDS_FORMAT,
                'dateFormat': DATE_FORMAT,
                'bookmakers': BOOKMAKER,
                'date' : "2024-09-05T00:00:00Z"
            }
        )

if odds_response.status_code != 200:
    print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')
else:
    odds_json = odds_response.json()

game_list = []
set_list = []
duplicate = False

for index, row in table.iterrows():
    week = row["Week"]
    pfs_winning_team = row["Winner/tie"]
    pfs_losing_team = row["Loser/tie"]
    for game in odds_json['data']:
        api_home_team = game['home_team']
        api_away_team = game['away_team']
        if (pfs_winning_team == api_home_team or pfs_winning_team == api_away_team) and (pfs_losing_team == api_home_team or pfs_losing_team == api_away_team):
            # check if we already covered the game
            for s in set_list:
                if set([api_home_team, api_away_team, row["Date"]]) == set(s):
                    duplicate = True
                    break
                else:
                    duplicate = False
            if duplicate:
                continue
            else:
                # we didn't cover this game yet
                set_list.append([api_home_team, api_away_team, row["Date"]])
                try:
                    matchup = Matchup(Team(row, game, True), Team(row, game, False))
                    game_list.append(matchup.info)
                except:
                    print("future game")
                    break


with open(f'characters/ashley_knowledge/NFL/2024/past_games_results.txt', 'w') as f:
    for line in game_list:
        f.write(f'"{line}",\n')