from classes import team

class Matchup:
    # constructor takes in a BeautifulSoup object
    # representing a single matchup and parses it
    def __init__(self, game):
        self.date = game.find('tr',{'class':'date'}).td.string
        self.winner = team.Team(game.find('tr',{'class':'winner'}))
        self.loser = team.Team(game.find('tr',{'class':'loser'}))
    
    # string representation of a matchup
    def __str__(self):
        return self.date + "\n" + self.winner.name + " " + self.winner.score + \
            "\n" + self.loser.name + " " + self.loser.score + "\n"