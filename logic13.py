def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    y=a%10
    z=a//10
    sum = y+z
    return sum%2 == 0