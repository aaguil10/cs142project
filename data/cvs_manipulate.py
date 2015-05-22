import csv

input_file = 'test_data.csv'
output_file = 'test_output.csv'
data = []

#Do your magic!
def edit_row(list):
        list[1] = '0'



#read data
with open(input_file, 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
	list = row[0].split(",")
	edit_row(list)
        data.append(list)

#write data
with open(output_file, 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for i in data:
    	spamwriter.writerow(i)


