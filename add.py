d={'a':[2,3,4,5],'b':[4,8,7,3],'c':[9,6,5,8]}
for i in d:
	g=d[i]
	l=[]
	sum=0
	j=0
	while j<len(g):
		sum+=g[j]
		j+=1
	l.append(sum)
	d[i]=l
print(d)
