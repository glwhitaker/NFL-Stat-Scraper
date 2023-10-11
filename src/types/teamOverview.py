from ..classes import matchup as MU
import csv

def findTeams(webpage):
    teams = []

    weeklyResults = webpage.find('div',{'id':'scores'}).find_all('div',{'class':'game_summary'})

    for match in weeklyResults:
        thisMatch = MU.Matchup(match)

        teams.append(thisMatch.away)
        teams.append(thisMatch.home)


    return teams

def writeTeamOverview(team):
    file = open('teamOverview.csv', 'w')
    writer = csv.writer(file)

    writer.writerow(["Team Overview"])
    writer.writerow([])

    writer.writerow([team.name])

