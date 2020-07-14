import inspect
from queue import Queue

'''
Create classes inside a function
'''
def create_class(x):
	class Dog:
		"""docstring for Dog"""
		def __init__(self, name):
			# super(Dog, self).__init__()
			self.name = name

		def print_val(self):
			print(x)

	return Dog


cls = create_class(10)

print(cls)

d = cls('Bin')

print(d.name)
d.print_val()




'''
create functions inside a loop
'''
for i in range(10):
	def show():
		print(i*2)

	show()


'''
Functions inside a function
'''
def fcn(x):
	if x == 1:
		def return_val():
			print('X is 1')
	else:
		def return_val():
			print(' X is not 1 ')
	return return_val

new_fcn = fcn(2)
new_fcn()
print('The ID of the function: ', id(new_fcn) )

print( inspect.getmembers(new_fcn) )
print()
print( inspect.getsource(new_fcn) )


print()
print('To see the source code of a built-in module')
print( inspect.getsource(Queue) )