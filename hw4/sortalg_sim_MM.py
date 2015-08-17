from hw4_MM import *
import random
import matplotlib.pyplot as plt
import timeit

def iterations(sort_type,n): #sorts randomly generated numbers of length n
	if sort_type=="insertion sort":
		insertion([random.randint(-500,500) for number in range(n)])
	elif sort_type=="selection sort":
		selection([random.randint(-500,500) for number in range(n)])

		
time_insertion=[]
for n in range(1,1000):
	t=timeit.Timer('iterations("insertion sort", %s)' % (n), 'from __main__ import iterations').timeit(number=1)
	time_insertion.append(t)
	
time_selection=[]
for n in range(1,1000):
	t=timeit.Timer('iterations("selection sort", %s)' % (n), 'from __main__ import iterations').timeit(number=1)
	time_selection.append(t)

plt.figure() # open figure to plot

plt.plot(range(1,1000),time_insertion,label="Insertion Sort")
plt.plot(range(1,1000),time_selection,label="Selection Sort")
plt.xlabel("Number of elements")
plt.ylabel("Time")
plt.title("Runtime by size")
plt.legend(loc="upper left")
plt.savefig("runtime_by_n.pdf")