print('Should run this command in the Terminal:')
print('> python hide_password.py')

simple = False

if(simple):
	username = input('username: ')
	password = input('password: ')
	print('Logging in...')
else:
	from getpass import getpass
	username = input('username: ')
	password = getpass('password: ')
	print('Logging in...')
