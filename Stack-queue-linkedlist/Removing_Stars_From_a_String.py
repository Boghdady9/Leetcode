def removeStars(self, s):
    """
    :type s: str
    :rtype: str
    """
    items = []
    for char in s:
        if char != '*':
            items.append(char)
        else:
            if items:
                items.pop()
    return ''.join(items)   