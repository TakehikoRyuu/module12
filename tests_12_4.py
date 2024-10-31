# Логирование
import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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

logger = logging.getLogger(__name__)

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            Test_Walk = Runner('Walk')
            for _ in range(10):
                Test_Walk.walk()
            self.assertEqual(Test_Walk.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError:
            logging.warning(f'Неверная скорость для {Test_Walk}', exc_info=True)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            Test_Run = Runner('Run')
            for _ in range(10):
                Test_Run.run()
            self.assertEqual(Test_Run.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except TypeError:
            logging.warning(f'Неверный тип данных для объекта {Test_Run}', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        Test_Chall0 = Runner('Chall0')
        Test_Chall1 = Runner('Chall1')
        for _ in range(10):
            Test_Chall0.run()
            Test_Chall1.walk()
            self.assertNotEqual(Test_Chall0.distance, Test_Chall1.distance)

if __name__ == '__main__':
    logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s", encoding='UTF-8')


    first = Runner('Вося', 10)
    second = Runner('Илья', 5)
    third = Runner(Арсен, -10)

    t = Tournament(101, third, second)
    print(t.start())
