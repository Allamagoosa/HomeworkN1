#!/usr/bin/python
def factorial(x):
    """ Test ====  
    >>> factorial(5)
    120
    """ 

    result = 1
    for i in range(1, x+1):
        result = result*i
    return result


def factorial_recursive(x):
    """ Test ==============  
    >>> factorial_recursive(6)
    720
    """

    if x <= 1: 
        return 1
    else: 
        return x*factorial_recursive(x-1)


def viete(b=-5, c=6):
    """Test==========
    >>> viete(-4, 4)
    (2, 2)
    """

    x1 = None
    x2 = None
    x = (None, None)
    for i in range(-10, 11):
        for j in range (-10, 11):
            if (i+j == -b) and (i*j == c):
                x = (i, j)
    return x

#print factorial(21), factorial_recursive(9), viete()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
