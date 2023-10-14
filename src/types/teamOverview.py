from ..classes import matchup as MU
import csv

# find all teams in a given week
# param: webpage - BeautifulSoup object
# return: list of Team objects
def findTeams(webpage):
    teams = []

    weeklyResults = webpage.find('div',{'id':'scores'}).find_all('div',{'class':'game_summary'})

    for match in weeklyResults:
        thisMatch = MU.Matchup(match)

        teams.append(thisMatch.away)
        teams.append(thisMatch.home)

    return teams

# find all sections in team overview
# param: webpage - BeautifulSoup object
# return: list of sections
def findOverview(webpage):
        # find headers
        headings = webpage.find('div',{'id':'content'}).find_all('h2')

        # remove last header
        headings.pop()

        return headings

# write team overview to csv file
# param: team - Team object
# param: webpage - BeautifulSoup object
def writeTeamOverview(team, webpage):
    file = open('teamOverview.csv', 'w')
    writer = csv.writer(file)

    writer.writerow(["Team Overview"])
    writer.writerow([])

    writer.writerow([team.name])
    
    sections = findOverview(webpage)
    for section in sections:
        writer.writerow([section.string])

