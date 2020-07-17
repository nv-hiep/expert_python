'''
Decorator
'''
def func(string):
	def wrapper():
		print('-> Started')
		print('string')
		print('<- Ended')
	return wrapper()


x = func('hello')


print()
print('================')


'''
Decorator
'''
def func(string):
	def wrapper():
		print('-> Started')
		print('string')
		print('<- Ended')
	return wrapper # withour brackets


x = func('hello') # print nothing
print(x)

# now
x()  # print string



print()
print('================')



'''
Decorator
'''
def func(fcn):
	def wrapper():
		print('-> Started')
		fcn()
		print('<- Ended')
	return wrapper # withour brackets



def func2():
	print('I am func2')


def func3():
	print('I am func3')


x = func(func2) # print nothing
print(x)
x()


y = func(func3) # print nothing
print(y)
y()



print()
print('================')



'''
Decorator
'''
def func(fcn):
	def wrapper():
		print('-> Started')
		fcn()
		print('<- Ended')
	return wrapper # withour brackets



def func2():
	print('I am func2')


def func3():
	print('I am func3')


# Like a decorator
func3 = func(func3)
func3()


func2 = func(func2)
func2()


print()
print('================')


'''
Decorator: Python has a better syntax
'''
def func(fcn):
	def wrapper():
		print('-> Started')
		fcn()
		print('<- Ended')
	return wrapper # withour brackets



# a decorator with @
@func
def func2():
	print('I am func2')

@func
def func3():
	print('I am func3')



func3()

func2()


print()
print('================')


'''
Decorator: now an error
'''
def func(fcn):
	def wrapper():
		print('-> Started')
		fcn()
		print('<- Ended')
	return wrapper # withour brackets



# a decorator with @
@func
def func2(x):
	print(x)

@func
def func3():
	print('I am func3')



func3()

# func2(5) # -> error
# TypeError: wrapper() takes 0 positional arguments but 1 was given
# Because it runs the function wrapper


print()
print('================')



'''
Decorator: a way to fix the error above
'''
def func(fcn):
	def wrapper(x):
		print('-> Started')
		fcn(x)
		print('<- Ended')
	return wrapper # withour brackets



# a decorator with @
@func
def func2(x):
	print(x)

@func
def func3():
	print('I am func3')



func2(5) # -> No error, printed "5"

# But
# func3() #-> error
# TypeError: wrapper() missing 1 required positional argument: 'x'


print()
print('================')


'''
Decorator: a way to fix the error above
'''
def func(fcn):
	def wrapper(*args, **kwargs):
		print('-> Started')
		fcn(*args, **kwargs)
		print('<- Ended')
	return wrapper # withour brackets



# a decorator with @
@func
def func2(x, y):
	print(x, y)

@func
def func3():
	print('I am func3')



func2(5,9) # -> No error, printed "5"

# OK now
func3() #-> No error


print()
print('================')




'''
Decorator: but now we want to return y in func2
'''
def func(fcn):
	def wrapper(*args, **kwargs):
		print('-> Started')
		fcn(*args, **kwargs)
		print('<- Ended')
	return wrapper # withour brackets



# a decorator with @
@func
def func2(x, y):
	print(x, y)
	return y

@func
def func3():
	print('I am func3')



z = func2(5,9) 
print('z = ', z) # -> None


print()
print('================')



'''
Decorator: fx by returning value from wrapper
'''
def func(fcn):
	def wrapper(*args, **kwargs):
		print('-> Started')
		ret = fcn(*args, **kwargs)
		print('<- Ended')
		return ret

	return wrapper # withour brackets



# a decorator with @
@func
def func2(x, y):
	print(x, y)
	return y

@func
def func3():
	print('I am func3')



z = func2(5,9) 
print('z = ', z) # return '9'


print()
print('================')




'''
Decorator: an application
'''
import time

def timer(fcn):
	def wrapper(*args, **kwargs):
		start = time.time()
		ret   = fcn(*args, **kwargs)
		total = time.time() - start
		print('Time: ', total)
		return ret

	return wrapper # withour brackets



# a decorator with @
@timer
def test():
	for _ in range(100000):
		pass


@timer
def test2():
	time.sleep(2)


test()
test2()

print()
print('================')



'''
'''
