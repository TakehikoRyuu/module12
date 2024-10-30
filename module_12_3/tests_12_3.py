import unittest
from tests_12_2 import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(self):
        self.all_results = []

    def setUp(self):
        self.Runner1 = Runner('Усэйн', 10)
        self.Runner2 = Runner('Андрей', 9)
        self.Runner3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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



class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        Test_Walk = Runner('Walk')
        for _ in range(10):
            Test_Walk.walk()
        self.assertEqual(Test_Walk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        Test_Run = Runner('Run')
        for _ in range(10):
            Test_Run.run()
        self.assertEqual(Test_Run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        Test_Chall0 = Runner('Chall0')
        Test_Chall1 = Runner('Chall1')
        for _ in range(10):
            Test_Chall0.run()
            Test_Chall1.walk()
            self.assertNotEqual(Test_Chall0.distance, Test_Chall1.distance)