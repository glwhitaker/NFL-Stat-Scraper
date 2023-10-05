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
for matchup in matchups:
    date = matchup.find('tr',{'class':'date'}).td.string

    winner = matchup.find('tr',{'class':'winner'})
    loser = matchup.find('tr',{'class':'loser'})
    
    print(date)
    print(winner.td.string + " - " + winner.td.next_sibling.next_sibling.string)
    print(loser.td.string + " - " + loser.td.next_sibling.next_sibling.string)
    print()




