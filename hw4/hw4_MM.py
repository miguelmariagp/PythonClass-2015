#Insertion Sort

#mylist=[2,1,3,4]
#mylist2=[9,8,7,6,5,4,3,2,1]

def insertion(thelist):
	for i in range(1,len(thelist)):
		val=thelist[i]
		j=i
		while j>0 and thelist[j-1]>val:
			thelist[j]=thelist[j-1]
			j=j-1
			thelist[j]=val
	return thelist

#insertion(mylist)
#print mylist
#insertion(mylist2)
#print mylist2
			
#Selection Sort
#(I just dont know why the list is empty in the end)

#mylist=[2,1,3,4]
#mylist2=[9,8,7,6,5,4,3,2,1]

def selection(thelist):
	for i in range(len(thelist)):
		m=min(thelist[i:])
		pos=thelist.index(m)
		if pos==i: pass
		else: thelist[pos],thelist[i]=thelist[i],thelist[pos]
	return thelist
	
#selection(mylist)
#print mylist
#selection(mylist2)
#print mylist2
