def find_prime_factors(n, prime_factors=[]):
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors

# Call the function and print the output to test
result = find_prime_factors(56)
print(result)
