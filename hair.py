a=int(input("enter the number:--"))
i=0
m={}
p={}
while i<a:
    p["hair"]=input("enter the name of person:--")
    p["eyes"]=input("enter the hair colore of the person:--")
    p["heigth"]=input("enter the colore of eyes:--")
    # z=input("enter the heigth:--")
    a=input("enter the name")
    m[a]=p
    i+=1
print(m)


# a={'company':{'name':10,'b':{'c':12,'d':20}}}
# p=a['company']['name']
# q=a['company']['b']['c']
# k=a['company']['b']['d