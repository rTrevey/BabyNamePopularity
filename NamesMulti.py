import re
import urllib
import requests
from bs4 import BeautifulSoup as bs
import sys
import matplotlib.pyplot as plt
import time
import os
#import numpy as np

baseurl = "http://www.ssa.gov/cgi-bin/popularnames.cgi"

def birthYearScrape(name):
	list = []
	for i in range(1880, 2014):
		post_params = {
           "number":"n",
           "top": "1000",
           "year": i
           }
		post_args  = urllib.urlencode(post_params)
		html = urllib.urlopen(baseurl, post_args).read()
		soup = bs(html)
		birthYear = soup.find('h2').getText().split()[2]
		try:
			regex = re.compile(r'td\>(%s)\</td\>' %name)
			regex2 = re.compile(r'\<td\>(\S+)\</td\>')
			nameMatch = re.findall(regex, html)[0]
			nameMatchindex = html.index(nameMatch) + len(name)
			numUni = re.findall(regex2, html[nameMatchindex: nameMatchindex + 25])[0]
			if ',' in numUni:
				num = (int(''.join(numUni.split(','))))
			else:
				num = int(numUni)
			tuple = (birthYear, num)
			print str(num) + " in " + str(birthYear)
		except Exception, e:
			num = 0
			print "Birth year count missing..."
			print birthYear
			print str(e)
			tuple = (birthYear, 0)
		list.append(tuple)
		time.sleep(2)
	return list

def makeInt(string):
	integer = int(re.findall(r'(\d+)', string)[0])
	return integer

def main(names):
	list_list =[]
	for name in names:#This loop should actually run inside the openfile loop
		list = []
		path = '/home/trevey/Documents/google-python-exercises/babynames/BabyNames/'
		fileList = os.listdir(path)
		for filename in fileList:
			year = str(filename)[-8:-4]
			try:
				with open(path + filename) as inFile:
					nameFile = inFile.read()
				regex = re.compile(r'%s,\w,(\d+)\r' %name)
				regex2 = re.compile(r'\w+,\w,(\d+)')
				listOfNums = re.findall(regex2, nameFile)
				realNums = [int(x) for x in listOfNums]
				total = sum(realNums)
				numbers = re.findall(regex, nameFile)
				number = sum([int(x) for x in numbers])
				percent = (float(number) / total) * 100
				tuple = (year, number, percent)
			except Exception, e:
				print str(e)
				tuple = (year, 0, 0)
			list.append(tuple)
		list.sort(key=lambda tup: tup[0])
		list_list.append(list)
	plot(list_list, names)
	
def plot(list_list, names):
	plt.figure(1)
	plt.subplot(211)
	rawlist1 = [int(y[1]) for y in list_list[0]]
	ylist1 = [x - rawlist1[i - 1] for i, x in enumerate(rawlist1)]
	rawlist2 = [int(y[1]) for y in list_list[1]]
	ylist2 = [x - rawlist2[i - 1] for i, x in enumerate(rawlist2)]
	print type(ylist2[0])
	list_totals = [ylist1 + ylist2]
	xlist1 = [x[0] for x in list_list[0]]
	xlist2 = [x[0] for x in list_list[1]]
	plt.plot(xlist1, ylist1, 'b', xlist2, ylist2, 'r')
	#minVal = min(list_totals) - (.20 * (min(list_totals)))
	#maxVal = max(list_totals) + (.20 * (min(list_totals)))
	#plt.axis([1880, 2013, minVal, maxVal])
	plt.ylabel('Popularity Shift/Rate of Change')
	plt.xlabel("Year")
	
	plt.subplot(212)
	list_totals2 = [y[2] for y in list_list[0]] + [y[2] for y in list_list[1]]
	y2list1 = [float(y[2]) for y in list_list[0]]
	y2list2 = [float(y[2]) for y in list_list[1]]
	plt.plot(xlist1, y2list1, 'b', xlist2, y2list2, 'r')
	#minVal2 = min(list_totals2) - (.20 *(min(list_totals2)))
	#maxVal2 = max(list_totals2) + (.20* (max(list_totals2)))
	#plt.axis([1880, 2013, minVal2, maxVal2])
	plt.ylabel('Percent of Births')
	plt.xlabel("Year")
	plt.show()

	
if __name__ == "__main__":
	names = [sys.argv[1], sys.argv[2]]
	main(names)
