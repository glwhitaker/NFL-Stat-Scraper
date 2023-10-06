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


def findWeeklyResults(webpage):

    file = open('weeklyOverview.csv', 'w')
    writer = csv.writer(file)

    # find weekly results tables
    weeklyResults = webpage.find('div',{'id':'scores'}).find_all('div',{'class':'game_summary expanded nohover'})

    allMatchups = []

    # write header row
    writer.writerow(["Weekly Results"])
    writer.writerow([])

    # loop through each matchup and create a Matchup object
    for match in range(0,len(weeklyResults), 2):
        # create two matchups at a time
        allMatchups.append(MU.Matchup(weeklyResults[match]))
        allMatchups.append(MU.Matchup(weeklyResults[match+1]))
        
        # write matchups two per row to csv
        writer.writerow([allMatchups[match].date, '', '', allMatchups[match+1].date])
        writer.writerow([allMatchups[match].away.name, allMatchups[match].away.score, '', allMatchups[match+1].away.name, allMatchups[match+1].away.score])
        writer.writerow([allMatchups[match].home.name, allMatchups[match].home.score, '', allMatchups[match+1].home.name, allMatchups[match+1].home.score])
        writer.writerow([])


    # find highest scoring team
    writer.writerow(["Higest Scoring Team"])
    highTeam, highScore = highestScore(allMatchups)
    writer.writerow([highTeam, highScore])

    # find the largest margin of victory
    writer.writerow(["Largest Margin of Victory"])
    largeTeam, largeMargin = largestMargin(allMatchups)
    writer.writerow([largeTeam, largeMargin])


    file.close()