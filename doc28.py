
a = [1, 2, 3, 4]
c = {}
n=c
for i in a:
    c[i] = {}
    c = c[i]
print(n)
