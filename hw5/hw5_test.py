import unittest
from hw5 import *

class hw5Test(unittest.TestCase):
	def test_input(self):
		LinkList(None)
		LinkList('a')
		LinkList(0.5)
		LinkList(1)
	
	def test_addNode(self):
		lili = LinkList(5)
		lili.addNode(7)
		lili.addNode(6)
		self.assertEqual('[5, 7, 6]',lili.__str__())
	
	def test_addNodeAfter(self):
		lili = LinkList(0)
		lili.addNodeAfter(3,1)
		lili.addNodeAfter(-1,1)
		lili.addNodeAfter(2,3)
		self.assertEqual('[0, -1, 3, 2]',lili.__str__())
	
	def test_addNodeBefore(self):
		lili = LinkList(-1)
		lili.addNodeBefore(8,1)
		lili.addNodeBefore(0,2)
		lili.addNodeBefore(50,3)
		self.assertEqual('[-1, 0, 50, 8]',lili.__str__())
		
	def test_removeNode(self):
		lili = LinkList(99)
		lili.addNode(2)
		lili.addNode(16)
		lili.addNodeBefore(-77,3)
		lili.addNodeAfter(0,3)
		lili.removeNode(1)
		lili.removeNode(4)
		lili.removeNode(2)
		lili.removeNode(2)
		self.assertEqual('[2]',lili.__str__())
	
	def test_removeNodeByValue(self):
		lili = LinkList(34)
		lili.addNode(1)
		lili.addNode(3)
		lili.addNodeBefore(0,1)
		lili.addNodeAfter(30,1)
		lili.addNodeAfter(30,5)
		lili.removeNodeByValue(30)
		self.assertEqual('[34, 0, 1, 3]',lili.__str__())
	
	def test_reverse(self):
		lili = LinkList(31)
		lili.addNode(70)
		lili.addNode(-23)
		self.assertEqual('[31, 70, -23]',lili.__str__())
		lili.reverse()
		self.assertEqual('[-23, 70, 31]',lili.__str__())
	
	def test_length(self):
		lili = LinkList(9)
		lili.addNode(30)
		lili.addNodeBefore(-65,1)
		lili.removeNode(1)
		self.assertEqual(2,lili.length)



if __name__ == '__main__':
	unittest.main()