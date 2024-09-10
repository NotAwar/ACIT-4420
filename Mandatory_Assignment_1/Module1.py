def find_prime_factors(n, prime_factors=None):
    i = 3
    if prime_factors is None:
        prime_factors = []
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 2 # skipping by 2 to skip even numbers
    if n > 1:
        prime_factors.append(n)
    return prime_factors

# Call the function and print the output to test
result = find_prime_factors(56)
print(result)
