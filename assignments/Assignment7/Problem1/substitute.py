
readfile = open('u.user', 'r')

for line in readfile:
	(userid, age, gender, occupation, zipcode) = line.split('|')
	if age == '27' and gender == 'M' and occupation == 'student':
		print userid, age, gender, occupation, zipcode
		
