def gcdOfStrings( str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    if (str1 + str2) == (str2 + str1):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        lengthOfCommonString = gcd(len(str1), len(str2))

        return str1[0:lengthOfCommonString]

    return ""









str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings( str1, str2))
