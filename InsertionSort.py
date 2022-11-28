def insertSort(line):
	for j in range(1,len(line)):
		k=j-1
		val=line[j]

		while k>=0 and val<line[k]:
			
				line[k+1]=line[k]

				k-=1
		line[k+1]=val
	return line




if __name__=="__main__":

	line=[-4,-1,9,0,3,10]

	print (insertSort(line))
