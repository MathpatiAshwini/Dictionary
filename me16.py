d =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
sum=0
for i in d.values():
  for k in i:
    sum+=1
print(sum)