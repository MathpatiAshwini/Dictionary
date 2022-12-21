a={1:20,2:50,3:50,4:30,5:25,6:30}
count=0
c=list(a.values())
print(c)
b={}
for i in a:
    d=[]
    for j in a:
        if a[i]==a[j]:
            d.append(j)
    b[a[i]]=d
print(b)
 





    
