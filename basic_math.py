def mul(a, b):
    """ Returns the value of a multiplied by b

    :param a: The first multiple
    :type a: int.
    :param b: The second multiple
    :returns: int -- Equal to a * b
    """
    return a * b


def mul_div(a, b, c=1):
    """ Returns a*b/c
    """
    rtn = a * b
    rtn = rtn / c
    return rtn


def is_prime(a):
    """ Returns true if a is prime and false otherwise

    >>> is_prime(3)
    True
    >>> is_prime(1)
    False
    >>> is_prime(4)
    False
    """
    if a < 2:
        return False
    return all(a % i for i in range(2, a))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
