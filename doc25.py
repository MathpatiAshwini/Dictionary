a=input("enter the characters:--")
count={}
for i in a:
    if i in count.keys():
        count[i]+=1
    else:
        count[i]=1
print(count)