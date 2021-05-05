import numpy as np

mat1 = np.array([[1,2],[3,4]])

def padding (mat1, pad):

	row, col = mat1.shape

	row2 = 0
	col2 = 0

	row2 = row + 2*pad
	col2 = col + 2*pad

	matres = np.zeros((row2, col2))

	for i in range(pad, row2-pad):
		for j in range(pad, col2-pad):
			matres[i][j] = mat1[i-pad][j-pad]

	return matres

print padding(mat1, 1)
