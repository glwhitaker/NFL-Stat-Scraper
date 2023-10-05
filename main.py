from bs4 import BeautifulSoup
import requests

URL = "https://www.pro-football-reference.com/teams/"

# Error handling for the HTTP request
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to get data")
    exit()

soup = BeautifulSoup(response.content, "lxml")

# Initialize dictionary for team names and URLs
nameDic = {}

# Locate the table and tbody
teamTable = soup.find("table", {"id": "teams_active"}).find("tbody")

# Populate the dictionary
for team in teamTable.find_all("tr", {"class": ""}):
    tnTag = team.find("th", {"data-stat": "team_name"})
    teamName = tnTag.a.text
    teamUrl = tnTag.a["href"]
    
    nameDic[teamName] = teamUrl


inp = input("Enter a team name: ")

for selection in nameDic.keys():
    if inp == selection:
        print("You've selected the " + selection + "!")
