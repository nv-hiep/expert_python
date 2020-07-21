print("With many zeros.. hard to read: ")
a = 10000000000
b = 100000000

total = a + b

print(f"{total}")

print()
print("Use this code: ")
a = 10_000_000_000
b = 100_000_000

total = a + b

print(f"{total:,}") # Use fstring with ":,"