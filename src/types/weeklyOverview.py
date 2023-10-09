from ..classes import matchup as MU
import csv

def highestScore(allMatchups):
    highScore = 0
    for match in allMatchups:
        if match.away.score > highScore:
            highScore = match.away.score
            highTeam = match.away.name
        if match.home.score > highScore:
            highScore = match.home.score
            highTeam = match.home.name
    
    return highTeam, highScore


def largestMargin(allMatchups):
    largeMargin = 0
    for match in allMatchups:
        if match.away.score > match.home.score:
            margin = match.away.score - match.home.score
        else:
            margin = match.home.score - match.away.score

        if margin > largeMargin:
            largeMargin = margin
            largeTeam = match.winner().name
        
    return largeTeam, largeMargin


def writeOverview(allMatchups):
    file = open('weeklyOverview.csv', 'w')
    writer = csv.writer(file)

    # write header row
    writer.writerow(["Weekly Results"])
    writer.writerow([])
    
    for match in allMatchups:
        writer.writerow([match.date])
        writer.writerow([match.away.name, match.away.score])
        writer.writerow([match.home.name, match.home.score])
        writer.writerow([])

    # find highest scoring team
    writer.writerow(["Highest Scoring Team"])
    highTeam, highScore = highestScore(allMatchups)
    writer.writerow([highTeam, highScore])

    # find the largest margin of victory
    writer.writerow(["Largest Margin of Victory"])
    largeTeam, largeMargin = largestMargin(allMatchups)
    writer.writerow([largeTeam, largeMargin])


    file.close()



def findWeeklyResults(webpage):
    # find weekly results tables
    weeklyResults = webpage.find('div',{'id':'scores'}).find_all('div',{'class':'game_summary expanded nohover'})

    allMatchups = []

    # loop through each matchup and create a Matchup object
    for match in weeklyResults:
        # create Matchup object
        matchup = MU.Matchup(match)
        # add Matchup object to list
        allMatchups.append(matchup)

    return allMatchups
        