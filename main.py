from classes import matchup
from bs4 import BeautifulSoup
import requests

URL = "https://www.pro-football-reference.com/"

r = requests.get(URL)

webpage = BeautifulSoup(r.content, "lxml")

# find weekly results tables
weeklyResults = webpage.find('div',{'id':'scores'})

# list of individual matchups
matchups = weeklyResults.find_all('div',{'class':'game_summary expanded nohover'})

#print each matchup
for game in matchups:
    myMatch = matchup.Matchup(game)
    
    print(myMatch)




