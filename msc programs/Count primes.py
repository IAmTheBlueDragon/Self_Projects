def countprimes(n):
	count=0
	if n<2:
		return(count)
	else:
		for i in range(1,n):
			for j in range(2,i):
				if i%j==0:
					break
			else:
				count=count+1
	return(count)
