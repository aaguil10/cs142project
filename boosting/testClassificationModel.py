import arff
import sys
from sklearn import linear_model

gender = {'Male' : 0, 'Female' : 1, 'Unknown' : 2}
language = {'English' : 0, 'EnglishandAnother' : 1, 'Another' : 2}

filename = sys.argv[1]

examples = []
labels = []

with open(filename, 'rb') as af:
	arffFile = arff.load(af)
	attributes = arffFile['attributes']
	data = arffFile['data']
	for row in data:
		row[0] = gender[row[0]] # index of gender
		row[12] = language[row[12]] # index of language
		examples.append(row[0:-1])
		labels.append(row[-1])

clf = linear_model.Perceptron()
print clf.fit(examples, labels)
print clf.coef_