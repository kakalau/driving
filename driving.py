country = input ('which country do you live: ')
age = input('How old are you: ')
age = int(age)
if country =='Taiwan':
	if age >=18:
		print('You can drive')
	else:
		print('You cannot drive')