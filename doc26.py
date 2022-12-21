dic = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

# for row in zip(*([key]+(value) for key, value in sorted(dic.items()))):
#     print(*row)

for i in dic:
    print(i,end=" ")
print()
