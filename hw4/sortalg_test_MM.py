#Sorting Algorithms test

import unittest
from hw4_MM import *

mylist=[2,1,3]
mylist2=[9,8,7,6,5,4,3,2,1]
class hw4Test(unittest.TestCase):
	def test_insertion(self):
		x=[9,8,7,6,5,4,3,2,1]
		insertion(x)
		for i in range(1,len(x)):
			if x[i-1] > x[i]:
				print self.fail("Insertion sort failed")
				
	def test_selection(self):
		x=[9,8,7,6,5,4,3,2,1]
		selection(x)
		for i in range(1,len(x)):
			if x[i-1] > x[i]:
				print self.fail("Selection sort failed")
			

if __name__ == '__main__': #Add this if you want to run the test with this script.
	unittest.main()