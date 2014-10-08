def dups(x):
	y=[]
	for i in x:
		if x.count(i)>1:
			y.append(i)
	print y



x=[1,2,3,1,1,4,3]
dups(x)

