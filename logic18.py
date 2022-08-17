def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
        #12345
    firstDigit = a%10 #5
    a = a//10 #1234
    twoDigit = a%10 #4
    a=a//10 #123
    threeDigit = a%10 #3
    a=a//10 #12
    fourDigit = a%10 #2
    fiveDigit = a//10 #1

    return firstDigit < twoDigit < threeDigit < fourDigit < fiveDigit