import decorators

# Sieve of Eratosthenes


@decorators.timeit
def primes_sieve2(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for(i, isprime) in enumerate(a):
        if isprime:
            # yield i  # Turn into generator
            for n in range(i*i, limit, i):
                a[n] = False
    return a


primes_sieve2(2000000)


