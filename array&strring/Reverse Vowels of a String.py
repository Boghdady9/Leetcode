def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowles='aioueAIOUE'
    s=list(s)
    i=0
    j=len(s)-1
    while i<j:
        if s[i] in vowles and s[j] in vowles:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        if s[i] not in vowles:
            i+=1
        if s[j] not in vowles:
            j-=1
