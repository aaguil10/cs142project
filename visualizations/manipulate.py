# This program combines the 'detect_ranges.py' file with 'fillValuesByClasses.py' file
#
# gpas are divided into 5 ranges where
# x > 3.61               is maped to 0
# 3.60 > x > 3.2883      is maped to 1
# 3.22 > x > 2.90        is maped to 2
# 2.89 > x > 2.33        is maped to 3
# 2.32 > x               is maped to 4
#
#
# Input Arguments: 
#   arg1 - 'name of csv file'
#   arg2 - 'name of output file'
# 
# Command Flags:
#   -n   - no normalization
#   (CURRENTLY DOES NOT WORK)-t   - manipulate test set (does not include firstyearunits and label)
#
# Output:
#   Program will output two files with name 'arg2'.arff and 'arg2'.csv.
#   Files will have means/modes of class
#

import csv
import arff
import math
import sys
import argparse
import decimal
import os
import shutil
from testConverter import *
from collections import Counter

# Classify Each Example
def edit_row(list):
    #print "old:"
    #print list
    #list.remove(list[0])
    #list.remove(list[-2])
    #list.remove(list[-2])
    x = -65
    try:
        x = float(list[-1])
    except Exception as e:
        pass
    else:
        pass

    #print x
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

# split the file by the number of classifiers
def splitFile(filename):
    numClasses = 0
    classData = dict()
    with open(filename, 'rb') as af:
        arffFile = arff.load(af)
        attributes = arffFile['attributes']
        classes = attributes[-1][1]
        # replaces empty list for Firstyrcumgpa
        template['attributes'][-1] = (template['attributes'][-1][0], classes)
        numClasses = len(classes)
        for c in classes: 
            classData.setdefault(c, [])
        arffData = arffFile['data']
        for row in arffData:
            if row[-1] != None:
                cList = classData[row[-1]]
                cList.append(row)
        # save each key of classData to a sepporate arff
        filenum = 0
        for key, data in classData.items():
            template['data'] = data
            with open(temp_dir + '\o%g.arff' % filenum, 'w') as arffFile:
                arffFile.write(arff.dumps(template))
            filenum += 1
    return numClasses

# finds the missing values for a particular ARFF file
def findMissingValues(filename):
    with open(filename, 'r+') as af:
        arffFile = arff.load(af)
        data = arffFile['data']
        attributes = arffFile['attributes']
        numExamples = len(data)
        averages = []
        # loop over each attribute
        for index in range(len(attributes)):
            attr = attributes[index]
            average = '?'
            if isinstance(attr[1], list): # find mode if attr is classifier
                words_to_count = (row[index] for row in data if row[index] != None)
                c = Counter(words_to_count)
                average = c.most_common(1)[0][0] # stacks on stacks
            else: # find mean
                average = sum([row[index] for row in data if row[index] != None]) / numExamples
            averages.append(average)
        # udpate the missing values
        for row in data:
            for index in range(len(row)):
                if row[index] == None:
                    row[index] = averages[index]
        # overwrite the file
        af.seek(0)
        af.write(arff.dumps(arffFile))
        af.truncate()
        return data

def replaceByConversion(example):
    # 4, 5, 6   SAT: Comp, Math, Writing
    # 9, 10, 11  ACT: Reading, Math, Writing
    if example[4] == None and example[9] != None:
        example[4] = ACTreadToSATcomp(example[8])
    if example[5] == None and example[10] != None:
        example[5] = ACTmathToSATmath(example[9])
    if example[6] == None and example[11] != None:
        example[6] = ACTwritToSATwrit(example[10])
    if example[9] == None and example[4] != None:
        example[9] = SATcompToACTread(example[3])
    if example[10] == None and example[5] != None:
        example[10] = SATmathToACTmath(example[4])
    if example[11] == None and example[6] != None:
        example[11] = SATwritToACTwrit(example[5])

# Normalizes a particular feature i
# NOTE: Assumes that i is a REAL number feature
def normFeature(ds, i):
	s = [row[i] for row in ds]
	maxVal = max(s)
	minVal = min(s)
	for row in ds:
		row[i] = (row[i] - minVal) / (maxVal - minVal)

# Helper Print Function
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


# =============== MAIN ===============
# ====================================
input_file = sys.argv[1]
output_arffFile = sys.argv[2]
recordMissingData = False if '-r' in sys.argv else True
isTestSet = False if '-t' not in sys.argv else True
useConverts = False if '-c' in sys.argv else True

pollo = 1
GPAs = []
data = []
list_intervals = ['0', '1', '2', '3', '4']

# Read Data
with open(input_file, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        featureMissing = False
        if(pollo == 0):
            list_data = []
            featureMissing = False
            for item in row:
                splitItems = item.split(",")
                if splitItems[-1] == '' and len(splitItems) > 1:
                    del splitItems[-1] # remove duplicates in split
                list_data.extend(splitItems)
                if(list_data[-1] != ''):
                    GPAs.append(list_data[-1])
                #print list_data
            edit_row(list_data)
            featureMissing = True if '' in list_data else False
            if recordMissingData or not featureMissing:
                data.append(list_data)
        else:
            pollo = 0

# Create ARFF Attributes Template
template_attr = [
        (u'Subjnum', u'REAL'),
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
    ]
if isTestSet:
    template_attr = []

# Creat ARFF Template
template = {
    u'attributes': template_attr,
    u'data': data, # list
    u'description': u'',
    u'relation': u'admission_stats'
}

# Save ARFF FILE
with open(output_arffFile, 'w') as arffFile:
    arffFile.write(arff.dumps(template))

print 'Finished Classifying...'

input_arff = output_arffFile

if not useConverts:
    with open(input_arff, 'r+') as af:
        arffFile = arff.load(af)
        data = arffFile['data']
        datalist = []
        for row in data:
            replaceByConversion(row)
            datalist.append(row)
        print 'Finished Converting...'
        arffFile['data'] = datalist
        af.seek(0)
        af.write(arff.dumps(arffFile))
        af.truncate()

#if useConverts:
# Calculate Means/Modoes and Normalize 
temp_dir = 'temp'
normalize = True if '-n' not in sys.argv else False

# see if temp directory exists and if so make a new one
if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir)
os.makedirs(temp_dir)

# split up the file
numFiles = splitFile(input_arff)

# fill in missing values
datalist = []
for i in range(numFiles):
    datalist.extend(findMissingValues(temp_dir + '\o%g.arff' % i))

print 'Finished Calculating Means/Modes...'

# combine all datafiles
with open(input_arff, 'r+') as af:
    arffFile = arff.load(af)
    # normalize the data is requested
    if normalize:
        attrs = arffFile['attributes']
        for index in range(len(attrs)):
            # skip features 0, 1 and 13
            if index != 0 and index != 1 and index != 13 and index != len(attrs)-1:
                normFeature(datalist, index)
        print 'Finished Normalizing...'
    arffFile['data'] = datalist
    af.seek(0)
    af.write(arff.dumps(arffFile))
    af.truncate()
#else:
#    with open(input_arff, 'r+') as af:
#        arffFile = arff.load(af)
#        data = arffFile['data']
#        datalist = []
#        for row in data:
#            replaceByConversion(row)
#            datalist.append(row)
#        print 'Finished Converting...'
#        arffFile['data'] = datalist
#        af.seek(0)
#        af.write(arff.dumps(arffFile))
#        af.truncate()

print 'Done!'