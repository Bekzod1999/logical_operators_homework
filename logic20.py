def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.

    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    #0 < n < 100000
    # 101001
    k = 6
    a = n % 10  # 1
    n = n//10  # 10100

    b = n % 10  # 0
    n = n//10  # 1010

    c = n % 10  # 4
    n = n//10  # 123

    d = n % 10  # 3
    n = n//10  # 12

    e = n % 10  # 2
    k += e
    f = n//10  # 1
    k += f
    k -= (a + b + c + d + f)
    return k > 3
x=main(110)
print(x)
