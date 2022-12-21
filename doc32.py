# 32.Write a Python program to get the key, value and item in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# c=0
# print("key,value,count")
# for key ,value in d.items():
#     c+=1
#     print(" "+str(key)+" "+str(value)+" "+str(c))

for i in d:
    print(i,d[i],i)
