import requests

def format_date(str):
    m = str[5:7]
    d = str[-2:]
    y = str[:4]
    return f"{m}/{d}/{y}"

# An api key is emailed to you when you sign up to a plan
# Get a free API key at https://api.the-odds-api.com/
API_KEY = '6a5d3c6ab9dc96538e9b9b9def1ab880'

SPORT = 'americanfootball_nfl' # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports

REGIONS = 'us' # uk | us | eu | au. Multiple can be specified if comma delimited

MARKETS = 'totals' # h2h | spreads | totals. Multiple can be specified if comma delimited

ODDS_FORMAT = 'decimal' # decimal | american

DATE_FORMAT = 'iso' # iso | unix

BOOKMAKER = "draftkings"


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# First get a list of in-season sports
#   The sport 'key' from the response can be used to get odds in the next request
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# sports_response = requests.get(
#     'https://api.the-odds-api.com/v4/sports', 
#     params={
#         'api_key': API_KEY
#     }
# )


# if sports_response.status_code != 200:
#     print(f'Failed to get sports: status_code {sports_response.status_code}, response body {sports_response.text}')

# else:
#     print('List of in season sports:', sports_response.json())



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# Now get a list of live & upcoming games for the sport you want, along with odds for different bookmakers
# This will deduct from the usage quota
# The usage quota cost = [number of markets specified] x [number of regions specified]
# For examples of usage quota costs, see https://the-odds-api.com/liveapi/guides/v4/#usage-quota-costs
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

odds_response = requests.get(
    f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds',
    params={
        'api_key': API_KEY,
        'regions': REGIONS,
        'markets': MARKETS,
        'oddsFormat': ODDS_FORMAT,
        'dateFormat': DATE_FORMAT,
        'bookmakers': BOOKMAKER,
        'commenceTimeFrom' : "2024-09-09T00:00:00Z"
    }
)

games_list = []

if odds_response.status_code != 200:
    print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')

else:
    odds_json = odds_response.json()
    print(odds_json)
    print('Number of events:', len(odds_json))
    for game in odds_json:
        home_team = game['home_team']
        away_team = game['away_team']
        start_time = format_date(game['commence_time'][:10])
        for book in game["bookmakers"]:
            for market in book['markets']:
                for g in market['outcomes']:
                    print(f"On {start_time}, the {away_team} play at the {home_team} where the spread is {g['name']} {g['point']} on DraftKings")
                    games_list.append(f"On {start_time}, the {away_team} play at the {home_team} where the spread is {g['name']} {g['point']} on DraftKings")
                    break
    
    with open('characters/ashley_knowledge/NFL/future_games_odds_list.txt', 'w') as f:
        for line in games_list:
            f.write(f'"{line}",\n')
    
    # Check the usage quota
    print('Remaining requests', odds_response.headers['x-requests-remaining'])
    print('Used requests', odds_response.headers['x-requests-used'])