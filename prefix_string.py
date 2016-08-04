def define(string):
    """ Returns a string with the "DEFINE: " prefix

    >>> define('abc')
    'DEFINE: abc'
    """
    return 'DEFINE: ' + string

if __name__ == "__main__":
    import doctest
    doctest.testmod()
