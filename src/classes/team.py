class Team:
    def __init__(self, teamGame):
        self.name = teamGame.td.string
        self.score = int(teamGame.td.next_sibling.next_sibling.string)