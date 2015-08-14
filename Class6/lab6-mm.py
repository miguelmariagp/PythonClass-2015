#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers

cds=[]
def gcd(n1,n2):
	beg = min(n1,n2)
	if n1%beg==0 and n2%beg==0:
		print beg
	else:
		for i in range(1,beg):
			if n1%i==0 and n2%i==0:
				cds.append(i)
		print max(cds)
	
gcd(8,16)
gcd(8,12)

def gcd(a,b):
	r=a%b
	if r==0:
		return b
	return gcd(b,r)

#Exercise 2
#Write a function that returns prime numbers less than 121

import math

def prime(n):
	for i in range(2,n):
		if n%i == 0:
			return None
	return n

primes=[]
for i in range(122):
	if prime(i): primes.append(prime(i))


#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html

def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks:
        hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)
        print "Move disk %d from peg %d to peg %d" % (ndisks, startPeg, endPeg)
        hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)
 
hanoi(ndisks=4)






