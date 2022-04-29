def relu(num : int) -> int:
    """
    >>> print(relu(5))
    5

    >>> print(relu(-2))
    0
    """
    return max(0, num)

if __name__ == '__main__':
    import doctest
    doctest.testmod()