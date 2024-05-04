def mergeAlternately( word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """

    s = ''
    for char1, char2 in zip(word1, word2):
        s += char1 + char2

    s += word1[len(s)//2:] + word2[len(s)//2:]
    return s




print(mergeAlternately( 'abc', 'pqr'))
