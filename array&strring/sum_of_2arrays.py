def arrayStringsAreEqual( word1, word2):
    """
    :type word1: List[str]
    :type word2: List[str]
    :rtype: bool
    """
    word1 = ''.join(word1)
    word2 = ''.join(word2)
    if word1 ==word2:
        return True
    else:
        return False

word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(arrayStringsAreEqual(word1,word2))
