string = 'aioue'
s = "abciiidef"
k = 3
window=s[:k]
max_vowels= sum(1 for char in window if char in string)
current_vowels = max_vowels
for i in range(k,len(s)):
    if s[i] in string:
        current_vowels+=1
    if s[i-k] in string:
        current_vowels-=1
    max_vowels=max(max_vowels,current_vowels)

print(max_vowels)

