import inspect
from queue import Queue

class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		# super(Person, self).__init__()
		self.name = name

	def __repr__(self):
		return f'Person({self.name})'

	def __mul__(self, x):
		if type(x) is not int:
			raise Exception('Invalid arg, must be Int')
		self.name = self.name * 4

	def __call__(self, y):
		print(y)

	def __len__(self):
		return len(self.name)


p = Person('Lucy')
p * 4
print(p)

p(4)
print(len(p))

print()
q = Queue()
print(q)
print(inspect.getsource(Queue))

class Queue(Queue):
	"""docstring for Queue"""
	def __repr__(self):
		return f'Queue({self._qsize()})'

	def __add__(self, item):
		self.put(item)

	def __sub__(self, item):
		self.get()


qu = Queue()
print(qu)
qu + 9
print(qu)
qu + 7
print(qu)
qu - None
print(qu)
