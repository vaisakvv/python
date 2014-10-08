

def product(x):
	p=1	
	for i in x:
		p=i*p
	return p


def factorial(f):
	f=f+1
	g=range(f)
	print product(g[1:])



factorial(5)


	
	
