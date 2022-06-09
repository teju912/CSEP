#factorial of a number using recursion
def recur_factorial(n):
	if n==1:
		return n
	else:
		return n*recur_factorial(n-1)
num=7
#check if the number is negative or not
if num<0:
	print("the factorial doesnot exist as it is negative")
elif num==0:
	print("the factorial doesnot exist for zero")
else:
	print("the factorial of number",num,"is",recur_factorial(num))
