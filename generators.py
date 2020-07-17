"""
We have limit RAM and memory
"""

# This code will raise errors with N = 100000000000
N = 100000000000
N = 10           # A small integer to run, but you can check with N = 100000000000
x = [i**2 for i in range(N)]

for xi in x:
	print(xi)

# -> MemoryError


"""
How to fix ? Use a generator !

It just looks at ONE value at a time, and 
does not stores the entire sequence of numbers
When we dont need to do that
""" 

# For example: with N = 100000000000
N = 100000000000
N = 10
for i in range(N):
	print(i)


print()
print('================')
class Gen:
	"""docstring for Gen"""
	def __init__(self, n):
		self.n    = n
		self.last = 0

	def __next__(self):
		return self.next()

	def next(self):
		if(self.last == self.n):
			raise StopIteration()

		ret = self.last**2
		self.last += 1
		return ret

# Check
N = 10000000000
N = 1000
g = Gen(N)
while True:
	try:
		print( next(g) )
	except StopIteration:
		break



print()
print('================')
def gen(n):
	for i in range(n):
		yield i**2

g = gen(10000)

for i in g:
	print(i)



print()
print('================')
print('You can use "next" to see how "yeild" works: ')
def gen(n):
	for i in range(n):
		yield i**2

g = gen(10000)
print(next(g))
print(next(g))
print(next(g))
print(next(g))



print()
print('================')
print('You can use many "yield"s: ')
def gen(n):
	for i in range(n):
		yield 1
		yield 2
		yield 5
		yield 7
		yield 10
		yield 100
		yield 1000
		yield 10000
		yield 100000

g = gen(10000)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


print()
print('================')
print('Check the memories: ')
import sys

def gen(n):
	for i in range(n):
		yield i**2

x = [i**2 for i in range(10000)]
g = gen(10000)

print(sys.getsizeof(x))
print(sys.getsizeof(g))


print()
print('================')