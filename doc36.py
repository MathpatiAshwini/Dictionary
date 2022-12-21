
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for a,b in zip(x,y):
    if x[a] == y[b]:
        print(b,": is present in both a,b")
