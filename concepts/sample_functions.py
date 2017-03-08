def get_middle(s):
    """
    Returns two letters from the center for even words and one for odd
    """
    if (len(s) <= 2):
        return s
    if ((len(s) % 2) == 0):
        chunk = (len(s)/2)-1
        return s[chunk:-chunk]
    else:
        chunk = int(len(s)/2)
        return s[chunk:-chunk]