

def sat_to_act_writing(sat_score):
	if(sat_score > 770):
		return 36
	elif (770 > sat_score >= 740):
		return 35
	elif (740 > sat_score >= 710):
		return 33
	elif (710 > sat_score >= 680):
		return 32
	elif (680 > sat_score >= 650):
		return 31
	elif (650 > sat_score >= 620):
		return 29
	elif (620 > sat_score >= 590):
		return 27
	elif (590 > sat_score >= 560):
		return 25
	elif (560 > sat_score >= 530):
		return 24
	elif (530 > sat_score >= 500):
		return 22
	elif (500 > sat_score >= 470):
		return 20
	elif (470 > sat_score >= 440):
		return 19
	elif (440 > sat_score >= 410):
		return 16
	elif (410 > sat_score >= 380):
		return 14
	elif (380 > sat_score >= 350):
		return 13
	elif (350 > sat_score >= 320):
		return 11
	elif (320 > sat_score >= 290):
		return 9
	elif (290 > sat_score):
		return 8

	return 0


print sat_to_act_writing(410)