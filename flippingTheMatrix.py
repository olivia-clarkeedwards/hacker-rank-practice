#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
	target_length = len(matrix) // 2
	result = 0
	
	for row in range(target_length):
		for col in range(target_length):
			val1 = matrix[row][col]
			val2 = matrix[row][len(matrix) - col - 1]
			val3 = matrix[len(matrix) - row - 1][col]
			val4 = matrix[len(matrix) - row - 1][len(matrix) - col - 1]

			result += max(val1, val2, val3, val4)
	
	return result
			
			
		
flippingMatrix(
	[[112, 42, 83, 119], 
  [56, 125, 56, 49], 
  [15, 78, 101, 43], 
  [62, 98, 114, 108]])

