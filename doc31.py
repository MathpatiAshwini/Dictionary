# Write a Python program to get the top three items in a shop. Go to the editor
a={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

b=list(a)
c=[]
i=0
while i<len(b):
    b.sort(reverse=True)
    x=b[i]
    c.append(x)
    d=c[:3]
    i+=1
print(i,":",d)

# for x, y in a.items():
#   print(x,":" ,y)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)
