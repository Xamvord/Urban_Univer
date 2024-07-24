import unittest
from hw_m12_3_tests import RunnerTest, TournamentTest

def suite():
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    test_suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
    test_suite.addTests(loader.loadTestsFromTestCase(TournamentTest))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
