dic={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}

# P= {x.replace(' ', ''): v 
#      for x, v in p.items()}
# print (" New dictionary : ", P)

a={}
for i in dic:
     j=0
     v=" "
     while j<len(i):
          if i[j]!=" ":
               v=v+i[j]
          j+=1
     a[v]=dic[i]
print(a)
