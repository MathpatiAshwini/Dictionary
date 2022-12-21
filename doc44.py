a={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
b=list(a.values())
c=list(a.keys())
d={}
e={}
f={}
g={}
i=0
while i<len(a):
    j=0
    while j<len(b[i]):
        d[c[i]]=b[i][0]
        e[c[i]]=b[i][1]
        f[c[i]]=b[i][2]
        g[c[i]]=b[i][3]
        z=(d,e,f,g)
        j+=1
    i+=1
print(list(z))
