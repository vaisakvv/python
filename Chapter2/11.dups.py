def dups(x):
	y=[]
	j=0
	for i in x:
		y.append(y[j])
		for k in y:
			if i==j:
				y.append(i)
		j
	print y
