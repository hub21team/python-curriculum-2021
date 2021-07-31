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

# n = 2, Expected output: [2, 3]
sieve_of_eratosthene(3)
# n = 50, Expected output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
sieve_of_eratosthene(50)
# n = 100, Expected output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
sieve_of_eratosthene(100)



