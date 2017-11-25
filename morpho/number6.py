#python2

if __name__ == "__main__":
	N =  int(raw_input())
	length_of_binary =len(format(N,'b'))
	a = length_of_binary-1
	b = format((N-2**a+1),'b').count('1')

	print a+b


