from ..classes import matchup as MU
import csv

# calculate the highest score in all matchups
# param: allMatchups - list of Matchup objects
# return: highTeam - team with highest score
#         highScore - highest score
def highestScore(allMatchups):
    highScore = 0
    # find max
    for match in allMatchups:
        # if score exists, set score
        if match.away.score != "TBD" and match.home.score != "TBD":
            if match.away.score > highScore:
                highScore = match.away.score
                highTeam = match.away.name
            if match.home.score > highScore:
                highScore = match.home.score
                highTeam = match.home.name
    
    return highTeam, highScore


# calculate the largest margin of victory
# param: allMatchups - list of Matchup objects
# return: largeTeam - team with largest margin of victory
#         largeMargin - margin of victory
def largestMargin(allMatchups):
    largeMargin = 0
    for match in allMatchups:
        if match.away.score != "TBD" and match.home.score != "TBD":
            if match.away.score > match.home.score:
                margin = match.away.score - match.home.score
            else:
                margin = match.home.score - match.away.score

            if margin > largeMargin:
                largeMargin = margin
                largeTeam = match.winner().name
        
    return largeTeam, largeMargin


# write weekly overview to csv file
# param: allMatchups - list of Matchup objects
def writeOverview(allMatchups):
    file = open('weeklyOverview.csv', 'w')
    writer = csv.writer(file)

    # write header row
    writer.writerow(["Weekly Results"])
    writer.writerow([])
    
    # write each matchup
    for match in allMatchups:
        writer.writerow([match.date])
        writer.writerow([match.away.name, match.away.score])
        writer.writerow([match.home.name, match.home.score])
        writer.writerow([])

    # write highest scoring team
    writer.writerow(["Highest Scoring Team"])
    highTeam, highScore = highestScore(allMatchups)
    writer.writerow([highTeam, highScore])

    # write the largest margin of victory
    writer.writerow(["Largest Margin of Victory"])
    largeTeam, largeMargin = largestMargin(allMatchups)
    writer.writerow([largeTeam, largeMargin])

    file.close()



# find all weekly results
# param: webpage - BeautifulSoup object
# return: allMatchups - list of Matchup objects
def findWeeklyResults(webpage):
    # find weekly results tables
    weeklyResults = webpage.find('div',{'id':'scores'}).find('div',{'class':'game_summaries'}).find_all('div')

    # list of Matchup objects
    allMatchups = []

    # loop through each matchup and create a Matchup object
    for match in weeklyResults:
        # create Matchup object
        allMatchups.append(MU.Matchup(match))

    return allMatchups
        