m= {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
x=list(m.values())
d=dict()
x.sort(reverse=True)
x=x[:4]
print(x)