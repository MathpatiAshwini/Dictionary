# 0.Write a Python program to convert a given dictionary into a list of lists. 
a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# o/p[[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]

# b=[]
# for i in a:
#     b[i]=a
# print(list(b))
list=[]
for i in a:
    v=i,a[i]
    list.append(v)
print(list)