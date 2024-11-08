def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    else:
        return n * skip_mul(n - 2)


def multiply(m, n):
    """ Takes two positive integers (including zero) and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    if n == 0:
        return 0
    return m + multiply(m,n-1)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i,count):
        if i >= n:
            return count
        else:
            if n%i == 0:
                count += 1
        return helper(i+1,count)    
    
    return (helper(1,0) <= 1)

