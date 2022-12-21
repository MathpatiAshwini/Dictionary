# # write a Python program to remove duplicates from Dictionary.
m = {'id1':{'name':['Sara'],'class':['V'],'subject_integration':['english, math, science']},
'id2':{'name':['David'],'class':['V'],'subject_integration':['english, math, science']},
'id3':{'name': ['Sara'],'class': ['V'],'subject_integration':['english, math, science']},
'id4':{'name': ['Surya'],'class': ['V'],'subject_integration':['english, math, science']}}
r = {}
for key,value in m.items():
    if value not in r.values():
        r[key] = value
print(r