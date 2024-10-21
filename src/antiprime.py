## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main() :
	x=int(intput("Enter a positive integer number: "))
	y=1
	r=0
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	while y <= x:
		if x % y == 0:
			r=r+1
		y=y+1

	l=x-1
	s=0
	while l<=1 and s<r:
		a=1
		s=0
		while a<=l:
			if l % a == 0:
				s=s+1
			a=a+1
		if s>=r:
			return("not anti-prime")
		l=l-1
	return("anti-prime")


	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
	
## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main())
