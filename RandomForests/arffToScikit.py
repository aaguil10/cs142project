# Craig Collins
# chcollin@ucsc.edu

import sys
import string
from sklearn import preprocessing
from sat_act_conv import sat_to_act_writing
from sat_act_conv import act_to_sat_writing

old_set  = "goodtrain_withmeans.arff"
gpa_set  = "goodtrain_rangedGPA.arff"
new_set  = "goodtrain_withmeans_rangedGPA.arff" #"removed_goodtrain_withmeans_rangedGPA.arff"
best_set = "goodtrain_SAT_ACT_CONV.arff"
test_set = "TestSetNoLabels.arff"

dataset = {}



def convertMe():
	try:
		f = open(old_set, 'r')
		test_file = open(test_set, 'r')
	except:
		sys.exit("Error: The was a problem opening your file.")
	t = f.read()
	t2 = test_file.read()
	attributes = []
	dataArrays = []
	testData = []
	targets = []
	reachedData = False;
	reachedData2 = False;
	tNL = t.split("\n")
	t2NL = t2.split("\n") # For merging the file
	for s in tNL:
		#print(s)
		if (not reachedData):
			if not s:
				continue
			if (s[0] == '@'):
				tempLine = s.split(" ")
				if (tempLine[0] == "@ATTRIBUTE"): # Add attribute to list of attributes
					tempString = ""
					for x in range(1,len(tempLine)):
						tempString += tempLine[x]
					tempString += " "
					attributes.append(tempString)
				elif (tempLine[0] == "@DATA"):
					reachedData = True
		else:
			if (s[0] == "%"):
				break
			else:
				values = s.split(",")
				# convert to ranged GPA
				if(float(values[-1]) > 3.61):
					values[-1] = '0'
				elif(3.61 >= float(values[-1]) and float(values[-1]) > 3.28):
					values[-1] = '1'
				elif(3.28 >= float(values[-1]) > 2.9):
					values[-1] = '2'
				elif(2.9 >= float(values[-1]) > 2.33):
					values[-1] = '3'
				else:
					values[-1] = '4'

				for val in range(len(values) - 1): # don't convert last values to num
					try:
						values[val] = float(values[val])
						# check to see if it is the mean value for ACTEngWrit
						#if (val == 10):
						#	if (values[val] == 9.39686684073 or
						#		values[val] == 7.20728929385 or
						#		values[val] == 7.99618320611 or
						#		values[val] == 9.13648648649): # IT WAS A MEAN
						#		print("Used SATWriting: " + str(values[6]))
						#		values[val] = sat_to_act_writing(values[6]) # SAT to Writ
						# check to see if it is the mean value for ACTMath
						#if (val == 9):
						#	if (values[val] == 9.90600522193): # IT WAS A MEAN
						#		print("Used SATMath: " + str(values[5]))
						#		values[val] = sat_to_act_writing(values[5]) # SAT to Math
						#if (val == 5): # check to see if it is the mean value for SATWRTG
						#	if (values[val] == 542.872062663): # IT WAS A MEAN
						#		print("Used ACTEngWrit: " + str(values[11]))
						#		values[val] = act_to_sat_writing(values[11]) # SAT to Writ
					except:
						continue
				dataArrays.append(values[:-3]) # not counting the last 3 since we don't know those
				targets.append(values[-1]) # last value is target data
	# For retrieving the Testing Data
	for s in t2NL:
		#print(s)
		if (not reachedData2):
			if not s:
				continue
			if (s[0] == '@'):
				tempLine = s.split(" ")
				#if (tempLine[0] == "@attribute"): # Add attribute to list of attributes
				#	tempString = ""
				#	for x in range(1,len(tempLine)):
				#		tempString += tempLine[x]
				#	tempString += " "
				#	attributes.append(tempString)
				if (tempLine[0] == "@data"):
					reachedData2 = True
		else:
			if (s[0] == "%"):
				break
			else:
				values = s.split(",")
				# convert to ranged GPA
				#if(float(values[-1]) > 3.61):
				#	values[-1] = '0'
				#elif(3.61 >= float(values[-1]) and float(values[-1]) > 3.28):
				#	values[-1] = '1'
				#elif(3.28 >= float(values[-1]) > 2.9):
				#	values[-1] = '2'
				#elif(2.9 >= float(values[-1]) > 2.33):
				#	values[-1] = '3'
				#else:
				#	values[-1] = '4'

				for val in range(len(values)):
					try:
						values[val] = float(values[val])
						# check to see if it is the mean value for ACTEngWrit
						#if (val == 10):
						#	if (values[val] == 9.39686684073 or
						#		values[val] == 7.20728929385 or
						#		values[val] == 7.99618320611 or
						#		values[val] == 9.13648648649): # IT WAS A MEAN
						#		print("Used SATWriting: " + str(values[6]))
						#		values[val] = sat_to_act_writing(values[6]) # SAT to Writ
						# check to see if it is the mean value for ACTMath
						#if (val == 9):
						#	if (values[val] == 9.90600522193): # IT WAS A MEAN
						#		print("Used SATMath: " + str(values[5]))
						#		values[val] = sat_to_act_writing(values[5]) # SAT to Math
						#if (val == 5): # check to see if it is the mean value for SATWRTG
						#	if (values[val] == 542.872062663): # IT WAS A MEAN
						#		print("Used ACTEngWrit: " + str(values[11]))
						#		values[val] = act_to_sat_writing(values[11]) # SAT to Writ
					except:
						continue
				testData.append(values[:]) # not counting the last 3 since we don't know those
				#targets.append(values[-1]) # last value is target data


	ls = {"data": dataArrays, "feature_names": attributes, "target": targets, "test" : testData}
	le_gender = preprocessing.LabelEncoder()
	le_lang = preprocessing.LabelEncoder()
	le_gender.fit(["Male", "Female", "Unknown"])
	le_lang.fit(["English", "EnglishandAnother", "Another"])
	for subj in ls["data"]:
		subj[0]  = le_gender.transform(subj[0]) # Gender
		subj[12] = le_lang.transform(subj[12]) # Languages
	for subj in ls["test"]:
		subj[1]  = le_gender.transform(subj[1]) # Gender
		subj[13] = le_lang.transform(subj[13]) # Languages
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




