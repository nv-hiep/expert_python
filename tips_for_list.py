print()
print('================')
print('Replace one/more consecutive elements by others:')


l = list(range(3))
print(l)

ll = l[:1]
print(ll)
l[:1] = [8,9,10]
print(l)

print()
print('================')
print('Invert the list:')


l = list(range(10))
print(l)
print(l[::-1])



print()
print('================')
print('Return and Yield:')

nums = [4,3,2,1]

print('Return: ')
def squared(nums):
	ret = []
	for num in nums:
		ret.append(num*num)
	return ret

print(squared(nums))


print('Yield:')
def squared(nums):
	for num in nums:
		yield num*num

for num in squared(nums):
	print(num)