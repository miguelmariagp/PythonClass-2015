def ordinal(integer):
	try:
		if integer/1 in range(11,14): #this is making  both 11-14 and string jump to except
			raise Exception
		elif (integer-1)%10==0: #what happens with numbers ending in 1
			return "%sst" % integer #It has to be return and not print in order to run the test
		elif (integer-2)%10==0: #what happens with numbers ending in 2
			return "%snd" % integer
		elif (integer-3)%10==0: #what happens with numbers ending in 3
			return "%srd" % integer
		else: #what happens to the rest
			return "%sth" % integer
		
	except TypeError: #if it is a string
		return "Enter a number!"
	except:
		if integer in [11,12,13]:
			return "%sth" % integer


print ordinal('b')
print ordinal(1)
print ordinal(21)
print ordinal(2)
print ordinal (143)
print ordinal(11)
print ordinal(16)
