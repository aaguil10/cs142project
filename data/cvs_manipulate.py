import csv

input_file = 'test_data.csv'
output_file = 'test_output.csv'
data = []


#Do your magic!
def edit_row(list):
    list[1] = '0'
    #pass

#read data
with open(input_file, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        list = []
        for item in row:
            splitItems = item.split(",")
            if splitItems[-1] == '' and len(splitItems) > 1:
                del splitItems[-1]
            list.extend(splitItems)
        edit_row(list)
        data.append(list)

#write data
with open(output_file, 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for i in data:
    	spamwriter.writerow(i)


