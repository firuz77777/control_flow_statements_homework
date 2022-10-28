def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2. If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
    s=0
    if a > 0:
        s = a + 1 
    else :
        s = a - 2 
    if a == 0:
        s = 10
    return s
print(main(0))