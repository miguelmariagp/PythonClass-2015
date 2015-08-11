from bs4 import BeautifulSoup
import urllib2 
import csv
import re

web_address='https://petitions.whitehouse.gov/petitions'
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read(),"html.parser")

#Open a .csv file
f = open('petitions.csv', 'wb')
my_writer = csv.DictWriter(f, fieldnames=("Title", "Date","Issues","Signatures"))
my_writer.writeheader()

#This gives me chunk with title and link
title=soup.find_all('a',{'rel':'nofollow'})

#This gives me chunk with link and number of signatures
sig=soup.find_all('div',{'class':'num-sig'})

#empty list to collect links
links=[]

for i in range(0,19):
	#xx and y extract the number of signatures from the string
	xx = str(sig[i])
	y = int(re.search(r'\d+',xx).group())
	#creating a list of the individual websites
	links.append(title[i]['href'])
	
	#opening each individual website
	web_address2=links[i]
	web_page2 = urllib2.urlopen(web_address2)
	soup2 = BeautifulSoup(web_page2.read(),"html.parser")
	
	issues=soup2.find_all('div',{'class':'issues'})[0]
	date=soup2.find_all('div',{'class':'date'})[0]
	my_writer.writerow({"Signatures":y,"Title":title[i].string,"Issues":re.sub(r'<[^>]+>','',str(issues))[8:],"Date":re.sub(r'<[^>]+>','',str(date))[16:]})
	
f.close()
	