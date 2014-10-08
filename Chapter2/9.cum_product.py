def cumulative_product(x):
	y=[]
	p=1
	for i in x:
		p=p*i
		y.append(p)
	print y


cumulative_product([1,2,3,4,5])



