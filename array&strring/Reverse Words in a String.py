def reverseWords( s):
    """
    :type s: str
    :rtype: str
    """
    lst = s.split()
    return (" ".join(lst[::-1]))
