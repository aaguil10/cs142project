import sys
import arff
import os
import shutil
from collections import Counter


input_arff = 'test_input.arff'
temp_dir = 'temp'

# arff template to be overwritten
template = {
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
        (u'Firstyrcumgpa', []) # empty list
    ],
    u'data': [], # empty list
    u'description': u'',
    u'relation': u'admission_stats'
}


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


# Main: 
#       get input, split file, replace missing values, recombine file
if len(sys.argv) > 1:
    input_arff = sys.argv[1]

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

# combine all datafiles
with open(input_arff, 'r+') as af:
    arffFile = arff.load(af)
    arffFile['data'] = datalist
    af.seek(0)
    af.write(arff.dumps(arffFile))
    af.truncate()