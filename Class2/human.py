class human(object):

	latin_name='homo sapien' #Attribute for the class
	
	#Add attributes for the instances.
	def __init__(self, age, sex, name=None): #initializer or constructor
		self.age = age
		self.name = name
		self.sex = sex
	def speak(self, words='Hello'):
		return words

	@classmethod # Works for the whole class
	def class_introduce(cls):
		return 'Here is humanity!'
		
		
	def __str__(self):
		return 'Human: %d year-old %s.' % (self.age, self.sex)
		
betul=human(34,'Female')
miguel=human(28,'Male','Miguel')		
		
print betul.sex
print miguel.name
print betul.name
print betul.speak()
print human.class_introduce()
print betul.class_introduce()
print betul


