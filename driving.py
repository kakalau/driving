country = input ('which country do you live: ')
age = input('How old are you: ')
age = int(age)
if country =='Taiwan':
	if age >=18:
		print('You can drive')
	else:
		print('You cannot drive')
elif country == 'America':
	if age >=16:
		print('You can drive')
	else:
		print('You cannot drive')
else:
	print('You can only input Taiwan or America')