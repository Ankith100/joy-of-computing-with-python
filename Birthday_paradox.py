import random
import datetime
def repeated_birthdays(a):
	duplicates=[]
	for i in range(1,len(a)):
		if a[i]==a[i-1] and a[i] not in duplicates:
			duplicates.append(a[i])
	print(duplicates)
birthday=[]
i=0
months=list(range(1,13))
while i<50:
	year=random.randint(1890,2020)
	if year%4==0 and year %100!=0 or year%400==0 :
		leap=1
	else:
		leap=0
	month=random.randint(1,12)
	if month==2 and leap==0:
		day=random.randint(1,28)
	elif month==2 and leap==1:
		day=random.randint(1,29)
	elif month in [1,3,5,7,8,10,12]:
		day=random.randint(1,31)
	else:
		day=random.randint(1,30)
	dd=datetime.date(year,month,day)
	day_of_year=dd.timetuple().tm_yday
	i+=1
	birthday.append(day_of_year)
birthday.sort()
i=0
print("Different Birthday days in a year generated using random module:")
while i<50:
	print(birthday[i],end="  ")
	i+=1
print('\nSame day birthdays are:')
repeated_birthdays(birthday)