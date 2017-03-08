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

def get_middle_refactor(s):
   return s[(len(s)-1)/2:len(s)/2+1]

"""
Print cases para get_middle
"""
print get_middle("test")
print get_middle("testing")
print get_middle("middle")
print get_middle("A")
print get_middle("of")

"""
Print cases para get_middle_refactor
"""
print get_middle_refactor("test")
print get_middle_refactor("testing")
print get_middle_refactor("middle")
print get_middle_refactor("A")
print get_middle_refactor("of")
