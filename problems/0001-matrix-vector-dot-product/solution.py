def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	col_a= len(a[0])
	if col_a != len(b):
		return -1
	
	ans = []
	for row in a:
		sum_ = 0
		for i in range(col_a):
			sum_+=(row[i]*b[i])
		ans.append(sum_)
	
	return ans

