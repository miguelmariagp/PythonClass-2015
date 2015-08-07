#Ordinal test

import unittest
import ordinal

class OrdinalTest(unittest.TestCase):

	def test_st(self):
		self.assertEqual('21st',ordinal.ordinal(21))
		
	def test_nd(self):
		self.assertEqual('2nd',ordinal.ordinal(2))
	def test_eleven(self):
		self.assertEqual('11th',ordinal.ordinal(11))
	def test_string(self):
		self.assertEqual("Enter a number!", ordinal.ordinal('b'))

if __name__ == '__main__': #Add this if you want to run the test with this script.
  unittest.main()