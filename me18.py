# d=dict()
# for x in range(1,16): 
#     d[x]=x**2 
# print(d)

# a = {(1,2):1,(2,3):2}
# print(a[2,3])

dict1={"a":10,"b":2,"c":3}
str1=""
for i in dict1:
    str1=str1+str(dict1[i])+" "
    str2=str1[:-1]
print(str2[::-1])