#!/usr/bin/python
def fact( n ):
        if n<1:
		return 1
	else:
		result = n * fact( n - 1 )
		print(str(n) + '! = ' + str(result))
		return result
fact(3)

