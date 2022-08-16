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
    #123456
    a = n%10#6
    n=n//10 #12345

    b = n%10#5
    n=n//10 #1234

    c = n%10#4
    n=n//10 #123

    d = n%10#3
    n=n//10 #12

    e = n%10#2
    f=n//10 #1
    return a + b + c + d +f

