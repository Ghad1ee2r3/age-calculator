from datetime import datetime

def check_birthdate(year, month, day):
	# write code here
	year= int(year)
	month= int(month)
	day= int(day)
	today = datetime.today()
	#dU=datetime.datetime(year, month, day)
	#if du> today:
	#	return False
	#else:
	#	return True

	#if year==2020 and month>today.month and day>today.day:
	#			return False

	if year<today.year  :
		return True
	elif month<today.month:
		return True
	else:
		if day<today.day:
			return True
		else:
			return False

	#else:
	#	return True


def calculate_age(year, month, day):
    # write code here
	today = datetime.today()
	year= int(year)
	month= int(month)
	day= int(day)
	age= (today.year- year)+(((today.month-month)+(today.day-day))/360)
	age=int(age)
	print ("You are "+str(age)+" years old ")

def main():
	# write main code here

	year= input("Enter year of birth: ")
	month=input("Enter month of birth:")
	day = input("Enter day of birth:")


	if check_birthdate(year, month, day)== True:
		calculate_age(year, month, day)
	else:
		print ("the birthdate is invalid")



if __name__ == '__main__':
	main()
