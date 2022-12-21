a=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
b=[]
i=0
while i<len(a):
    if 'id'=='#FF0000':
        b=a[i]
        # break
    else:
        b[i]=a[i][1]
    i+=1
print((b)