s="A man, a plan, a canal: Panama"
s = (s.lower())
s=''.join(e for e in s if e.isalnum())
if s==s[::-1]:
    print(True)
else:
    print(False)
