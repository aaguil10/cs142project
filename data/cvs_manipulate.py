import csv
import arff
import math
import sys
import decimal

input_file = 'goodtrain.csv'
output_file = 'test_output.csv'
output_arffFile = 'test_arff.arff'
interval = 1
list_intervals = ['4.0', '3.0', '2.0', '1.0', '0.0']
data = []

# Set to True if you want to record rows with missing features.
recordMissingData = False


def roundPartial (value, resolution):
    return round (value / resolution) * resolution

def hasMissing(row):
    for i in range(0,len(row)):
        if(row[i] == ""):
            return True
    return False

#Do your magic!
def edit_row(row):
    #row[-1] = row[-1]
    #math.ceil(str(row[-1])*100)/100
    try:
        #gpa = math.ceil(float(row[-1])*1)/1
        gpa = roundPartial(float(row[-1]), float(interval))
        row[-1] = gpa
    except Exception:
        gpa = 0
        print "can't convert student: " + row[0]
    #row.remove(row[0])
    #print row[-1]
    

def drange(start, stop, step):
    r = start
    while r <= stop + 0.00000001: # ignore this plz
    	#yield r
        if r % 1.0 == 0:
            yield '%g.0' % r
        else:
            d = decimal.Decimal(interval)
            d = '%g' % abs(d.as_tuple().exponent)
            str = '%.' + d + 'f'
            yield str % r
        r += step


# Get Program Arguments
# argc[1] = name of file
# argv[2] = interval for gpa classification
if len(sys.argv) > 1:
    interval = sys.argv[2]
    input_file = sys.argv[1];
    #list_intervals = ["%.2f" % x for x in drange(0.0, 4.0, float(interval))]
    list_intervals = [x for x in drange(0.0, 4.0, float(interval.strip('"')))]
    if len(sys.argv) > 3:
        recordMissingData = True if sys.argv[3].lower() == 'true' else False


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
    print 'finished convertering'

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
        (u'Firstyrcumgpa', list_intervals)
        #(u'Firstyrcumgpa', u'REAL')
    ],
    u'data': cutData, # list
    u'description': u'',
    u'relation': u'admission_stats'
}
with open(output_arffFile, 'w') as arffFile:
    arffFile.write(arff.dumps(arffdata))
