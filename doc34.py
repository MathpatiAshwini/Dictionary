dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# Sample output: 5

count=0
for i in dict:
    v=dict[i]
    for j in v:
        count+=1
print(count)
