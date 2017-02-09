import csv

lst=[]
with open('h3.csv', 'rb') as csvfile:
	read = csv.reader(csvfile)
	for row in read:
		lst_temp=[]
		lst_temp.append(str(row[2]))
		lst_temp.append(str(row[3]))
		lst_temp.append(str(row[7]))
		lst_temp.append(str(row[8]))
		if lst_temp not in lst and str(row[7]) is not '' :
			print lst_temp
			lst.append(lst_temp)