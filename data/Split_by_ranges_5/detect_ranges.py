import csv
import arff
import math
import sys
import decimal

input_file = 'goodtrain.csv'
output_arffFile = 'test_arff.arff'
data = []
list_intervals = ['0', '1', '2', '3', '4']
#gpas are divided into 5 ranges where
# x > 3.61               is maped to 0
# 3.60 > x > 3.2883      is maped to 1
# 3.22 > x > 2.90        is maped to 2
# 2.89 > x > 2.33        is maped to 3
# 2.32 > x               is maped to 4


def edit_row(list):
    print "old: " 
    print list
    list.remove(list[0])
    #list.remove(list[-2])
    #list.remove(list[-2])
    x = -65
    try:
        x = float(list[-1])
    except Exception, e:
        pass
    else:
        pass

    print x
    if(x > 3.61):
        list[-1] = 0
    elif(3.61 >= x and x > 3.28):
        list[-1] = 1
    elif(3.28 >= x > 2.9):
        list[-1] = 2
    elif(2.9 >= x > 2.33):
        list[-1] = 3
    else:
        list[-1] = 4

    print "new: " 
    print list
    print " "

def print_seperators():
    GPAs.sort()
    #print GPAs
    print "1: " + GPAs[1]
    print "577: " + GPAs[577]
    print "-"
    print "578: " + GPAs[578]
    print "1154: " + GPAs[1154]
    print "-"
    print "1155: " + GPAs[1155]
    print "1731: " + GPAs[1731]

    print "-"
    print "1732: " + GPAs[1732]
    print "2308: " + GPAs[2308]
    print "-"
    print "2309: " + GPAs[2309]
    print "2884: " + GPAs[2883]



pollo = 1

GPAs = []
#read data
with open(input_file, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        if(pollo == 0):
            list = []
            featureMissing = False
            for item in row:
                splitItems = item.split(",")
                if splitItems[-1] == '' and len(splitItems) > 1:
                    del splitItems[-1] # remove duplicates in split
                list.extend(splitItems)
                if(list[-1] != ''):
                    GPAs.append(list[-1])
                #print list
            edit_row(list)
            data.append(list)
        else:
            pollo = 0

#print data

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
        (u'Firstyrcumgpa', list_intervals)
        #(u'Firstyrcumgpa', u'REAL')
    ],
    u'data': data, # list
    u'description': u'',
    u'relation': u'admission_stats'
}
with open(output_arffFile, 'w') as arffFile:
    arffFile.write(arff.dumps(arffdata))


