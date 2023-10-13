import src.types.weeklyOverview as WO
import src.types.teamOverview as TO

from bs4 import BeautifulSoup
import requests

URL = "https://www.pro-football-reference.com"
r = requests.get(URL)
webpage = BeautifulSoup(r.content, "lxml")

print("\nWelcome to NFL Scraper!\n")

print("Select an option:")
print("1. Weekly Overview")
print("2. Team Overview")

choice = input("Enter option: ")

if choice == "1":
    result = WO.findWeeklyResults(webpage)
    WO.writeOverview(result)

elif choice == "2":
    result = TO.findTeams(webpage)
    # print numbered list of teams to choose from
    for i in range(len(result)):
        print(str(i+1) + ". " + result[i].name)
    teamChoice = input("Enter option: ")
    
    # new webpage appended to URL
    URL += result[int(teamChoice)-1].link
    r = requests.get(URL)
    webpage = BeautifulSoup(r.content, "lxml")
    
    # write overview
    TO.writeTeamOverview(result[int(teamChoice)-1], webpage)