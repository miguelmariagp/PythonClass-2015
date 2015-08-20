class Node():
	def __init__(self,_value=None,_next=None):
		self.value=_value
		self.next=_next
	
	def __str__(self):
		return str(self.value)

	
class LinkList():
	def __init__(self,value):
		if type(value)==int:
			self.head=Node(value)
			self.length=1
		else:
			print "Integers, please!"
		
	def length(self): #returns the length of the list, which is updated in each method
		return self.length
		
		
	def addNode(self,new_value):
		moving = self.head
		while moving.next != None:
			moving = moving.next
		moving.next = Node(new_value) #The new node is added at the end
		self.length += 1
		
	def addNodeAfter(self, new_value, after_node):
		if after_node > self.length or after_node < 1: #Only possible cases
			print "Outside of range"
		elif after_node==1:
			temp=self.head.next
			self.head.next=Node(new_value)
			self.head.next.next = temp
			self.length += 1
		else:
			current_node = self.head
			index = 2
			while index <= after_node:
				current_node = current_node.next
				index += 1
			current_node.next = Node(new_value, current_node.next)
			self.length += 1
			
	def addNodeBefore(self, new_value, before_node):
		if before_node < 1 or before_node > self.length: #Only possible cases
			print "Outside of range"
		elif before_node==self.head:
			temp=self.head
			self.head=Node(new_value)
			self.head.next=temp
			self.length += 1
		else:
			current_node = self.head
			index=2
			while index <= (before_node-1):
				current_node=current_node.next
				index+=1
			current_node.next = Node(new_value, current_node.next)
			self.length += 1	

	def removeNode(self, node_to_remove):
		if node_to_remove > self.length or node_to_remove < 1:
			print "Outside of range"
		elif node_to_remove == 1 and self.length == 1:  # When you try to remove the only node in the list
			print "This will kill the list!"
		elif node_to_remove == 1:
			self.head = self.head.next
			self.length -= 1
		elif node_to_remove == self.length:
			current_node = self.head
			index=2
			while index <= (node_to_remove-1):
				current_node = current_node.next
				index += 1
			current_node.next = None
			self.length -= 1
		else:
			current_node=self.head
			index=2
			while index <= node_to_remove:
				current_node = current_node.next
				index += 1
			current_node.value = current_node.next
			current_node.next = current_node.next.next
			self.length -= 1
			
	
	def removeNodeByValue(self, value):
		current_node = self.head
		index=1
		while index <= self.length:
			if current_node.value == value:
				self.removeNode(index)
				if index==1: #If the node to remove was the head
					current_node=self.head
				else: #If the node is somewhere else in the list
					indextwo=1
					current_node = self.head
					while indextwo < index: #Second loop to find the right current_node
						current_node = current_node.next
						indextwo+=1
			else: #Moving forward if the node is not the one we wanted
				index+=1
				current_node=current_node.next
	
	def reverse(self):
		current_node=self.head
		last=None
		while current_node:
			next = current_node.next
			current_node.next = last
			last = current_node
			current_node = next
		if self.head:
			self.next = self.head
			self.head = last
		return self.__str__()
				
	
	def __str__(self):
		linked_list = '[%s' % (self.head)
		current_node = self.head
		while current_node.next != None:
			current_node = current_node.next
			linked_list += ', ' + str(current_node)
		linked_list += ']'
		return linked_list
			
		

lili=LinkList(5)
print lili
lili.addNode(6)
print lili
lili.addNodeAfter(8,1)
print lili
lili.addNodeBefore(2,3)
print lili
lili.removeNode(4)
print lili
#problem here
lili.removeNodeByValue(8)
print lili
#and problem here
lili.reverse()
print lili
print lili.length