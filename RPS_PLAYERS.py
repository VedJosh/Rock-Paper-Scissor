class Player:

    def __init__(self,name):
        self.player_name = name
        self.rps = None
        self.score = 0

    def player_score(self):
        return f"{self.player_name}'s SCORE is {self.score}"
    
    def player_choice(self):
        self.rps = input("'R' for Rock\n'P' for Paper\n'S' for Scissor\nEnter: ").upper()