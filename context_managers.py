# DO NOT open a file like this
file = open("file.txt", 'w')
file.write("Hello")
file.close()

'''
Because you may not close the file properly
for example: An error occurs

file = open("file.txt", 'w')
file.write("Hello")asdasdsda # Here the syntax error
file.close()

'''

# Should open a file like this
file = open("file.txt", 'w')
try:
	file.write("Hello")
finally:
	file.close()

# Or like this
with open("file.txt", "w") as file:
	file.write("Hello")
# End - with



print()
print('================')
'''
why this code:

with open("file,txt", "w") as file:
	file.write("Hello")

is good?

OK let's see:
'''

class File():
	"""docstring for File"""
	def __init__(self, filename, method):
		self.file = open(filename, method)

	def __enter__(self):
		print('1. Enter')
		return self.file

	def __exit__(self, type, value, traceback):
		# to handle the exveptions
		print("3. Exit")
		self.file.close()


with File("file.txt", "w") as f:
	print("2. Middle")
	f.write('Hello!')

"""
Return: 
1. Enter
2. Middle
3. Exit

in an right order -> OK!
"""


print()
print('================')
# Run or not
if(False):
	"""
	Now if we have a syntax  error:
	"""
	class File():
		"""docstring for File"""
		def __init__(self, filename, method):
			self.file = open(filename, method)

		def __enter__(self):
			print('1. Enter')
			return self.file

		def __exit__(self, type, value, traceback):
			# to handle the exveptions
			print("3. Exit")
			self.file.close()


	with File("file.txt", "w") as f:
		print("2. Middle")
		f.write('Hello!')
		raise Exception()
	"""
	Still return: 
	1. Enter
	2. Middle
	3. Exit

	in an right order -> The file is always closed -> ok
	"""



print()
print('================')
if(False):
	"""
	Now Check the params: type, value, traceback
	"""
	class File():
		"""docstring for File"""
		def __init__(self, filename, method):
			self.file = open(filename, method)

		def __enter__(self):
			print('1. Enter')
			return self.file

		def __exit__(self, type, value, traceback):
			# to handle the exveptions
			print(f"{type}, {value}, {traceback}")
			print("3. Exit")
			self.file.close()


	with File("file.txt", "w") as f:
		print("2. Middle")
		f.write('Hello!')
		raise Exception()
	"""
	Return: 
	1. Enter
	2. Middle
	<class 'Exception'>, , <traceback object at 0x7fad0b1c0300>
	3. Exit
	Traceback (most recent call last):
	  File ....
	-> THis means we have an exception
	"""

print()
print('================')
'''
To handle this:
We can set return True for __exit__()
'''
if(True):
	"""
	Now Check the params: type, value, traceback
	"""
	class File():
		"""docstring for File"""
		def __init__(self, filename, method):
			self.file = open(filename, method)

		def __enter__(self):
			print('1. Enter')
			return self.file

		def __exit__(self, type, value, traceback):
			# to handle the exveptions
			print(f"{type}, {value}, {traceback}")
			print("3. Exit")
			self.file.close()
			if(type == Exception):
				return True


	with File("file.txt", "w") as f:
		print("2. Middle")
		f.write('Hello!')
		raise Exception()
	"""
	Return: 
	1. Enter
	2. Middle
	<class 'Exception'>, , <traceback object at 0x7f6131a188c0>
	3. Exit
	[Finished in 0.0s]
	-> No error/exception
	"""


print()
print('================')
'''
If we change 
raise Exception() => raise FileExistsError()

We'll still have an exception, but anyway the file will be always closed
'''
if(False):
	"""
	Now Check the params: type, value, traceback
	"""
	class File():
		"""docstring for File"""
		def __init__(self, filename, method):
			self.file = open(filename, method)

		def __enter__(self):
			print('1. Enter')
			return self.file

		def __exit__(self, type, value, traceback):
			# to handle the exveptions
			print(f"{type}, {value}, {traceback}")
			print("3. Exit")
			self.file.close()
			if(type == Exception):
				return True


	with File("file.txt", "w") as f:
		print("2. Middle")
		f.write('Hello!')
		raise FileExistsError()
	"""
	Return: 
	1. Enter
	2. Middle
	<class 'FileExistsError'>, , <traceback object at 0x7f67c810ae40>
	3. Exit
	Traceback (most recent call last):
	  File "/home/kiemhiep/projects/expert_python/context_managers.py", line 222, in <module>
	    raise FileExistsError()
	FileExistsError
	"""





print()
print('================')
'''
Now we're gonna create a Context Manager using decorator and generator
'''
from contextlib import contextmanager

@contextmanager
def file(filename, method):
	print("1. @ Enter")
	# Create a file object
	file = open(filename, method)

	# Enter the file
	yield file

	# Close the file
	file.close()
	print("3. @ Exit")


with file("text.txt", "w") as f:
	print("2. @ Middle")
	f.write("Hello")