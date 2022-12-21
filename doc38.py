a={'c1':'red','c2':'green','c3':None}
b={}
for k,v in a.items():
    if v!=None:
        b[k]=v
print(b)
