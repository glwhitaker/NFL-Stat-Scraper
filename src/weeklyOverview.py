import csv
from classes import matchup

def findWeeklyResults(webpage):

    file = open('report.csv', 'w')
    writer = csv.writer(file)

    # find weekly results tables
    weeklyResults = webpage.find('div',{'id':'scores'}).find_all('div',{'class':'game_summary expanded nohover'})

    allMatchups = []

    # write header row
    writer.writerow(["Weekly Results"])
    writer.writerow([])

    # loop through each matchup and create a Matchup object
    for match in weeklyResults:
        myMatch = matchup.Matchup(match)

        # add Matchup object to list
        allMatchups.append(myMatch)

        # write to csv
        writer.writerow([myMatch.date])
        writer.writerow([myMatch.away.name, myMatch.away.score])
        writer.writerow([myMatch.home.name, myMatch.home.score])
        writer.writerow([myMatch.winner().name])
        writer.writerow([])

    # find the largest margin of victory
    largestMargin = 0
    for match in allMatchups:
        if match.away.score > match.home.score:
            margin = match.away.score - match.home.score
        else:
            margin = match.home.score - match.away.score

        if margin > largestMargin:
            largestMargin = margin
            largestTeam = match.winner().name

    writer.writerow(["The largest margin of victory was the " + largestTeam + " by " + str(largestMargin) + " points."])


    file.close()