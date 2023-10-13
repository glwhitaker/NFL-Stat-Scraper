from ..classes import matchup as MU
from ..classes import team as T
import csv

def findTeams(webpage):
    teams = []

    weeklyResults = webpage.find('div',{'id':'scores'}).find_all('div',{'class':'game_summary'})

    for match in weeklyResults:
        thisMatch = MU.Matchup(match)

        teams.append(thisMatch.away)
        teams.append(thisMatch.home)


    return teams

def writeTeamOverview(team, webpage):
    file = open('teamOverview.csv', 'w')
    writer = csv.writer(file)

    writer.writerow(["Team Overview"])
    writer.writerow([])

    writer.writerow([team.name])
    
    results = team.findOverview(webpage)
    for result in results:
        writer.writerow([result.string])

