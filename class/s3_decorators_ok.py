"""
Decorators
"""
def outer_function():
	msg = 'Hi'

	def inner_function():
		print( msg )

	return inner_function() # with brackets


outer_function()


print()
print('=============')
print()

"""
or
"""
def outer_function():

	msg = 'Hi'

	def inner_function():
		print( msg )

	return inner_function # without brackets


x = outer_function()
x()
x()


print()
print('=============')
print()

"""
Decorator
"""
def outer_function(msg):

	def inner_function():
		print( msg )

	return inner_function # without brackets


hi_fcn = outer_function('Hi')
bi_fcn = outer_function('Bye')

hi_fcn()
bi_fcn()


print()
print('=============')
print()



"""
Decorator
"""
def decorator_function(original_function):

	def wrapper_function():
		return original_function()

	return wrapper_function # without brackets


def display():
	print('Display function ran')


decorated_display = decorator_function(display)	
decorated_display()

"""
Decorating a function allows to easily add functionalities 
to the existing function by adding the
functionalities into the wrapper
For example:
"""

print()
print('=============')
print()



"""
Decorator
"""
def decorator_function(original_function):

	def wrapper_function():
		print('wrapper executed this before - {}'.format(original_function.__name__))
		return original_function()

	return wrapper_function # without brackets



# add @decorator_function
# the same as:
# display = decorator_function(display)	

@decorator_function
def display():
	print('Display function ran')


display()

"""
So, to highlight:

@decorator_function
def display():
	print('Display function ran')



is the same as:
def display():
	print('Display function ran')


display = decorator_function(display)
"""




print()
print('=============')
print()
"""
Decorator
"""
def decorator_function(original_function):

	def wrapper_function():
		print('wrapper executed this before - {}'.format(original_function.__name__))
		return original_function()

	return wrapper_function # without brackets



# add @decorator_function
# the same as:
# display = decorator_function(display)	

@decorator_function
def display():
	print('Display function ran')

# the following code will raise an error
# TypeError: wrapper_function() takes 0 positional arguments but 2 were given

# @decorator_function
# def display_info(name, age):
# 	print('display_info ran with arguments ({}, {})'.format(name, age))


# display_info('Bin', 25)






print()
print('=============')
print()
"""
Decorator: how to fix ?
"""
def decorator_function(original_function):

	def wrapper_function(*args, **kwargs):
		print('wrapper executed this before - {}'.format(original_function.__name__))
		return original_function(*args, **kwargs)

	return wrapper_function # without brackets



# add @decorator_function
# the same as:
# display = decorator_function(display)	

@decorator_function
def display():
	print('Display function ran')

# the following code runs OK
@decorator_function
def display_info(name, age):
	print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Bin', 25)




print()
print('=============')
print()

"""
Decorator class, if you like to use decorator class instead of decorator function
"""

class decorator_class(object):
	"""docstring for decorator_class"""
	def __init__(self, original_function):
		# super(decorator_class, self).__init__()
		self.original_function = original_function

	def __call__(self, *args, **kwargs):
		print('Call method executed this before - {}'.format(self.original_function.__name__))
		return self.original_function(*args, **kwargs)
		


@decorator_class
def display():
	print('Display function ran')

@decorator_class
def display_info(name, age):
	print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Bin', 25)





print()
print('=============')
print('An application with decorator_function')
print()
"""
Decorator:
"""
def my_logger(orig_fcn):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_fcn.__name__), level=logging.INFO )

	def wrapper(*args, **kwargs):
		logging.info(
			'Ran with arguments and kwargs ({}, {})'.format(args, kwargs)
			)
		return orig_fcn(*args, **kwargs)

	return wrapper


def my_timer(orig_fcn):
	import time

	def wrapper(*args, **kwargs):
		t1     = time.time()
		result = orig_fcn(*args, **kwargs)
		t2     = time.time() - t1
		print('{} ran in: {} sec'.format(orig_fcn.__name__, t2))

		return result

	return wrapper


@my_logger
def display_info(name, age):
	print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Tim', 30)




print()
print('=============')
print('An application with decorator_function, with my_timer')
print()
"""
Decorator:
"""
def my_logger(orig_fcn):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_fcn.__name__), level=logging.INFO )

	def wrapper(*args, **kwargs):
		logging.info(
			'Ran with arguments and kwargs ({}, {})'.format(args, kwargs)
			)
		return orig_fcn(*args, **kwargs)

	return wrapper


def my_timer(orig_fcn):
	import time

	def wrapper(*args, **kwargs):
		t1     = time.time()
		result = orig_fcn(*args, **kwargs)
		t2     = time.time() - t1
		print('{} ran in: {} sec'.format(orig_fcn.__name__, t2))

		return result

	return wrapper


import time

@my_timer
def display_info(name, age):
	time.sleep(1)
	print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Tim', 30)




print()
print('=============')
print('An application with decorator_function')
print('Stacking decorator_functions')
print()

"""
Decorator: see https://www.youtube.com/watch?v=FsAPt_9Bf3U
"""
from functools import wraps

def my_logger(orig_fcn):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_fcn.__name__), level=logging.INFO )

	@wraps(orig_fcn)
	def wrapper(*args, **kwargs):
		logging.info(
			'Ran with arguments and kwargs ({}, {})'.format(args, kwargs)
			)
		return orig_fcn(*args, **kwargs)

	return wrapper


def my_timer(orig_fcn):
	import time

	@wraps(orig_fcn)
	def wrapper(*args, **kwargs):
		t1     = time.time()
		result = orig_fcn(*args, **kwargs)
		t2     = time.time() - t1
		print('{} ran in: {} sec'.format(orig_fcn.__name__, t2))

		return result

	return wrapper


import time

@my_logger
@my_timer
def display_info(name, age):
	time.sleep(1)
	print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Timm', 35)