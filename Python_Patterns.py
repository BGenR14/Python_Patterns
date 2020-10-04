print("Number 1")
print()
n = 10 # Can also be entered from user too
for i in range(1, n + 1):
	print("*"*n)

print()
print("Number 2")
print()

n = 9 # Can also be entered from user too
for i in range(1, n + 1):
	for j in range(1, n + 1):
		print(i, end = " ")
	print()

print()
print("Number 3")
print()

n = 10 # Can also be entered from user too
for i in range(1, n + 1):
	for j in range(1, n + 1):
		print(j, end = " ")
	print()

print()
print("Number 4")
print()

for i in range(1, n + 1):
	for j in range(1, n + 1):
		print(chr(64 + i), end = " ")
	print()

print()
print("Number 5")
print()

for i in range(1, n + 1):
	for j in range(1, n + 1):
		print(chr(64 + j), end = " ")
	print()

print()
print("Number 6")
print()

for i in range(1, n + 1):
	for j in range(1, i + 1):
		print("*", end = " ")
	print()

print()
print("Number 7")
print()

n = 9
for i in range(1, n + 1):
	for j in range(1, i + 1):
		print(i, end = " ")
	print()


print()
print("Number 8")
print()

n = 10
for i in range(1, n + 1):
	for j in range(1, i + 1):
		print(j, end = " ")
	print()


print()
print("Number 9")
print()

for i in range(1, n + 1):
	for j in range(1, i + 1):
		print(chr(64 + i), end = " ")
	print()

print()
print("Number 10")
print()

for i in range(1, n + 1):
	for j in range(1, i + 1):
		print(chr(64 + j), end = " ")
	print()

print()
print("Number 11")
print()

for i in range(1, n + 1):
	for j in range(1, n + 2 - i):
		print("*", end = " ")
	print()

print()
print("Number 12")
print()

n = 9
for i in range(1, n + 1):
	for j in range(1, n + 1 - i):
		print(i, end = " ")
	print()


print()
print("Number 13")
print()

n = 10
for i in range(1, n + 1):
	for j in range(1, n + 2 - i):
		print(j, end = " ")
	print()
