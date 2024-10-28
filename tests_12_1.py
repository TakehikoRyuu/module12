#Простые Юнит-Тесты
import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        Test_Walk = Runner('Walk')
        for _ in range(10):
            Test_Walk.walk()
        self.assertEqual(Test_Walk.distance, 50)

    def test_run(self):
        Test_Run = Runner('Run')
        for _ in range(10):
            Test_Run.run()
        self.assertEqual(Test_Run.distance, 100)

    def test_challenge(self):
        Test_Chall0 = Runner('Chall0')
        Test_Chall1 = Runner('Chall1')
        for _ in range(10):
            Test_Chall0.run()
            Test_Chall1.walk()
            self.assertNotEqual(Test_Chall0.distance, Test_Chall1.distance)


if __name__ == '__main__':
    unittest.main()