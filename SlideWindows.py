def slideWindow(s):
	left=right=0
	n=len(s)
	line=[]


	while right<n:

		while s[right] in line:

			line.remove(s[left])
			left+=1

		line.append(s[right])
		right+=1

		print ("the length is: {} and the list is: {}".format(len(line),line))


if __name__=="__main__":

	s="abcabcbb"

	slideWindow(s)