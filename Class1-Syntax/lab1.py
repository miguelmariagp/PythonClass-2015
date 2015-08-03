def binarify_cheat(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  elif num>0:
	return format(num,'b')
  return ''.join(digits)
  
def binarify_real(num):
	if num<=0: return '0'
	digits=[]
	while num != 0:
		digits.append(str(num%2))
		num /= 2
	digits.reverse()
	return ''.join(digits)
 
print binarify_real(22)
 
def int_to_base(num,base):
	"""convert positive integer to base 2"""
	if num<=0: return '0'
	digits=[]
	while num!=0:
		digits.append(str(num % base))
		num /= base
	digits.reverse()
	return ''.join(digits)
			
print int_to_base(22,2)



def base_to_int(string, base):
	"""take a string-formatted number and its base and return the base-10 integer"""
	if string=="0" or base <= 0 : return 0 
	string=string[::-1]
	x = [digit for digit in string]
	integ = []
	for i in range(0,len(string)):
		integ.append(int(x[i])*base**i)
	return sum(integ)
	
print base_to_int('10110',2)

	

def flexibase_add(str1, str2, base1, base2):
  return base_to_int(str1,base1) + base_to_int(str2,base2)
  """add two numbers of different bases and return the sum"""

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  return base_to_int(str1,base1) * base_to_int(str2,base2) 

#unfinished
def romanify(num):
  """given an integer, return the Roman numeral version"""
  result = 'M'*num/1000
  if num/100 == int()

  romano[] = 
  return romano
	
  
  result = ""
  return result
  
# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.