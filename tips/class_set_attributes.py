class Person():
	"""docstring for Person"""
	pass


# add attribute
person = Person()


person.first ='First'
person.last  ='Last'

print(person.first)
print(person.last)


print()
print("===============")
print("Use setattr:")
# add attribute
person = Person()


first_key = 'first'
first_val = 'First Value'

setattr(person, first_key, first_val)
print(person.first)


first = getattr(person, first_key)
print(first)


print()
print("===============")
print("Use setattr with a loop:")
# add attribute
person = Person()


person_info = {'first' : 'First Value',
                'last' : 'Last Value'}

for key, val in person_info.items():
	setattr(person, key, val)

print(person.first)
print(person.last)


print()
for key in person_info.keys():
	print( getattr(person, key) )