a=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

b=[]
for i in a:
  for j in i.values():
    if j not in b:
      b.append(j)
    z=set(b)
print(z)

