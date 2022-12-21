a=[2,2,2,3,3,3,5,5,1,1]
count={}
n=0
l=[]
for i in a:
    if i not in l:
        l.append(i)
        count[i]=0
    n+=1
    count[i]=count[i]+1
print(count)
for j in count.keys():
    count[j]=j*count[j]
print(count)

