import csv
import arff
import math
import sys
import decimal

input_file = 'has_no_missing_lables.csv'
output_file1 = 'male_full_lables.arff'
output_file2 = 'female_full_lables.arff'
data = []

#read data
with open(input_file, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        list = []
        for item in row:
            splitItems = item.split(",")
            if splitItems[-1] == '' and len(splitItems) > 1:
                del splitItems[-1] # remove duplicates in split
            list.extend(splitItems)
            data.append(list) # do not include id num at index 0
    print 'finished convertering'

#split data
female_ex = []
male_ex = []
for example in data:
    print example
    if(len(example) > 0):
        if (example[0] == "Female"):
            female_ex.append(example)
        if (example[0] == "Male"):
            male_ex.append(example)


#write data
# with open(output_file1, 'wb') as csvfile:
#     spamwriter1 = csv.writer(csvfile, delimiter=',',
#                             quotechar=' ', quoting=csv.QUOTE_MINIMAL)
#     for i in female_ex:
#         spamwriter1.writerow(i)

# #write data
# with open(output_file2, 'wb') as csvfile:
#     spamwriter2 = csv.writer(csvfile, delimiter=',',
#                             quotechar=' ', quoting=csv.QUOTE_MINIMAL)
#     for i in male_ex:
#         spamwriter2.writerow(i)

# Output arff File
cutData = female_ex[2:] # remove feature names on first row
arffdata = {
    u'attributes': [
        #(u'gender', [u'Male', u'Female', u'Unknown']),
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
        (u'Firstyrcumgpa', list_intervals)
        #(u'Firstyrcumgpa', u'REAL')
    ],
    u'data': cutData, # list
    u'description': u'',
    u'relation': u'admission_stats'
}
with open(output_file2, 'w') as arffFile:
    arffFile.write(arff.dumps(arffdata))


cutData2 = male_ex[2:] # remove feature names on first row
arffdata2 = {
    u'attributes': [
        #(u'gender', [u'Male', u'Female', u'Unknown']),
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
        (u'Firstyrcumgpa', list_intervals)
        #(u'Firstyrcumgpa', u'REAL')
    ],
    u'data': cutData2, # list
    u'description': u'',
    u'relation': u'admission_stats'
}
with open(output_file1, 'w') as arffFile:
    arffFile.write(arff.dumps(arffdata2))
