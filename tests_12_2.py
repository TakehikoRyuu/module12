# Методы Юнит-тестирования
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
    def setUpClass(self):
        self.all_results = []


    def setUp(self):
        self.Runner1 = Runner('Усэйн', 10)
        self.Runner2 = Runner('Андрей', 9)
        self.Runner3 = Runner('Ник', 3)

    def test_tournament_results(self):
        tournaments = [
            Tournament(90, self.Runner1, self.Runner3),
            Tournament(90, self.Runner2, self.Runner3),
            Tournament(90, self.Runner1, self.Runner2, self.Runner3)
        ]

        for tournament in tournaments:
            results = tournament.start()
            last_place = max(results.keys())
            self.assertEqual(results[last_place].name, self.Runner3.name)

            formatted_result = {place: runner.name for place, runner in results.items()}
            self.all_results.append(formatted_result)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)


if __name__ == '__main__':
    unittest.main()