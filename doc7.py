dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
for i in (dic1,dic2,dic3):
    dic4.update(i)
print(dic4)

# for i in dic2:
#     dic1[i]=dic2[i]
# for j in dic3:
#     dic2[i]=dic3[i]
# print(dic1)
