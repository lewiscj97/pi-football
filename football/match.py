class Match:
    def __init__(self, home_team, away_team, home_score, away_score, time):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score
        self.time = time

    def to_string(self):
        print(f'{self.home_team} {self.home_score} {self.time} {self.away_score} {self.away_team}')

    def to_array(self):
        return [f'{str(self.home_team)}: {self.home_score}', str(self.time), f'{str(self.away_team)}: {self.away_score}' ]
