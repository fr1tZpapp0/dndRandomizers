from random import randint, choice


# CURRENCY TYPES = CP, SP, EP, GP, PP

currencyRange = randint(1, 100)


tinyRange = randint(1, 5)
basicRange = randint(1, 25)
mediumRange = randint(50, 100)
highRange = randint(250, 1350)
insaneRange = randint(1400, 50000)


def randomizeLoot(level):
	
	if 1 <= level <= 5: # LEVELS 1-5
		if 1 <= currencyRange <= 20:
			print(str(basicRange) + " " + "CP")

		elif 20 < currencyRange <= 40:
			print(str(basicRange) + " " + "SP")

		elif 40 < currencyRange <= 60:
			print(str(basicRange) + " " + "EP")

		elif 60 < currencyRange <= 80:
			print(str(basicRange) + " " + "GP")

		elif 80 < currencyRange <= 100:
			print(str(tinyRange) + " " + "PP")


	elif 5 < level <= 10: # LEVELS 6-10
		if 1 <= currencyRange <= 20:
			print(str(mediumRange) + " " + "CP")

		elif 20 < currencyRange <= 40:
			print(str(mediumRange) + " " + "SP")

		elif 40 < currencyRange <= 60:
			print(str(mediumRange) + " " + "EP")

		elif 60 < currencyRange <= 80:
			print(str(mediumRange) + " " + "GP")

		elif 80 < currencyRange <= 100:
			print(str(basicRange) + " " + "PP")


	elif 10 < level <= 15: # LEVELS 11 - 15
		if 1 <= currencyRange <= 20:
			print(str(highRange) + " " + "CP")

		elif 20 < currencyRange <= 40:
			print(str(highRange) + " " + "SP")

		elif 40 < currencyRange <= 60:
			print(str(highRange) + " " + "EP")

		elif 60 < currencyRange <= 80:
			print(str(highRange) + " " + "GP")

		elif 80 < currencyRange <= 100:
			print(str(mediumRange) + " " + "PP")


	elif 15 < level <= 20: # LEVELS 16 +
		if 1 <= currencyRange <= 20:
			print(str(insaneRange) + " " + "CP")

		elif 20 < currencyRange <= 40:
			print(str(insaneRange) + " " + "SP")

		elif 40 < currencyRange <= 60:
			print(str(insaneRange) + " " + "EP")

		elif 60 < currencyRange <= 80:
			print(str(insaneRange) + " " + "GP")

		elif 80 < currencyRange <= 100:
			print(str(highRange) + " " + "PP")

	else: # NOT A VALID LEVEL OBVIOUSLY
		print("NOT VALID LEVEL")