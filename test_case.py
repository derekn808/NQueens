from nqueens import *
import unittest


class TestProblem(unittest.TestCase):

	def test_5Queens(self):
		a = NQueens(5)
		case1 = (2, 0, 3, 1, 4)
		self.assertIn(case1, a.solutions)
		self.assertTrue(a.checkBoard(case1))

	def test_8Queens(self):
		b = NQueens(8)
		case2 = (7, 3, 0, 2, 5, 1, 6, 4)
		self.assertIn(case2, b.solutions)
		self.assertTrue(b.checkBoard(case2))	

if __name__ == '__main__':
    unittest.main()