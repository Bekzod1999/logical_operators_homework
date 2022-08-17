from re import X


def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    #9 < x < 1000

    y = x%10 # 3
    x = x//10 #32
    z = x//10 #32%10 =2
    #x=x//10 #32//10 =3
    return (y == x or y == z) and y!=0