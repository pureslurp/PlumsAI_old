import requests
from datetime import datetime


def format_date(str):
    m = str[5:7]
    d = str[-2:]
    y = str[:4]
    return convert_date(f"{m}/{d}/{y}")

def get_day_of_week_iso(date_str):
    """
    Returns the day of the week for a given date in YYYY-MM-DD format.

    :param date_str: A string representing a date in YYYY-MM-DD format.
    :return: The day of the week as a string (e.g., 'Monday').
    """
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        return date.strftime('%A')  # Returns the full name of the day
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

def convert_date(date_str):
    # Parse the date string into a datetime object
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")

    # Format the datetime object to the desired output
    formatted_date = date_obj.strftime("%B %d, %Y")

    return formatted_date

# An api key is emailed to you when you sign up to a plan
# Get a free API key at https://api.the-odds-api.com/
API_KEY = '6a5d3c6ab9dc96538e9b9b9def1ab880'

SPORT = 'americanfootball_nfl' # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports

REGIONS = 'us' # uk | us | eu | au. Multiple can be specified if comma delimited

MARKETS = 'spreads,totals' # h2h | spreads | totals. Multiple can be specified if comma delimited

ODDS_FORMAT = 'decimal' # decimal | american

DATE_FORMAT = 'iso' # iso | unix

BOOKMAKER = "draftkings"

class Matchup:
    def __init__(self, game):
        self.game = game
        self.home_team = game['home_team']
        self.away_team = game['away_team']
        self.start_time = game['commence_time'][:10]

    @property
    def spread(self):
        for book in game["bookmakers"]:
            for market in book['markets']:
                if market['key'] == 'spreads':
                    return abs(float(market['outcomes'][0]['point']))

    @property
    def favorite(self):
        for book in game["bookmakers"]:
            for market in book['markets']:
                if market['key'] == 'spreads':
                    if market['outcomes'][0]['point'] < 0:
                        return market['outcomes'][0]['name']
                    else:
                        return market['outcomes'][1]['name']

    @property
    def underdog(self):
        for book in game["bookmakers"]:
            for market in book['markets']:
                if market['key'] == 'spreads':
                    if market['outcomes'][0]['point'] < 0:
                        return market['outcomes'][1]['name']
                    else:
                        return market['outcomes'][0]['name']

    @property
    def ou(self):
        for book in game["bookmakers"]:
            for market in book['markets']:
                if market['key'] == 'totals':
                    return float(market['outcomes'][0]['point'])

    @property
    def info(self):
        print(self.start_time)
        return f"On {get_day_of_week_iso(self.start_time)} {format_date(self.start_time)}, the {self.away_team} play at the {self.home_team} where the spread is {self.underdog} {self.spread} points and the over/under is {self.ou}."
        # This means the {self.favorite} are projected to win (also referred to as favorites) by {self.spread} points and the {self.underdog} are projected to lose (also referred to as underdogs) by {self.spread} points. The over/under is {self.ou}, which means the total score from each team is projected to be {self.ou}.



odds_response = requests.get(
    f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds',
    params={
        'api_key': API_KEY,
        'regions': REGIONS,
        'markets': MARKETS,
        'oddsFormat': ODDS_FORMAT,
        'dateFormat': DATE_FORMAT,
        'bookmakers': BOOKMAKER,
        'commenceTimeFrom' : "2024-09-09T00:00:00Z",
        'commenceTimeTo': "2024-12-10T00:00:00Z"
    }
)

games_list = []

if odds_response.status_code != 200:
    print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')

else:
    odds_json = odds_response.json()
    print('Number of events:', len(odds_json))
    for game in odds_json:
        matchup = Matchup(game)
        print(matchup.info)
        games_list.append(matchup.info)

    with open('characters/ashley_knowledge/NFL/2024/future_games_odds_list.txt', 'w') as f:
        for line in games_list:
            f.write(f'"{line}",\n')

    # Check the usage quota
    print('Remaining requests', odds_response.headers['x-requests-remaining'])
    print('Used requests', odds_response.headers['x-requests-used'])