import unittest
import tests_12_3


run_ST = unittest.TestSuite()
run_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
run_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))

runer = unittest.TextTestRunner(verbosity=2)
runer.run(run_ST)