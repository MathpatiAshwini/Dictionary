# Write a Python program to check all values are same in a dictionary. Go to the editor
z={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
x=list(z.values())
count=0
j=0
while j<len(x):
    if x[0]==x[j]:
        count+=1
    j+=1
if count==4:
    print('true')
else:
    print("no")
  

q=z['Cierra Vega']
count=0
for i in z:
    if z[i]==q:
        count+=1
if count==len(z):
    print("true")
else:
    print("no")