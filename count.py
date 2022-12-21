dict="aabracadabraaabbccrr"
count={}
n=0
l=[]
for i in dict:
    if i not in l:
        l.append(i)
        count[i]=0
    n+=1
    count[i]=count[i]+1
print(count)
print(l)