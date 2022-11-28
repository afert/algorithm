def bubbleSort(line):


	count=0

	while count!=len(line)-1:

		count=0

		for i in range(0,len(line)-1):

			if line[i]>line[i+1]:
				n=line[i+1]
				line[i+1]=line[i]
				line[i]=n
			else:
				count+=1
				
	return line


if __name__=="__main__":

	line=[-4,-1,9,0,3,10]

	print(bubbleSort(line))