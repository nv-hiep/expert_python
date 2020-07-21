def squared(func):
	return lambda x: func(x) * func(x)


@squared
def double(x):
	return 2*x


print(double(5))


print()
print('==================')
def squared(func):
	def wrapper(x):
		return func(x) * func(x)		
	return wrapper


@squared
def double(x):
	return 2*x

print(double(5))


print()
print('==================')
def squared(func):
	def wrapper(x):
		return func(x) * func(x)		
	return wrapper


def double(x):
	return 2*x


double = squared(double)
print(double(5))













print()
print('==================')
def triple(func):
	def wrapper(x):
		return 3. * func(x)
	return wrapper


def double(x):
	return 2*x


double = triple(double)
print(double(5))



print()
print('==================')
def triple(func):
	def wrapper(x):
		return 3. * func(x)
	return wrapper

@triple
def double(x):
	return 2*x

print(double(5))



'''
--------------------------------
'''

print()
print('==================')
def prepend_a_string(func):
	def wrapper(x):
		return 'This is the result : ' + str( func(x) )
	return wrapper

@prepend_a_string
def double(x):
	return 2*x

print(double(5))





print()
print('Same as:')
def prepend_a_string(func):
	def wrapper(x):
		return 'This is the result : ' + str( func(x) )
	return wrapper



def double(x):
	return 2*x


double = prepend_a_string(double)

print(double(5))
