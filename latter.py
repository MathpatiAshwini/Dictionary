a=['ankit','ajay','rohan','rohit','sanaya','sanjay']
b=[]
i=0
while i<len(a):
    p=a[i]
    c=0
    for j in p:
        if a[i]==p[j+1]:
            c+=1
        b.append(c)
    i+=1
print(b)

