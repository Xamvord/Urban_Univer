import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Usain", 10)
        self.andrey = Runner("Andrey", 9)
        self.nick = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            result_str = {place: str(runner) for place, runner in value.items()}
            print(f"Test {key}: {result_str}")

    def test_01_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.assertTrue(results[len(results)] == self.nick)
        TournamentTest.all_results["Usain vs Nick"] = results

    def test_02_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.assertTrue(results[len(results)] == self.nick)
        TournamentTest.all_results["Andrey vs Nick"] = results

    def test_03_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.assertTrue(results[len(results)] == self.nick)
        TournamentTest.all_results["Usain vs Andrey vs Nick"] = results

if __name__ == '__main__':
    unittest.main()
