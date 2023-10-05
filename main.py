from classes import matchup
from bs4 import BeautifulSoup
import requests
import csv

URL = "https://www.pro-football-reference.com/"
r = requests.get(URL)
webpage = BeautifulSoup(r.content, "lxml")

file = open('report.csv', 'w')
writer = csv.writer(file)


# find weekly results tables
weeklyResults = webpage.find('div',{'id':'scores'})

# list of individual matchups
matchups = weeklyResults.find_all('div',{'class':'game_summary expanded nohover'})

#print each matchup
for game in matchups:
    myMatch = matchup.Matchup(game)

    writer.writerow([myMatch.away.name, myMatch.away.score])
    writer.writerow([myMatch.home.name, myMatch.home.score])
    writer.writerow([""])




