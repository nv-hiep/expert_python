a = (1, 2)
print(a)

a = [1, 2]
print(a)



print()
a, b = (1,2)
print(a)
print(b)


a, b = [1,2]
print(a)
print(b)

print()
print("Ignore the second value")
a, _ = [1,2]
print(a)


print()
print("---")
a, b, *c = [1, 2, 3, 4, 5, 6]
print(a)
print(b)
print(c)

print()
print("Ignore some values")
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7]
print(a)
print(b)
print(c)
print(d)

print()
print("Ignore some values")
a, b, *_ = [1, 2, 3, 4, 5, 6]
print(a)
print(b)


print()
print("Ignore some values")
a, b, *_, d = [1, 2, 3, 4, 5, 6]
print(a)
print(b)
print(d)

print()
print("Ignore some values")
a, b, *_, d = [1, 2, 3, 4, 5, 6, 7]
print(a)
print(b)
print(d)