# Write a Python program to count the number of items in a dictionary value that is a list.
# Sample output: 5
dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# ctr = sum(map(len, dict.values()))
# print(ctr)

count=0
for i in dict:
    v=dict[i]
    for j in v:
        count+=1
print(count)

