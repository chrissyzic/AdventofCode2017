import csv
filename = 'daytwo_input.csv'

##FIRST STAR

checksum = 0

with open(filename) as csvDataFile:
	spreadsheet = csv.reader(csvDataFile)

	for row in spreadsheet:
		row_max = int(row[0])
		row_min = int(row[0])
		for i in range(len(row)):
			if int(row[i]) > row_max:
				row_max = int(row[i])
			elif int(row[i]) < row_min:
				row_min = int(row[i])
		row_diff = row_max - row_min
		checksum = checksum + row_diff

print "First star answer: " + str(checksum)

##SECOND STAR

checksum = 0

def find_row_res(listy):
	for i in range(len(listy)):
		for j in range(len(listy)):
			if int(listy[i]) != int(listy[j]) and int(listy[i]) % int(listy[j]) == 0:
				numerator = int(listy[i])
				denominator = int(listy[j])
			if int(listy[i]) != int(listy[j]) and int(listy[j]) % int(listy[i]) == 0:
				numerator = int(listy[j])
				denominator = int(listy[i])
	row_res = numerator / denominator
	return row_res
		
with open(filename) as csvDataFile:
	spreadsheet = csv.reader(csvDataFile)

	for row in spreadsheet:
		row_result = find_row_res(row)
		checksum = checksum + row_result
	print "Second star answer: " + str(checksum)

