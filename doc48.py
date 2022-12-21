a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
a={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}


h={}
for i in a:
    b=len(a[i])
    h[a[i]]=b
print(h)
