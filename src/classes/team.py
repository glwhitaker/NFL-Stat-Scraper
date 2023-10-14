# define Team class
class Team:
    # constructor
    # param: teamGame - BeautifulSoup object containing team's game data
    def __init__(self, teamGame):
        self.name = teamGame.td.string
        # if score exists, set score
        if teamGame.td.next_sibling.next_sibling.string != None:
            self.score = int(teamGame.td.next_sibling.next_sibling.string)
        else:
            self.score = "TBD"
        self.link = teamGame.td.a['href']