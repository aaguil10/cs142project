

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


def sat_to_act_tota1(sat_score):
	if(sat_score > 2390):
		return 36
	elif (2390 > sat_score >= 2330):
		return 35
	elif (2330 > sat_score >= 2250):
		return 34
	elif (2250 > sat_score >= 2180):
		return 33
	elif (2180 > sat_score >= 2120):
		return 32
	elif (2120 > sat_score >= 2060):
		return 31
	elif (2060 > sat_score >= 2000):
		return 30
	elif (2000 > sat_score >= 1940):
		return 29
	elif (1940 > sat_score >= 1880):
		return 28
	elif (1880 > sat_score >= 1820):
		return 27
	elif (1820 > sat_score >= 1770):
		return 26
	elif (1770 > sat_score >= 1710):
		return 25
	elif (1710 > sat_score >= 1650):
		return 24
	elif (1650 > sat_score >= 1590):
		return 24
	elif (1590 > sat_score >= 1530):
		return 23
	elif (1530 > sat_score >= 1470):
		return 22
	elif (1470 > sat_score >= 1410):
		return 21
	elif (1410 > sat_score >= 1350):
		return 20
	elif (1350 > sat_score >= 1290):
		return 19
	elif (1290 > sat_score >= 1230):
		return 18
	elif (1230 > sat_score >= 1170):
		return 17
	elif (1170 > sat_score >= 1100):
		return 16
	elif (1100 > sat_score >= 1020):
		return 15
	elif (1020 > sat_score >= 950):
		return 14
	elif (950 > sat_score >= 870):
		return 13
	elif (870 > sat_score >= 780):
		return 12
	elif (780 > sat_score):
		return 11
	return 0


def act_to_sat_writing(act_score):
	if(act_score == 36):
		return 800
	elif (act_score == 35):
		return 770
	elif (act_score == 33):
		return 740
	elif (act_score == 32):
		return 710
	elif (act_score == 31):
		return 680
	elif (act_score == 29):
		return 650
	elif (act_score == 27):
		return 620
	elif (act_score == 25):
		return 590
	elif (act_score == 24):
		return 560
	elif (act_score == 22):
		return 530
	elif (act_score == 20):
		return 500
	elif (act_score == 19):
		return 470
	elif (act_score == 16):
		return 440
	elif (act_score == 14):
		return 410
	elif (act_score == 13):
		return 380
	elif (act_score == 11):
		return 350
	elif (act_score == 9):
		return 320
	elif (act_score == 8):
		return 290
	return 0

def act_to_sat_math(act_score):
	if(act_score == 36):
		return 800
	elif (act_score == 33):
		return 770
	elif (act_score == 31):
		return 740
	elif (act_score == 30):
		return 710
	elif (act_score == 28):
		return 680
	elif (act_score == 26):
		return 650
	elif (act_score == 25):
		return 620
	elif (act_score == 24):
		return 590
	elif (act_score == 22):
		return 560
	elif (act_score == 21):
		return 530
	elif (act_score == 19):
		return 500
	elif (act_score == 17):
		return 470
	elif (act_score == 16):
		return 440
	elif (act_score == 15):
		return 410
	elif (act_score == 14):
		return 350
	elif (act_score == 13):
		return 290
	return 0


print act_to_sat_math(31)