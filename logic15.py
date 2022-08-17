def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
   
    y=a%10 #3
    a=a//10 #12
    z=a//10 #1
    a=a%10
    sum = y+z+a
    return sum%2==1