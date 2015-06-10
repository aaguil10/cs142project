# Craig Collins
# chcollin@ucsc.edu

import sys
import string
from sklearn import preprocessing

old_set = "goodtrain_withmeans.arff"
gpa_set = "goodtrain_rangedGPA.arff"
new_set = "goodtrain_withmeans_rangedGPA.arff" #"removed_goodtrain_withmeans_rangedGPA.arff"

dataset = {}



def convertMe():
	try:
		f = open(new_set, 'r')
		#gpa_file = open(gpa_set, 'r')
	except:
		sys.exit("Error: The was a problem opening your file.")
	t = f.read()
	#t2 = gpa_file.read()
	attributes = []
	dataArrays = []
	targets = []
	reachedData = False;
	tNL = t.split("\n")
	#t2NL = t2.split("\n") # For merging the file
	for s in tNL:
		#print(s)
		if (not reachedData):
			if not s:
				continue
			if (s[0] == '@'):
				tempLine = s.split(" ")
				if (tempLine[0] == "@attribute"): # Add attribute to list of attributes
					tempString = ""
					for x in range(1,len(tempLine)):
						tempString += tempLine[x]
					tempString += " "
					attributes.append(tempString)
				elif (tempLine[0] == "@data"):
					reachedData = True
		else:
			if (s[0] == "%"):
				break
			else:
				values = s.split(",")
				for val in range(len(values) - 1): # don't convert last values to num
					try:
						values[val] = float(values[val])
					except:
						continue
				dataArrays.append(values[:-3]) # not counting the last 3 since we don't know those
				targets.append(values[len(values) - 1]) # last value is target data


	ls = {"data": dataArrays, "feature_names": attributes, "target": targets}
	le_gender = preprocessing.LabelEncoder()
	le_lang = preprocessing.LabelEncoder()
	le_gender.fit(["Male", "Female", "Unknown"])
	le_lang.fit(["English", "EnglishandAnother", "Another"])
	for subj in ls["data"]:
		subj[0]  = le_gender.transform(subj[0]) # Gender
		subj[12] = le_lang.transform(subj[12]) # Languages
	#dataset = mergeGPA(ls)
	#print(ls)
	return ls

# run after 
def mergeGPA(data2):
	try:
		gpa_file = open(gpa_set, 'r')
	except:
		sys.exit("Error: The was a problem opening your file.")

	t = gpa_file.read()
	tNL = t.split("\n")
	reachedData = False;
	data = data2["data"]
	target = data2["target"]
	counter = 0;
	for s in tNL:
		#print(s)
		if (not reachedData):
			if not s:
				continue
			if (s[0] == '@'):
				tempLine = s.split(" ")
				if (tempLine[0] == "@ATTRIBUTE"): # Add attribute to list of attributes
					continue
				elif (tempLine[0] == "@DATA"):
					reachedData = True
		else:
			if (s[0] == "%"):
				break
			else:
				values = s.split(",")
				print(values[-1])
				target[counter] = values[-1] #last element replaced
				counter = counter + 1
	return data2




