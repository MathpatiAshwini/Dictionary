# Write a Python program to check whether a given key already exists in a dictionary.
z=int(input("enter the length of dictionary:-"))
a={}
i=0
while i<z:
    b=input("enter the keys:-")
    c=input("enter the values:-")
    a[b]=c
    i=i+1
print(a)
z=input("enter key")
for i in a:
    if i==z:
        print("yes already exsits")
