class Test(object):
	"""Class itself is an object"""
	pass


print(Test)
print( Test() )
print(type( Test() ))

def fcn():
	pass

print(type(fcn))

print()
print('================')

'''
These two things below are equivalent
'''

class Test():
	pass

Test = type( 'Test', (), {} )
Test = type( 'Test', (), {'x':5} )
#           name - inherit - attributes

print( Test )
print(Test())

t = Test()
print(t.x)

t.say = 'Hello'
print(t.say)



print()
print('================')
# Inherite
class Foo:
	def show(self):
		print('Hi')


Test = type( 'Test', (Foo,), {'x':5} )
t = Test()
t.show()


# Add a function
def add_attribute(self):
	self.z = 10


Test = type( 'Test', (Foo,), {'x':5, 'add_attribute': add_attribute} )
t = Test()
t.add_attribute()
print(t.z)


print()
print('================')


'''
Metaclass
'''
class Meta(type):

	def __new__(self, class_name, bases, attrs):
		""" before __init__ method """
		print(attrs)
		return type(class_name, bases, attrs)


class Dog(metaclass=Meta):
	x = 5
	y = 8

	def hello(self):
		print('Hi!')

# d =  Dog()



print()
print('================')


'''
Metaclass - change to UPPERCASE
'''
class Meta(type):

	def __new__(self, class_name, bases, attrs):
		""" before __init__ method """
		
		print(attrs)
		a ={}
		for name, val in attrs.items():
			if(name.startswith('__')):
				a[name] = val
			else:
				a[name.upper()] = val
		
		print(a)
		return type(class_name, bases, a)


class Dog(metaclass=Meta):
	x = 5
	y = 8

	def hello(self):
		print('Hi!')


d = Dog()
# print(d.x) # -> Error
print(d.X)

# print(d.hello()) # -> Error
print(d.HELLO()) # We already changed the construcion of the attributes


print()
print('================')


'''
'''
