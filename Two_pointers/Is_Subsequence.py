s = "abc"
t = "ahbgdc"
i,j=0,0
while (j < len(t) and i < len(s)):
    if s[i]==t[j]:
        i+=1
    j+=1
if (i==len(s)):
    print(i)


