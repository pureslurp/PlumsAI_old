import requests
from bs4 import BeautifulSoup

# URL constants
WIN_LOSS_URL = "https://www.teamrankings.com/nfl/trends/win_trends/"
ATS_URL = "https://www.teamrankings.com/nfl/trends/ats_trends/"
OVER_UNDER_URL = "https://www.teamrankings.com/nfl/trends/ou_trends/"

# Mapping team city names to full team names with mascots
TEAM_NAME_MAP = {
    "Arizona": "Arizona Cardinals",
    "Atlanta": "Atlanta Falcons",
    "Baltimore": "Baltimore Ravens",
    "Buffalo": "Buffalo Bills",
    "Carolina": "Carolina Panthers",
    "Chicago": "Chicago Bears",
    "Cincinnati": "Cincinnati Bengals",
    "Cleveland": "Cleveland Browns",
    "Dallas": "Dallas Cowboys",
    "Denver": "Denver Broncos",
    "Detroit": "Detroit Lions",
    "Green Bay": "Green Bay Packers",
    "Houston": "Houston Texans",
    "Indianapolis": "Indianapolis Colts",
    "Jacksonville": "Jacksonville Jaguars",
    "Kansas City": "Kansas City Chiefs",
    "Las Vegas": "Las Vegas Raiders",
    "LA Chargers": "Los Angeles Chargers",
    "LA Rams": "Los Angeles Rams",
    "Miami": "Miami Dolphins",
    "Minnesota": "Minnesota Vikings",
    "New England": "New England Patriots",
    "New Orleans": "New Orleans Saints",
    "NY Giants": "New York Giants",
    "NY Jets": "New York Jets",
    "Philadelphia": "Philadelphia Eagles",
    "Pittsburgh": "Pittsburgh Steelers",
    "San Francisco": "San Francisco 49ers",
    "Seattle": "Seattle Seahawks",
    "Tampa Bay": "Tampa Bay Buccaneers",
    "Tennessee": "Tennessee Titans",
    "Washington": "Washington Commanders"
}

def fetch_data(url):
    """Fetch and parse table data from the given URL."""
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve data from {url}: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='tr-table')
    if not table:
        print(f"Could not find the data table on {url}.")
        return None

    rows = table.find_all('tr')[1:]  # Skip the header row
    data = {}
    for row in rows:
        cols = row.find_all('td')
        team_city = cols[0].text.strip()
        record = cols[1].text.strip()
        data[team_city] = record
    return data

def merge_data(win_loss_data, ats_data, over_under_data):
    """Combine data from all sources into a single structure."""
    merged_data = []
    for team_city, win_loss_record in win_loss_data.items():
        full_team_name = TEAM_NAME_MAP.get(team_city, team_city)
        ats_record = ats_data.get(team_city, "N/A")
        over_under_record = over_under_data.get(team_city, "N/A")
        merged_data.append({
            "team_name": full_team_name,
            "win_loss_record": win_loss_record,
            "ats_record": ats_record,
            "over_under_record": over_under_record
        })
    return merged_data

def save_to_file(data, filename="characters/ashley_knowledge/NFL/2024/nfl_team_records.txt"):
    """Write the merged data to a text file."""
    with open(filename, 'w') as file:
        for team in data:
            var = f"{team['team_name']} this season are {team['win_loss_record']} straight up, {team['ats_record']} against the spread, and {team['over_under_record']} against the over under."
            file.write(
                f'"{var}",\n'
            )

if __name__ == "__main__":
    # Fetch data from the three sources
    win_loss_data = fetch_data(WIN_LOSS_URL)
    ats_data = fetch_data(ATS_URL)
    over_under_data = fetch_data(OVER_UNDER_URL)

    if win_loss_data and ats_data and over_under_data:
        # Merge and save data
        merged_data = merge_data(win_loss_data, ats_data, over_under_data)
        save_to_file(merged_data)
        print("NFL team records have been saved to nfl_team_records.txt.")
    else:
        print("Failed to retrieve or merge NFL data.")
