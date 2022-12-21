a={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}

v={}
for i in a:
    m=a[i]
    if m[0]>=6 and m[1]>=10:
        v[i]=a[i]
print(v)