def doubleLinearSearch(line,target):
	left=0
	right=len(line)-1

	while left<=right:

		if line[left]==target:
			return left
		elif line[right]==target:
			return right
		else:
			left+=1
			right-=1

	return -1

if __name__=="__main__":

	line=[2,3,5,6,9,28,78]

	target=6

	print (doubleLinearSearch(line,target))
