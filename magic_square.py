# Magic square is square matrix of numbers in which the addition of numbers in row-wise and column wise and diagonal wise  
def generate_square(n):
	ms=[[0 for i in range(n)]for j in range(n)]
	(i,j)=(n//2,n-1)
	num=1
	while(num<=n*n):
		if i==-1 and j==n:
			(i,j)=(0,n-2)
		else:
			if i<0:
				i=n-1
			if j==n:
				j=0
		if ms[i][j]:
			j-=2
			i+=1
			continue
		else:
			ms[i][j]=num
			num+=1
		i-=1
		j+=1
	for i in range(n):
		for j in range(n):
			print(ms[i][j],end=" ")
		print()
n=int(input("Enter the size of the square: "))
generate_square(n)