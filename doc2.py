d='w3resoource'
a={}
b=[]
for i in d:
    if i not in b:
        b.append(i)
        x=d.count(i)
        a[i]=x
print(a  )