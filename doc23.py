# # 3.Write a Python program to find the highest 3 values of corresponding keys in a dictionary
a={'a':20,'b':300,'c':5000,'d':100,'e':500}
b=list(a.values())
c=[]
i=0
while i<len(b):
    b.sort(reverse=True)
    x=b[i]
    c.append(x)
    d=c[:3]
    i+=1
print(d)



