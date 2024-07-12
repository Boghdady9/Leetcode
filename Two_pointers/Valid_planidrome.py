s="A man, a plan, a canal: Panama"
s = (s.lower())
s=''.join(e for e in s if e.isalnum())
left=0
right=len(s)-1
while left != right:
    if s[left]==s[right]:
        left+=1
        right-=1
    else:
        print("Not a palindrome")
        break
print("Palindrome")