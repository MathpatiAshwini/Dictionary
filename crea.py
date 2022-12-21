a=int(input("enter the length odfthe dictionary --> "))
b={}
for i in range(a):
    x=input("enter the keys:-- ")
    y=input("enter the values:--")
    b.update({x:y})
print(b)
a2=int(input("enter the length odfthe dictionary--> "))
b2={}
for i in range(a2):
    x2=input("enter the keys:--")
    y2=input("enter the values:--")
    b2.update({x2:y2})
print(b2)
b.update(b2)
print("updated dictionary:--",b)