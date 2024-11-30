import pandas as pd
import urllib.request
from datetime import datetime

# url = "https://www.footballdb.com/games/index.html"
url = 'https://www.pro-football-reference.com/years/2024/games.htm'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

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

for table in df:
    print(table)
    table["Date"] = table["Date"].apply(lambda x: fix_date(x))
    # for index, row in table.iterrows():
    #     if past_date(row['Date']):
    #         print(f"On {row['Date']} the {row['Visitor']}'s played the {row['Home']}")
    #     else:
    #         print(f"On {row['Date']} the {row['Visitor']}'s are going to play the {row['Home']}")