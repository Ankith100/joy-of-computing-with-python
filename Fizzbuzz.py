#This is a game that is played by a small group
#Everyone starts telling numbers consecutively and fastly without stopping 
#The one who get number that is divisible by 3 will tell Fizz
#The one who get number that is divisible by 5 will tell Buzz
#The one who get number that is divisible by 3 and 5 will tell FizzBuzz
#If we a person don't tell correctly we will be out of game and game continues till there will be one guy left - winner.
for i in range(1,101):
	if i%3==0 and i%5==0:
		print(i,"Fizzbuzz")
	elif i%3==0:
		print(i,"Fizz")
	elif i%5==0:
		print(i,"Buzz")
	else:
		print(i)
