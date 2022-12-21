a={1:20,2:50,3:50,4:30,5:25,6:30}
p=list(a.keys())
q=list(a.values())
count=0
b={}
for i in a:
    if i not in b:
        count+=a[i]
        b[i]=count
print(b)