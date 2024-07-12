n=[7,1,5,3,6,4]
start=0
end=0
profit=0
while end <= len(n)-1 :
    if n[end] >= n[start]:
        profit=max(profit,n[end]-n[start])
        end+=1
    else:
       start+=end
       end+=1

print(profit)






