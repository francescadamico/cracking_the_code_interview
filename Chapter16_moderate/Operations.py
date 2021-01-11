''' write methods to implement the multiply, divide and subtract operations for integers. The results of all these are integers. You can use the add operator, but not minus, times or divide.'''


def multiply(A, B):

	# returns A*B
	R = 0
	for _ in range(A):
		R += B

	return R

def divide(A, B):
	
	# returns A/B	
	summ = 0
	R = 0

	if A < B:
		return 0

	while summ < A:
		R += 1
		summ += B

	return R

def subtract(A, B):
	
	# returns A-B
	R= 0

	if A >= B:
		while R + B != A:
			R += 1
		return R
	else:
		while R + A != B:
			R += 1 
		return -R	


A = 4
B = 8

M = multiply(A, A) # 32
D = divide(A, A) # 0
D1 = divide(B, A) # 2
S = subtract(A, A) # 

print(M, D, D1, S)
	

