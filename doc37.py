# d={9:'sam',2:'ram',3:'wor',22:'rose',1:'ram'}
# for key in d.items():
#     b=sorted(d[key])
#     x=set(b)
# print(x)


# a=['kelly','emma']
# b={'desagmaton':'deueloper','salary':8000}
# q=list(b)
# for i in b.keys():
#     print(b.update(a))

# d={'s':{'d2':{1:{2:3,4:3}}}}
# print(d["s"]["d"][3])
# d={"class":{"students":{"name":'mike','math':{'physecs':70,'history':80}}}}
# print(d["class"]["students"]["math"]["physecs"])
# # print()


# a=int(input("enter  the no.of beds....."))
# b=int(input(" enter the no.of girls..."))
# c=int(input(" enter the room no:"))
# if a>b:
#     if a==b:
#         print(a-b,"girls are left")
# if a<b:
# 	if a==0:
# 		print(b-a," beds are left")
# else:
# 	print("go to another room")

# from pprint import pprint
# dict_nums = dict(x=list(range(11, 20)), y=list(range(21, 30)), z=list(range(31, 40)))
# pprint(dict_nums)
# print(dict_nums["x"][4])
# print(dict_nums["y"][4])
# print(dict_nums["z"][4])
# for k,v in dict_nums.items():
#    print(k, "has value", v)


# a={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# b=[]
# for i in 'x','y','z':
#     # p=len(key)//2
#     # print(key[p])

#     print(a.keys(),"has value",a[i])


# a={'a':'ram','b':'tanu'}
# for i in a:
#     for j in a[i]:
#         print(j)
#     print()
