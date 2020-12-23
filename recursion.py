

# factorial recursion

def recur_factorial(n):
	# base case
	if n == 1:
		return n
	else:
		return n * recur_factorial(n-1)

print(recur_factorial(5))

# recursion calculate the sum of a list of numbers

def recur_list_sum(lis):
	# base case
	if len(lis) == 1:

		return lis[0]
	# recursive case
	else:
		return lis[0] + recur_list_sum(lis[1:])

print(recur_list_sum([1,2,3,4,5]))

# fibonacci sequence

def recur_fibonacci(n):
	if n <=1:
		return n
	else:
		return (recur_fibonacci(n-1) + recur_fibonacci(n-2))

for i in range(10):
	print(recur_fibonacci(i))

# harmonic sum ( 1 + 1/2 + 1/3 + 1/4 + ............)

def harmonic_sum(n):
	if n <= 1:
		return 1
	else:
		return 1/n + harmonic_sum(n-1)

print(harmonic_sum(7))


