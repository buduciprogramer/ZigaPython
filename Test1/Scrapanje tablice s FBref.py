import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Učitaj stranicu i obradi HTML
url = "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"
html = requests.get(url).text.replace("<!--", "").replace("-->", "")
soup = BeautifulSoup(html, "html.parser")

# 2. Pronađi tabelu sa rasporedom utakmica
table = soup.find("table", id="sched_2025-2026_9_1")

if table:
    df = pd.read_html(str(table))[0]
    df.to_csv("premier_league_2025_26_raspored.csv", index=False)
    print(" Raspored je spremljen kao 'premier_league_2025_26_raspored.csv'")

    # 3. Filtriraj utakmice gdje igra Arsenal
    arsenal_matches = df[(df['Home'] == 'Arsenal') | (df['Away'] == 'Arsenal')]

    # 4. Ispiši u terminalu
    print("\n Arsenalov raspored:")
    print(arsenal_matches[['Date', 'Time', 'Home', 'Away', 'Score']])

    # 5. Spremi i u poseban fajl (opcionalno)
    arsenal_matches.to_csv("arsenal_raspored_2025_26.csv", index=False)
    print(" Arsenalov raspored spremljen kao 'arsenal_raspored_2025_26.csv'")

else:
    print(" Tabela nije pronađena.")