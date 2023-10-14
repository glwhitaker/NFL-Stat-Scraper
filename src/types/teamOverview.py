from ..classes import matchup as MU
from ..classes import section as SE
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
        sections = []

        for section in webpage.find('div',{'id':'content'}).find_all('div',{'class':'table_wrapper'}):\
            sections.append(SE.Section(section))
        
        return sections

# write team overview to csv file
# param: team - Team object
# param: webpage - BeautifulSoup object
def writeTeamOverview(team, webpage):
    file = open('teamOverview.csv', 'w')
    writer = csv.writer(file)

    writer.writerow(["Team Overview"])
    writer.writerow([])

    writer.writerow([team.name])
    writer.writerow([])
    
    sections = findOverview(webpage)

    for section in sections:
        writer.writerow([section.header.text])
        writer.writerow(section.headings)
        for row in section.rows:
            writer.writerow(row)
        writer.writerow([])
    
