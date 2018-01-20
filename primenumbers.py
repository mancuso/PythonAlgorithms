import decorators

# Sieve of Eratosthenes


@decorators.timeit
def primes_sieve(limit):
    """ Return list of primes smaller than limit as list indexes marked as true - O(n(logn)(loglogn))     """
    a = [True] * limit
    a[0] = a[1] = False

    for(i, isprime) in enumerate(a):
        if isprime:
            # yield i  # Turn into generator
            for n in range(i*i, limit, i):
                a[n] = False
    return a


@decorators.timeit
def isprime(n):
    """ Returns True if n is prime using deterministic AKS primality test - O(log(n)^12)    """
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


primes_sieve(2000000)
print(isprime(508012429))
