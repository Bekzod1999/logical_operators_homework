def main(a, b, c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    return (a < b and c > a) or (a > b and b > c)
x=main(6,4,1)
print(x)