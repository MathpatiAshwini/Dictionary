# a={'a':25,'b':10,'c':50,'d':100}
# z=a['z']=5000
# x=a['x']=1000
# print(z)
# x=len(a)
# print(x)

user=input("enter the time:")
if user[-2:]=="AM" or user[-2:]=="am":
    if user[:2]=="12":
        print("00"+user[2:8],'am')
    else:
        print(user[:8],'pm')
else:
    v=int(user[:2])
    if v<12:
        v=v+12
    
        print(str(v)+user[2:8],'pm')
