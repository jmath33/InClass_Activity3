import unittest
import calc

class testCalc(unittest.TestCase):

	def test_add(self):
		self.assertEqual(calc.add(2,3), 5)

	def test_add_2(self):
		self.assertEqual(calc.add(2,5), 8)

	def test_sub(self):
		self.assertEqual(calc.subtract(8,3), 5)

	def test_sub_2(self):
		self.assertEqual(calc.subtract(8,2), 8)

	def test_multiply(self):
		self.assertEqual(calc.multiply(2,3), 6)

	def test_multiply_2(self):
		self.assertEqual(calc.multiply(2,5), 8)

	def test_div(self):
		self.assertEqual(calc.divide(12,4), 3)

	def test_div_2(self):
		self.assertEqual(calc.divide(100,2), 6)

if __name__ == '__main__':
	unittest.main()
