import csv
import arff

input_file = 'test_data.csv'
output_file = 'test_output.csv'
output_arffFile = 'test_arff.arff'
data = []

# Set to True if you want to record rows with missing features.
recordMissingData = False



#Do your magic!
def edit_row(list):
    #list[1] = '0'
    pass

#read data
with open(input_file, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        list = []
        featureMissing = False
        for item in row:
            splitItems = item.split(",")
            if splitItems[-1] == '' and len(splitItems) > 1:
                del splitItems[-1] # remove duplicates in split
            list.extend(splitItems)
        edit_row(list)
        featureMissing = True if '' in list else False
        if recordMissingData or not featureMissing:
            data.append(list[1:]) # do not include id num at index 0

#write data
with open(output_file, 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for i in data:
    	spamwriter.writerow(i)


# Output arff File
cutData = data[1:] # remove feature names on first row
arffdata = {
    u'attributes': [
        (u'gender', [u'Male', u'Female', u'Unknown']),
        (u'Firgen', u'REAL'),
        (u'famincome', u'REAL'),
        (u'SATCRDG', u'REAL'),
        (u'SATMATH', u'REAL'),
        (u'SATWRTG', u'REAL'),
        (u'SATTotal', u'REAL'),
        (u'HSGPA', u'REAL'),
        (u'ACTRead', u'REAL'),
        (u'ACTMath', u'REAL'),
        (u'ACTEngWrit', u'REAL'),
        (u'APIScore', u'REAL'),
        (u'FirstLang', [u'English', u'EnglishandAnother', u'Another']),
        (u'HSGPAunweighted', u'REAL'),
        (u'Firststyrunitsforgpa', u'REAL'),
        (u'Firststyeartotcumunits', u'REAL'),
        (u'Firstyrcumgpa', u'REAL')
    ],
    u'data': cutData,
    u'description': u'',
    u'relation': u'admission_stats'
}
with open(output_arffFile, 'w') as arffFile:
    arffFile.write(arff.dumps(arffdata))