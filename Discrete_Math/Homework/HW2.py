#Q4
def sieve(n):
    if n <= 1:
        return "The number provided has to be higher than 1."
    
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False #Set the numbers 0 and 1 as false sice they aren't prime numbers

    p = 2 #Start at 2 since it is first prime

    while p * p <= n:
        if is_prime[p] == True:
            for i in range(p * p, n + 1, p): #Set the multiples of primes as false
                is_prime[i] = False
        p += 1
    
    prime_nums = [i for i in range(n + 1) if is_prime[i]]
    return prime_nums

number = int(input("Input a number: "))
result = sieve(number)

print(f"The result = {result}")


#--------#


#Q5
def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    
    old_s, s = 1, 0
    old_t, t = 0, 1
    old_r, r = a, b
    
    #Use euclidean algorithm to calculate while the remainder is not 0
    while r != 0:
        quotient = old_r // r

        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    
    #old_r is the greates common denominator (gcd), old_s and old_t are the coefficient
    return (old_r, old_s, old_t)

a, b = int(input("Enter the first positive integers: ")), int(input("Enter the second positive integers: "))
print(egcd(a, b))