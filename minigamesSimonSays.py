class SimonSays:
    def __init__(self):
        self.Board ={}
        self.Board[0] = {}
        self.Board[1] = {}

    def Generate_Board(self):
        self.Board[0][0] = "dark-green"
        self.Board[0][1] = "dark-red"
        self.Board[1][0] = "dark-yellow"
        self.Board[1][1] = "dark-blue"

        return self.Board

