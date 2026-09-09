# quite a few IF and ELIF conditions for AGE GROUPS

name = input("What is your name? --->")
age = int(input("What is your age? --->"))

if age >= 0 and age <=5 :
	print("You will be part of the INFANT group age.")
elif age >= 6 and age <=12 :
	print("You will be part of the KID group age.")
elif age >= 13 and age <=15 :
	print("You will be part of the PRE-TEEN group age.")
elif age >= 6 and age <=19 :
	print("You will be part of the TEENAGER group age.")
elif age >= 20 and age <=25 :
	print("You will be part of the EARLY ADULTHOOD group age.")
elif age >= 26 and age <=29 :
	print("You will be part of the MID ADULTHOOD group age.")
elif age >= 30 and age <=58 :
	print("You will be part of the ADULTHOOD group age.")
elif age >= 59 and age <=150 :
	print("You will be part of the SENIOR group age.")
elif age >=151 :
	print("Woah now—! Are you for real-real? You must be a bot.")