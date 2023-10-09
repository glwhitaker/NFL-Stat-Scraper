# define Team class
class Team:
    # constructor
    # param: teamGame - BeautifulSoup object containing team's game data
    def __init__(self, teamGame):
        self.name = teamGame.td.string
        self.score = int(teamGame.td.next_sibling.next_sibling.string)