a=['one','two','three']
b={}
i=0
while i<len(a):
    b[i+1]=a[i]
    i+=1
print(b)