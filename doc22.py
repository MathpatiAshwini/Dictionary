a= {'1':['a','b'], '2':['c','d']}
list= list(a.values())
for i in list[0]:
    for j in list[1]:
        print(i+j)
# i=0
# s=my_list[0]
# t=s[-1]
# while i<len(s):
#     j=0
#     while j<len(s):
#         print(s[i]+t[i])
#         j=j+1
#     i=i+1
