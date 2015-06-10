# Craig Collins
# CMPS 142
# Run by using python3
# then just type "import BruteForceParameters as BFP"

import arffToScikit as ARF
import sys
import string
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation



# Vars to iterate over
min_samples_leaf_MIN = 4
min_samples_leaf_MAX = 8
min_samples_split_MIN = 2
min_samples_split_MAX = 6
min_weight_fraction_leaf_MIN = 0.0
min_weight_fraction_leaf_MAX = 0.0
n_estimator_MIN = 1000
n_estimator_MAX = 1001
cross_validation_MAX = 10
n_jobs_VALUE = 1
max_features_VALUE = 'auto'


clff = RandomForestClassifier()
# Data
data = ARF.convertMe()
print (data["feature_names"])

# Resulting Data

# Example
# RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
#            max_depth=None, max_features='auto', max_leaf_nodes=None,
#            min_samples_leaf=1, min_samples_split=2,
#            min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
#            oob_score=False, random_state=None, verbose=0,
#            warm_start=False)

def main():
	# Declare Globlas
	global clff
	global data
	resultMatrix = []
	# initialize the list
	X = data["data"]
	Y = data["target"]
	MAX_AVGSCORE = 0.0
	MAX_S = ""
	clff = RandomForestClassifier(min_samples_split=min_samples_split_MIN, n_estimators=n_estimator_MIN)
	iteration = 0
	for m_s_s in range(min_samples_split_MIN, min_samples_split_MAX): # loop through min_sample_leaf
		for m_s_l in range(min_samples_leaf_MIN, min_samples_leaf_MAX): # loop through min_sample_leaf
			for n_est in range(n_estimator_MIN, n_estimator_MAX): # loop through n_estimator
				# initialize the list
				resultMatrix.append([])
				clff = RandomForestClassifier(
					min_samples_leaf=m_s_l,
					min_samples_split=m_s_s,
					n_estimators=n_est,
					n_jobs=n_jobs_VALUE,
					max_features=max_features_VALUE)
					#class_weight={"9" : 0.4})
				for cv in range(cross_validation_MAX): # Iterate some number of splits
					# Create Dictionary to hold data
					tempD = { \
						"min_samples_split" : m_s_s, \
						"min_samples_leaf" : m_s_l, \
						"n_estimator" : n_est, \
						"random_state" : cv, \
						"score" : 0.0 }
					X1, X2, Y1, Y2 = cross_validation.train_test_split(X, Y, test_size=0.1, random_state=cv)
					clff.fit(X1, Y1)
					#X3 = clff.transform(X1, 0.03)
					#X4 = clff.transform(X2, 0.03)
					#clff.fit(X3, Y1)
					tempD["score"] = clff.score(X2, Y2)
					resultMatrix[iteration].append(tempD)
				# average them
				totalScore = 0
				for x in range(cross_validation_MAX):
					tempScore = resultMatrix[iteration][x]["score"]
					totalScore += tempScore
				avgScore = float(totalScore) / float(cross_validation_MAX)
				tempD = {"AverageScore" : avgScore}
				resultMatrix[iteration].append(tempD)
				s = str(resultMatrix[iteration][cross_validation_MAX]["AverageScore"]) + " : (" + str(resultMatrix[iteration][cross_validation_MAX - 1]["min_samples_split"]) + ", " + \
					str(resultMatrix[iteration][cross_validation_MAX - 1]["min_samples_leaf"]) + ", " + str(resultMatrix[iteration][cross_validation_MAX - 1]["n_estimator"]) + ")"
				print(s)

				# Track MAX_AVGSCORE and store string
				if (avgScore > MAX_AVGSCORE):
					MAX_AVGSCORE = avgScore
					MAX_S = (s + '.')[:-1]
					print("**New Maximum**")
				# increment iteration
				iteration = iteration + 1
	print ("Total iterations: " + str(iteration))
	return resultMatrix, MAX_AVGSCORE, MAX_S

result, max_score, parameters= main()
print(max_score, "---", parameters)

def returnCLF():
	return clff
# Display results
#for x in range(len(result)):
	#print(result[x])
	#print(str(result[x][cross_validation_MAX]["AverageScore"]) + " : (" + str(result[x][cross_validation_MAX - 1]["min_samples_split"]) + ", " + \
		#str(result[x][cross_validation_MAX - 1]["min_samples_leaf"]) + ", " + str(result[x][cross_validation_MAX - 1]["n_estimator"]) + ")" )



