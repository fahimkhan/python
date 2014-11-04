

def call(a):
	if a==1:
		return 
	
        elif a%2==0:
		print a
		a=a/2
		call(a)
	else:
		print a
		a=a*3+1
		call(a)




