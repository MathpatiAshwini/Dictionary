
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
 
user=input("enter the key")
sum=0
for i in student:
    for j in i:
        if j==user:
            sum=sum+i[j]
print(sum)
