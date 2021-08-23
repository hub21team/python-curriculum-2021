"""
You will implement the Eratosthene’s method to find prime numbers less than or equal to a given integer n, which is as follows:
- Create a list of numbers from 2 to n
- Mark all numbers that are divisible by 2 and are greater than or equal to the square of it.
- Repeat the above step for every unmarked number in the list. (ie. you will check for 3, 5, 7, and so on right after this step)
- Unmarked numbers yield the primes. 
"""
def sieve_of_eratosthene(n):
    is_prime = [True] * (n-1)
    for i in range(2, n+1):
        # i'th entry in is_prime reflects if the number (i+2) is a prime or not
        if is_prime[i-2]:
            # when i=2, iterate over 4, 6, 8, 10, ...
            # when i=3, iterate over 6, 9, 12, ...
            for j in range(i*i, n+1, i):
                is_prime[j-2] = False    
    print([i[0] for i in enumerate(is_prime, 2) if i[1]])
    return [i[0] for i in enumerate(is_prime, 2) if i[1]]

# n = 2, Expected output: [2, 3]
sieve_of_eratosthene(3)
# n = 50, Expected output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
sieve_of_eratosthene(50)
# n = 100, Expected output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
sieve_of_eratosthene(100)
# sieve_of_eratosthene(360003811210086751)

is_prime = [True] * (1<<15)
def batch_sieve(i, j, primes):
    print((j-i+1))
    is_prime = [True] * (j-i+1)
    # print(i, j)
    for prime in range(i, j+1):
        if is_prime[prime-i]:
            for k in range(2*prime, j+1, prime):
                is_prime[k-i] = False
    # print(is_prime)
    return [i[0] for i in enumerate(is_prime, i) if i[1]]

def batch_sieve_old(i, j, primes):
    for x in range(i, j):
        is_prime = True
        for prime in primes:
            if x % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)

def optimized_sieve(n):
    primes = []
    for i in range(2, n+1, 1<<15):
        # print(i, i+1<<15)
        primes += batch_sieve(i, min(n, i+1<<15), primes)
    
    return primes

import math
# print(optimized_sieve(100))
# print(optimized_sieve(int(math.sqrt(3600036751))))
# print(optimized_sieve(int(math.sqrt(360003811210086751))))

def optimized_prime(n):
    primes = []
    for i in range(2, int(math.sqrt(n)) + 1, 50):
        pass

# Python3 program to print all primes
# smaller than n, using segmented sieve
import math
prime = []

# This method finds all primes
# smaller than 'limit' using
# simple sieve of eratosthenes.
# It also stores found primes in list prime
def simpleSieve(limit):
	
	# Create a boolean list "mark[0..n-1]" and
	# initialize all entries of it as True.
	# A value in mark[p] will finally be False
	# if 'p' is Not a prime, else True.
	mark = [True for i in range(limit + 1)]
	p = 2
	while (p * p <= limit):
		
		# If p is not changed, then it is a prime
		if (mark[p] == True):
			
			# Update all multiples of p
			for i in range(p * p, limit + 1, p):
				mark[i] = False
		p += 1
		
	# Print all prime numbers
	# and store them in prime
	for p in range(2, limit):
		if mark[p]:
			prime.append(p)
			print(p,end = " ")
			
# Prints all prime numbers smaller than 'n'
def segmentedSieve(n):
	
	# Compute all primes smaller than or equal
	# to square root of n using simple sieve
	limit = int(math.floor(math.sqrt(n)) + 1)
	simpleSieve(limit)
	
	# Divide the range [0..n-1] in different segments
	# We have chosen segment size as sqrt(n).
	low = limit
	high = limit * 2
	
	# While all segments of range [0..n-1] are not processed,
	# process one segment at a time
	while low < n:
		if high >= n:
			high = n
			
		# To mark primes in current range. A value in mark[i]
		# will finally be False if 'i-low' is Not a prime,
		# else True.
		mark = [True for i in range(limit + 1)]
		
		# Use the found primes by simpleSieve()
		# to find primes in current range
		for i in range(len(prime)):
			
			# Find the minimum number in [low..high]
			# that is a multiple of prime[i]
			# (divisible by prime[i])
			# For example, if low is 31 and prime[i] is 3,
			# we start with 33.
			loLim = int(math.floor(low / prime[i]) *
										prime[i])
			if loLim < low:
				loLim += prime[i]
				
			# Mark multiples of prime[i] in [low..high]:
			# We are marking j - low for j, i.e. each number
			# in range [low, high] is mapped to [0, high-low]
			# so if range is [50, 100] marking 50 corresponds
			# to marking 0, marking 51 corresponds to 1 and
			# so on. In this way we need to allocate space
			# only for range
			for j in range(loLim, high, prime[i]):
				mark[j - low] = False
				
		# Numbers which are not marked as False are prime
		for i in range(low, high):
			if mark[i - low]:
				print(i, end = " ")
				
		# Update low and high for next segment
		low = low + limit
		high = high + limit

# Driver Code
n = 100
print("Primes smaller than", n, ":")
segmentedSieve(int(math.sqrt(360003811210086751)))

# This code is contributed by bhavyadeep
