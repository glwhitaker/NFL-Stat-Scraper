from . import team

class Matchup:
    # constructor takes in a BeautifulSoup object
    # representing a single matchup and parses it
    def __init__(self, game):
        self.date = game.find('tr',{'class':'date'}).td.string
        self.away = team.Team(game.tr.findNext('tr'))
        self.home = team.Team(game.tr.findNext('tr').findNext('tr'))

    # returns the winner of the matchup
    def winner(self):
        if self.away.score > self.home.score:
            return self.away
        else:
            return self.home