# Q29.Write a Python program to sort a list alphabetically in a dictionary.

a=[{'rajeshri':100,'nagnath':90,'ankita':200,'kapil':10,'ashwini':5}]
z={}
i=0
while i<len(a):
    for j in a[i]:
        z[j]=a[i][j]
    i+=1
p=sorted(z.items())
print(dict(p))