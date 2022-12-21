a={'a':3,'b':15,'c':20}
z=list(a)
sum=0
i=0
while i<len(z):
    sum+=a[z[i]]
    i+=1
print(sum)