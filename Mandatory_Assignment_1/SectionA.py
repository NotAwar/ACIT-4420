def find_prime_factors(n, prime_factors=None):
    if prime_factors is None:
        prime_factors = []
        
    # Handle the factor 2 first to skip even numbers later
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    i = 3
   
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 2 # skipping by 2 to skip even numbers
    if n > 1:
        prime_factors.append(n)
    return prime_factors

# Call the function and print the output to test the results
print(find_prime_factors(56))   # Output: [2, 2, 2, 7]
print(find_prime_factors(97))   # Output: [97] (prime number)
print(find_prime_factors(100))  # Output: [2, 2, 5, 5]
print(find_prime_factors(1))    # Output: [] (no prime factors for 1)
print(find_prime_factors(2))    # Output: [2]