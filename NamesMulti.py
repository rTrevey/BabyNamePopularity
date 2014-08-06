import re
import sys
import matplotlib.pyplot as plt
import os

def main(names):
	list_list =[]
	for name in names:
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
	plt.figure(1, figsize = (7.5, 9.25))
	plt.subplot(311)
	ylist1 = [int(y[1]) for y in list_list[0]]
	ylist2 = [int(y[1]) for y in list_list[1]]
	list_totals = [ylist1 + ylist2]
	xlist1 = [x[0] for x in list_list[0]]
	xlist2 = [x[0] for x in list_list[1]]
	plt.plot(xlist1, ylist1, 'b', xlist2, ylist2, 'r')
	plt.ylabel('Total Births By Name')
	plt.xlabel("Year")
	
	plt.subplot(312)
	y2list1 = [x - ylist1[i - 1] for i, x in enumerate(ylist1)]
	y2list2 = [x - ylist2[i - 1] for i, x in enumerate(ylist2)]
	list_totals = [y2list1 + y2list2]
	plt.plot(xlist1, y2list1, 'b', xlist2, y2list2, 'r')
	plt.ylabel('Popularity Shift/Rate of Change')
	plt.xlabel("Year")
	
	plt.subplot(313)
	list_totals2 = [y[2] for y in list_list[0]] + [y[2] for y in list_list[1]]
	y3list1 = [float(y[2]) for y in list_list[0]]
	y3list2 = [float(y[2]) for y in list_list[1]]
	plt.plot(xlist1, y3list1, 'b', xlist2, y3list2, 'r')
	plt.ylabel('Percent of Births')
	plt.xlabel("Year")
	plt.tight_layout()
	plt.show()

	
if __name__ == "__main__":
	names = [sys.argv[1], sys.argv[2]]
	main(names)
