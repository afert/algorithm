def fibonacciSearch(line,target):
	n=len(line)

	f2=0
	f1=1
	f=1

	while f<n:
		f2=f1
		f1=f
		f=f1+f2

	offset=-1



	while f>=1:

		i=min(f2+offset,n-1)

		print ("i is: {}".format(i))




		if line[i]<target:
			f=f1
			f1=f2
			f2=f-f1

			offset=i

			

		elif line[i]>target:
			f=f2
			f1=f1-f2
			f2=f-f1
			
		else:
			return i
	return -1



if __name__=="__main__":

	line=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
	print (fibonacciSearch(line,4))

