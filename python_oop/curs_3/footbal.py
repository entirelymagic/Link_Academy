from time import time, sleep
from random import randint


class Team:
    def __init__(self, team_name):
        self.team_name = team_name


class Score:
    def __init__(self, home, away):
        self.home = home
        self.away = away


class Match:
    __END_TIME = 90

    def __init__(self, home, away):
        self.home = Team(home)
        self.away = Team(away)
        self.minute = 0
        self.score = [0, 0]

    @staticmethod
    def __generate_chance():
        return randint(1, 90)

    def start(self):
        total_score = randint(0, 13)
        nr_of_goals = 0
        event_time = set()
        self.minute = 0
        nr_events = len(event_time)
        while nr_events < total_score:
            event_time.add(self.__generate_chance())
            nr_events = len(event_time)
        print('Game Started')
        while self.minute <= self.__END_TIME:
            self.minute += 1
            sleep(0.1)

            if nr_of_goals <= total_score:
                for event in sorted(event_time):
                    if event == self.minute:
                        if self.__generate_chance() > self.__generate_chance():  # check what team will score
                            self.score[0] += 1
                            print(f' {self.home.team_name}  scored at minute {self.minute}')
                        else:
                            self.score[1] += 1
                            print(f' {self.away.team_name}  scored at minute {self.minute}')
                        print(f'The score is {self.score[0]} : {self.score[1]}')
                        nr_of_goals += 1

        print('*' * 30)
        print(f"Game ended: Final score {self.home.team_name}:{self.score[0]} {self.away.team_name}:{self.score[1]}")


match = Match('Steaua', 'Dinamo')
match.start()
